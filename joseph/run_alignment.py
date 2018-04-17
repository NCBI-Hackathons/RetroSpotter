import argparse
import os

parser = argparse.ArgumentParser(description='Align an SRA against a reference')

parser.add_argument('--sra', type=str, nargs=1, required=True,
                    help='The SRA ID')
parser.add_argument('--blast_db', type=str, nargs=1, required=True,
                    help='The blast db to search against')
parser.add_argument('--config_file', type=str, nargs=1, required=True,
                    help='The config file')
args = parser.parse_args()


def parse_config(config_file_location):

	config_dict ={}

	file = open(config_file_location, 'rt')

	for line in file:

		line_parsed = line.strip().split(':')

		config_dict[line_parsed[0]] = line_parsed[1]

	return config_dict


config_dict = parse_config(args.config_file[0])

def run_alignment():

	command = '{magicblast} -sra {sra} -db {blast_db} -no_unaligned -out {output}.sam'.format(
			magicblast=config_dict['magicblast'],
			sra= args.sra[0],
			blast_db=args.blast_db[0],
			output=args.sra[0]

		)

	os.system(command)

run_alignment()