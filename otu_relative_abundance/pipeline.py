import subprocess

"""
Python script to handle pre-processing code, creating graphs in R, and 
performing post-processing. 
"""

otu_file = "relative_otu_vectors_for_r_graphs_transposed.txt"
severity_file = "severity_file.tsv"

process = subprocess.Popen("Rscript mantel_relative_abundance.R " + severity_file + " " + otu_file,
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
std_output, std_error = process.communicate()

print(std_output)