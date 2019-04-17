import os
import sys
import re

# Append script path to import path to locate tass_eval
sys.path.append(os.path.realpath(__file__))

# Import evalTask1 function fro tass_eval module
from tass_eval import evalTask1

#
# MAIN
#
if __name__=="__main__":
	run_file = sys.argv[1]
	gold_file = sys.argv[2]

	scores = evalTask1(gold_file, run_file)
	print("f1_score: %f\n" % scores['maf1'])
	print("precision: %f\n" % scores['map'])
	print("recall: %f\n" % scores['mar'])
	print("accuracy: %f\n" % scores['a'])