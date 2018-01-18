import subprocess
from distance_calcs_relative_freq_otus import distance_calcs_relative_freq_asvs
"""
Python script to handle pre-processing code, creating graphs in R, and 
performing post-processing. 
"""
# custom file
custom_asv_relative_abundance_file = "relative_transposed.tsv"
# TODO fix transpose dataframe
asv_relative_changes_file = "relative_otu_vectors_for_r_graphs_transposed.tsv"
# Find the change in relative Amplicon Sequence Variant for

severity_file = "severity_file.tsv"
taxonomy_file = "taxonomy.tsv"

distance_calcs_relative_freq_asvs(custom_asv_relative_abundance_file, asv_relative_changes_file)

# TODO get names from metrics
def make_taxonomy_dict(taxonomy_file):

    taxonomy_dict = {}
    with open(taxonomy_file, 'r') as fin:
        next(fin)
        for line in fin.readlines():
            splitline = line.split('\t')
            taxonomy_dict[splitline[0]] = splitline[1]

    return taxonomy_dict

process = subprocess.Popen("Rscript mantel_relative_abundance.R " + severity_file + " " + "relative_otu_vectors_for_r_graphs_transposed.tsv",
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
std_output, std_error = process.communicate()

reformat = std_output.decode("utf-8")
reformat = reformat.split('\n')[:-1]

fout = open('results_file_011618.txt', 'w')

# TODO weird coding. return from R is odd...
for i in reformat:
    i = i[5:-1]
    i = i.split(',')
    i = '\t'.join(i)
    fout.write(i + '\n')

fout.close()


print(make_taxonomy_dict(taxonomy_file))