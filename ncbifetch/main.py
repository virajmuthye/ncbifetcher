
import configparser
import argparse

from ncbifetch.fetcher import battery


def main():
    # Part where the arguments are passed
    parser = argparse.ArgumentParser(description='Parse NCBI and then work with the biological data')

    parser.add_argument('-f', '--fetch', action='store_true',
                        help="Fetch from the ncbi")

    parser.add_argument('-i', '--index', action='store_true',
                        help="Resets the indexes")

    parser.add_argument('-p', '--pull', action='store_true',
                        help="Pull from storage")



    # Part where the config is parsed
    config = configparser.ConfigParser()
    config.read('ncbifetcher.config')

    email = config['OPTIONS']['email']
    location_index = config['INDEX']['index_location']
    location_storage = config['STORAGE']['location_storage']

    # battery('txid36190[Organism] mitochondria', location_storage, email)
    # parse_config()
    return 2+2



if __name__ == "__main__":
    main()
