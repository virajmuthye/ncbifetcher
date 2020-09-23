from Bio import Entrez
from bs4 import BeautifulSoup
import _pickle as pickle

query_from_user = "X16885.1"
# query_from_user = "starfish AND atp6"

Entrez.email = "wwinnett@iastate.edu"

handle = Entrez.esearch(db="nucleotide", term=query_from_user)
record = Entrez.read(handle)
gi_query = ",".join(record["IdList"])
handle = Entrez.efetch(db="nucleotide", id=gi_query, rettype="gb", retmode="xml")

# raw_data = handle.read()

raw_data = Entrez.read(handle)
r = 2

# soup = BeautifulSoup(raw_data)

# print(raw_data)
# with open("sandbox.txt", "wb") as current_file:
#     for line in raw_data:
#         current_file.write(line)


# raw_data = {'A': 2}
# with open('file.txt', 'wb') as file:
#     file.write(pickle.dumps(raw_data))







