
import subprocess

"""
Python script to handle pre-processing code, creating graphs in R, and 
performing post-processing. 
"""

otu_file = "/Volumes/JEN_DATA/autism_project/microbial_analysis/03_mapping/updated_mappings_110917/mapping_asd_dms/otu_relative_abundance/relative_otu_vectors_for_r_graphs_transposed.txt"

# lethargy = c(-1, -4, -1, 3, -6, -1, 0, 5, 6, 1, -2, 2, -6, -8, 11, 0, 1, 5, 1, 5, 4)
# hyperactivity = c(7, 2, 0, -2, -4, 2, 9, 6, 13, 7, 7, 1, 2, 1, 5, -4, -1, -4, 3, 0, -3)
# stereotypy = c(1, -1, 3, 4, 0, -1, 1, -1, 1, 2, -3, -2, -2, 0, 1, -2, -2, -2, 0, 0, 0)
# inapp_speech = c(0, 2, 4, 2, 1, 1, 5, 0, 4, 4, -3, 2, 1, -1, 5, -2, -3, -2, -1, 0, 1)


lethargy = [-1, -4, -1, 3, -6, -1, 0, 5, 6, 1, -2, 2, -6, -8, 11, 0, 1, 5, 1, 5, 4]
hyperactivity = [7, 2, 0, -2, -4, 2, 9, 6, 13, 7, 7, 1, 2, 1, 5, -4, -1, -4, 3, 0, -3]
stereotypy = [1, -1, 3, 4, 0, -1, 1, -1, 1, 2, -3, -2, -2, 0, 1, -2, -2, -2, 0, 0, 0]
inapp_speech = [0, 2, 4, 2, 1, 1, 5, 0, 4, 4, -3, 2, 1, -1, 5, -2, -3, -2, -1, 0, 1]

severity_metric_list = [lethargy, hyperactivity, stereotypy, inapp_speech]

process = subprocess.Popen("Rscript mantel_relative_abundance.R " + otu_file,
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
std_output, std_error = process.communicate()

print(std_output)