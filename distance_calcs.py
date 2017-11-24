# coding=utf-8

import subprocess
import json


#slightly modified mapping... removal of columns without ints
with open('mapping_longitudinal_asd_severity_only_distance_matrix_'
          'calculations_small.txt', 'r') as fin:
    mapping = fin.readlines()

asd_dict = {}
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
    for header_item in header_list[1:]:
        small_dict[header_item] = splitline[header_list.index(header_item)]

    asd_dict[sample_id] = small_dict


differences_dict_double = {}
differences_dict_half = {}

for k1, v1 in asd_dict.items():
    # print(key_original, value_original)
    for k2, v2 in asd_dict.items():
        name_string = str(k1) + '__' + str(k2)
        if k1 != k2 and v1['Subject'] == v2['Subject']:

            if int(v1['Sample_Number']) < int(v2['Sample_Number']):
                print(int(v1['Sample_Number']) )

                small_dict = {}
                for header_item in header_list[metric_start:]:
                    small_dict['first_comparison'] = k1
                    small_dict['second_comparison'] = k2
                    try:
                        small_dict[header_item + '_diff'] = int(v1[header_item]) - int(v2[header_item])

                    except:
                        small_dict[header_item + '_diff'] = 999

                differences_dict_half[name_string] = small_dict

            else:
                small_dict = {}
                for header_item in header_list[metric_start:]:
                    small_dict['first_comparison'] = k1
                    small_dict['second_comparison'] = k2
                    try:
                        small_dict[header_item + '_diff'] = int(v2[header_item]) - int(v1[header_item])
                    except:
                        small_dict[header_item + '_diff'] = 1000

            differences_dict_double[name_string] = small_dict

# print(json.dumps(differences_dict, sort_keys=True, indent=4))

dm_dict = {}
for header_item in header_list[metric_start:]:
    dm_dict[header_item] = ''

print(dm_dict)

for header_item in header_list[metric_start:]:

    for key1 in sorted(asd_dict.keys()):
        for key2 in sorted(asd_dict.keys()):

            if str(key1) + '__' + str(key2) in differences_dict_double:

                metric_value = differences_dict_double[str(key2) + '__' + str(key1)][header_item + '_diff']
                dm_dict[header_item] += str(-metric_value) + '\t'

            else:
                dm_dict[header_item] += '0\t'

        dm_dict[header_item] += '\n'

#print/write all metrics in header_list, and print in distance matrix form
# for header_item in header_list[metric_start:]:
#     print(dm_dict[header_item])

# print just the values for Excel or R graphs

def print_graph_values(asd_severity_metric):
    print('\n')
    print(asd_severity_metric)
    for key, value in sorted(differences_dict_half.items()):
        print(key + '\t' + str(-(value[asd_severity_metric + '_diff'])))

    metric_value_list = []
    for key, value in sorted(differences_dict_half.items()):
        metric_value_per_subject_comparison = str(-(value[asd_severity_metric + '_diff']))
        print(metric_value_per_subject_comparison)
        metric_value_list.append(metric_value_per_subject_comparison)

    return asd_severity_metric, metric_value_list

vectors_for_R_file = open('vectors_for_r_graphs.tsv', 'w')

# print/write all metrics in header_list, but make them in vector form
for header_item in header_list[metric_start:]:
    asd_severity_metric, metric_value_list = print_graph_values(header_item)
    print(metric_value_list)
    vectors_for_R_file.write(asd_severity_metric + '\t' + str("\t".join(metric_value_list)) + '\n')

vectors_for_R_file.close()