import subprocess
import sys
import os
from Bio.Align.Applications import ClustalwCommandline
import parametrai

def all(input_file, align_type, alignment_out, hmm_file, genome_database, transeq_output, number_frames):

	if align_type == "clustalw":
		cline = ClustalwCommandline("clustalw", infile=input_file, gapopen=10, gapext=0.5, outfile=alignment_out)
		child = subprocess.call(str(cline), shell=(sys.platform!="win32"))
	if align_type == "muscle":
		subprocess.run(["muscle", "-in", input_file, "-out", alignment_out])

	subprocess.run(["hmmbuild", hmm_file, alignment_out])
	subprocess.run(["transeq", genome_database, transeq_output, "-frame", number_frames])
	subprocess.run(["hmmsearch", hmm_file, transeq_output])

all(input_file=parametrai.input_file, align_type=parametrai.type, alignment_out=parametrai.output_file, hmm_file=parametrai.hmm_file, genome_database=parametrai.database, transeq_output=parametrai.new_database, number_frames=parametrai.frames)


	
	
	
	
	

