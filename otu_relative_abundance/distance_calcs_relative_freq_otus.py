


"""
Input is as below which includes ASVs (amplicon sequence variants) and their
relative abundance per sample

#SampleID	Subject	Sample_Number	852bfcb95375282d779f638524d195fb	9327da197cd2232a4def87f314f833a9
stool.ASD.12.1	12	1	0.080176471	0.019352941
stool.ASD.12.2	12	2	0.014823529	0.011
stool.ASD.14.1	14	1	0	0.036352941
stool.ASD.14.2	14	2	0	0.020470588

For each OTU, this script finds the Euclidean distance between two different
relative abundance values for two different samples taken from the same person
on different sampling days.

These values can then be used in R to create scatterplots that map the
change one metric (microbial diversity, ASD severity, GI symptoms, etc)
compared to the change in another metric to look at within-person
changes and the relationship between metrics.
"""

with open('relative_transposed.tsv', 'r') as fin:
    mapping = fin.readlines()

metric_values_dict = {}
# get header_list from file
for line in mapping:
    splitline = line.strip().split('\t')
    header_list = splitline
    break

# start point of metric
metric_start = 3

for line in mapping[1:]:
    splitline = line.strip().split('\t')
    sample_id = splitline[0]

    small_dict = {}
    for metric_item in header_list[1:]:
        small_dict[metric_item] = splitline[header_list.index(metric_item)]

    metric_values_dict[sample_id] = small_dict

differences_dict = {}
for subject_key, metric_value_dict in metric_values_dict.items():
    for metric_name_key, metric_value in metric_values_dict.items():
        name_string = str(subject_key) + '__' + str(metric_name_key)
        if subject_key != metric_name_key and metric_value_dict['Subject'] == metric_value['Subject']:

            # we only need one comparison (i.e. sample 1 compared to sample 2
            # is sufficient. We do not need sample 2 compared to sample 1 also)
            if float(metric_value_dict['Sample_Number']) < float(metric_value['Sample_Number']):
                small_dict = {}
                for metric_item in header_list[metric_start:]:
                    small_dict['first_comparison'] = subject_key
                    small_dict['second_comparison'] = metric_name_key
                    small_dict[metric_item + '_diff'] = float(metric_value_dict[metric_item]) - float(metric_value[metric_item])

                differences_dict[name_string] = small_dict

dm_dict = {}
for metric_item in header_list[metric_start:]:
    dm_dict[metric_item] = ''


for metric_item in header_list[metric_start:]:
    for key1 in sorted(metric_values_dict.keys()):
        for key2 in sorted(metric_values_dict.keys()):
            dm_dict[metric_item] += '\t'

        dm_dict[metric_item] += '\n'

# print just the values for Excel or R graphs
# (TODO) transpose output or check R
def print_graph_values(metric):
    metric_value_list = []
    for key, value in sorted(differences_dict.items()):
        metric_value_per_subject_comparison = str(-(value[metric + '_diff']))
        metric_value_list.append(metric_value_per_subject_comparison)

    return metric, metric_value_list

vectors_for_R_file = open('vectors_for_r_graphs_relative_otus.tsv', 'w')

# print/write all metrics in header_list, but make them in vector form
for metric_item in header_list[metric_start:]:
    metric, metric_value_list = print_graph_values(metric_item)
    vectors_for_R_file.write(metric + '\t' + str("\t".join(metric_value_list)) + '\n')

vectors_for_R_file.close()