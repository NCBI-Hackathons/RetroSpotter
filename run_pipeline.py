import argparse
import os

parser = argparse.ArgumentParser(description='Run the data generation pipeline')

parser.add_argument('--bam_folder', type=str, nargs=1, required=True,
                    help='The directory containing the bam files.')
parser.add_argument('--source', type=str, nargs=1, required=True,
                    help='The source of the bam files e.g. AML')
parser.add_argument('--roi_start', type=int, nargs=1, required=True,
                    help='The 0 based start position of ROI')
parser.add_argument('--roi_end', type=int, nargs=1, required=True,
                    help='The 0 based end position of ROI')
parser.add_argument('--email', type=str, nargs=1, required=True,
                    help='Email for Entrez.')
parser.add_argument('--max_errors', type=int, nargs=1, required=True,
                    help='Number of times to try the API')
parser.add_argument('--file_comment', type=str, nargs=1, required=True,
                    help='text to add to file name')
args = parser.parse_args()
