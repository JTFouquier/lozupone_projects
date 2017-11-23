# coding=utf-8


import subprocess

# get index
# print(header_list.index('SLURPEEFREQ'))
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

for line in mapping[1:]:
    splitline = line.strip().split('\t')
    sample_id = splitline[0]

    # print(sample_id + '\t' + splitline[header_list.index('Hyperactivity')])

    small_dict = {}
    for header_item in header_list[1:]:
        small_dict[header_item] = splitline[header_list.index(header_item)]

    asd_dict[sample_id] = small_dict

    # asd_dict[sample_id] = {
    #     'subject': splitline[header_list.index('Subject')],
    #     'sample_number': splitline[header_list.index('Sample_Number')],
    #     'irritability': splitline[header_list.index('Irritabilty')],
    #     'lethargy': splitline[header_list.index('Lethargy')],
    #     'stereotypy': splitline[header_list.index('Stereotypy')],
    #     'hyperactivity': splitline[header_list.index('Hyperactivity')],
    #     'inapp_speech': splitline[header_list.index('Inapp_Speech')],
    #     'slurpee': splitline[header_list.index('SLURPEEFREQ')],
    # }
# print('test', asd_dict)


differences_dict_double = {}
differences_dict_half = {}

for k1, v1 in asd_dict.items():
    # print(key_original, value_original)
    for k2, v2 in asd_dict.items():
        name_string = str(k1) + '_' + str(k2)
        if k1 != k2 and v1['Subject'] == v2['Subject']:

            if int(v1['Sample_Number']) < int(v2['Sample_Number']):
                print(int(v1['Sample_Number']) )

                # irritability_diff = int(v1['irritability']) - int(v2['irritability'])
                # lethargy_diff = int(v1['lethargy']) - int(v2['lethargy'])
                # stereotypy_diff = int(v1['stereotypy']) - int(v2['stereotypy'])
                # hyperactivity_diff = int(v1['hyperactivity']) - int(v2['hyperactivity'])
                # inapp_speech_diff = int(v1['inapp_speech']) - int(v2['inapp_speech'])
                # slurpee_diff = int(v1['slurpee']) - int(v2['slurpee'])


                # name_string = str(k1) + '__' + str(k2)

                small_dict = {}
                for header_item in header_list[3:]:
                    small_dict['first_comparison'] = k1
                    small_dict['second_comparison'] = k2
                    try:
                        small_dict[header_item + '_diff'] = int(v1[header_item]) - int(v2[header_item])

                    except:
                        small_dict[header_item + '_diff'] = 999


                differences_dict_half[name_string] = small_dict

                # differences_dict_half[name_string] = {
                #     'first_comparison': k1,
                #     'second_comparison': k2,
                #     'irritability_diff': irritability_diff,
                #     'lethargy_diff': lethargy_diff,
                #     'stereotypy_diff': stereotypy_diff,
                #     'hyperactivity_diff': hyperactivity_diff,
                #     'inapp_speech_diff': inapp_speech_diff,
                #     'slurpee_diff': slurpee_diff,
                # }
            else:
                small_dict = {}
                for header_item in header_list[3:]:
                    small_dict['first_comparison'] = k1
                    small_dict['second_comparison'] = k2
                    try:
                        small_dict[header_item + '_diff'] = int(v2[header_item]) - int(v1[header_item])
                    except:
                        small_dict[header_item + '_diff'] = 1000

                # irritability_diff = int(v2['irritability']) - int(v1['irritability'])
                # lethargy_diff = int(v2['lethargy']) - int(v1['lethargy'])
                # stereotypy_diff = int(v2['stereotypy']) - int(v1['stereotypy'])
                # hyperactivity_diff = int(v2['hyperactivity']) - int(v1['hyperactivity'])
                # inapp_speech_diff = int(v2['inapp_speech']) - int(v1['inapp_speech'])
                # slurpee_diff = int(v2['slurpee']) - int(v1['slurpee'])

            # name_string = str(k1) + '__' + str(k2)
            differences_dict_double[name_string] = small_dict

            # differences_dict_double[name_string] = {
            #     'first_comparison': k1,
            #     'second_comparison': k2,
            #     'irritability_diff': irritability_diff,
            #     'lethargy_diff': lethargy_diff,
            #     'stereotypy_diff': stereotypy_diff,
            #     'hyperactivity_diff': hyperactivity_diff,
            #     'inapp_speech_diff': inapp_speech_diff,
            #     'slurpee_diff': slurpee_diff
            # }

# print(json.dumps(differences_dict, sort_keys=True, indent=4))

dm_irritabilty = ''
dm_hyperactivity = ''
dm_stereotypy = ''
dm_inapp_speech = ''
dm_lethargy = ''
dm_slurpee = ''

column_headers = []
row_headers = []
print(asd_dict)


for key1 in sorted(asd_dict.keys()):
    print(key1)
    for key2 in sorted(asd_dict.keys()):
        print(key2)
        if str(key1) + '_' + str(key2) in differences_dict_double:



            irritabilty_value = differences_dict_double[str(key2) + '_' + str(key1)]['Irritabilty_diff']
            dm_irritabilty += str(-irritabilty_value) + '\t'

            hyperactivity_value = differences_dict_double[str(key2) + '_' + str(key1)]['Hyperactivity_diff']
            dm_hyperactivity += str(-hyperactivity_value) + '\t'

            stereotypy_value = differences_dict_double[str(key2) + '_' + str(key1)]['Stereotypy_diff']
            dm_stereotypy += str(-stereotypy_value) + '\t'

            inapp_speech_value = differences_dict_double[str(key2) + '_' + str(key1)]['Inapp_Speech_diff']
            dm_inapp_speech += str(-inapp_speech_value) + '\t'

            lethargy_value = differences_dict_double[str(key2) + '_' + str(key1)]['Lethargy_diff']
            dm_lethargy += str(-lethargy_value) + '\t'

            slurpee_value = differences_dict_double[str(key2) + '_' + str(key1)]['SLURPEEFREQ_diff']
            dm_slurpee += str(-slurpee_value) + '\t'

        else:
            dm_irritabilty += '0\t'
            dm_hyperactivity += '0\t'
            dm_stereotypy += '0\t'
            dm_lethargy += '0\t'
            dm_inapp_speech += '0\t'
            dm_slurpee += '0\t'

    dm_irritabilty += '\n'
    dm_hyperactivity += '\n'
    dm_stereotypy += '\n'
    dm_lethargy += '\n'
    dm_inapp_speech += '\n'
    dm_slurpee += '\n'

# print('\t'.join(sorted(asd_dict.keys())))
print('dm_irritabilty')
print(dm_irritabilty)
#
print('dm_hyperactivity')
print(dm_hyperactivity)
#
# print('dm_stereotypy')
# print(dm_stereotypy)
#
# print('dm_lethargy')
# print(dm_lethargy)
#
# print('dm_inapp_speech')
# print(dm_inapp_speech)


def print_graph_values(asd_severity_metric):
    """
    print just the values for Excel or R graphs
    """
    print('\n')
    print(asd_severity_metric)
    for key, value in sorted(differences_dict_half.items()):
        print(key + '\t' + str(-(value[asd_severity_metric + '_diff'])))

asd_severity_list = ['Lethargy', 'SLURPEEFREQ']



for i in asd_severity_list:
    print_graph_values(i)

