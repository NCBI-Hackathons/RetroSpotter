import argparse
import os

parser = argparse.ArgumentParser(description='Create a BLAST DB')

parser.add_argument('--fasta_file', type=str, nargs=1, required=True,
                    help='The fasta_file')
parser.add_argument('--config_file', type=str, nargs=1, required=True,
                    help='The config file')
args = parser.parse_args()

config_dict = {}

def parse_config(config_file_location):

	file = open(config_file_location, 'rt')

	for line in file:

		line_parsed = line.strip().split(':')

		config_dict[line_parsed[0]] = line_parsed[1]

	return config_dict


config_dict = parse_config(args.config_file[0])

def create_blast_db():

	command = '{makeblastdb} -in {fasta} -dbtype nucl -parse_seqids -out {blastdb}'.format(
			makeblastdb=config_dict['makeblastdb'],
			blastdb = 'myblastdb',
			fasta = args.fasta_file[0]

		)


	os.system(command)




create_blast_db()