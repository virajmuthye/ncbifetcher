
__author__ = "Bill Winnett"
__email__ = "bwinnett12@gmail.com"

import glob
import os

from Bio import Entrez
from writer import battery_writer
from indexer import reset_indexes


# TODO - Have the user to input their email
# Parses the genebank and fetches what the user inputs
def parse_ncbi(query_from_user, output_type, email):

    # Always tell ncbi who you are. Using mine until testing is over and the user will input theirs
    Entrez.email = email

    # searches for those who fit your request
    handle = Entrez.esearch(db="nucleotide", term=query_from_user)

    # Records those who match the query and then formats them so it can fetch them
    record = Entrez.read(handle)
    gi_query = ",".join(record["IdList"])

    retmode_input = ("text", "xml")[output_type == "fasta"]

    # Fetches those matching IDs from esearch
    handle = Entrez.efetch(db="nucleotide", id=gi_query, rettype="gb", retmode=retmode_input)

    # for xml... if using .txt it should be handle.read()
    if output_type == "fasta":
        raw_data = Entrez.read(handle)
    else:
        raw_data = handle.read()

    return raw_data


# Something to run to run both functions. Ultimately will be done using R (Front End)
# TODO - make this neater
def battery(search_query, output_folder, email):

    xml_to_write = parse_ncbi(search_query, "fasta", email)
    text_to_write = parse_ncbi(search_query, "text", email)

    battery_writer("xml", xml_to_write, output_folder)
    battery_writer("text", text_to_write, output_folder)

    reset_indexes()


def delete_folder_contents():

    files = glob.glob('./storage/*/*')
    for f in files:
        os.remove(f)


def main():
    delete_folder_contents()

    # Edit this one to change search query
    test_genes = ['txid36190[Organism] mitochondria']

    # Edit this one to change location of storage (default ./storage)
    output_folder = "./storage/"
    # battery(test_genes, output_folder, "wwinnett@iastate.edu")


if __name__ == "__main__":
    main()
