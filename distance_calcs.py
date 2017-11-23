# coding=utf-8


import subprocess


header_list = ['#SampleID', 'Subject', 'Sample_Number', 'Irritabilty', 'Lethargy', 'Stereotypy', 'Hyperactivity', 'Inapp_Speech',
'Age_In_Years', 'GI_Symptoms', 'Abdominal_Pain', 'Bloating', 'Loose_Stool', 'Constipation', 'Sample_Symptoms',
'CollectionDate', 'Location', 'Where_Moved_From', 'Time_From_First_Sample_Months', 'Special_Diets',
'Diet_Questionnaire_Date', 'WEIGHT', 'HEIGHTFEET', 'HEIGHTINCHES', 'BLACKAFRICAN', 'WHITE', 'HISPANIC', 'ASIAN',
'NATIVEINDIAN', 'OTHERETHNICITY', 'VITAMINREGULARUSE', 'VITAMINPILLDAYSAMOUNT', 'CHOCMILKFREQ', 'CHOCMILKQUAN',
'REDUCEDFATMILKFREQ', 'REDUCEDFATMILKQUAN', 'TYPEOFMILK', 'SOFTDRINKSFREQ', 'SOFTDRINKSQUAN', 'SODAAMOUNT', 'SLURPEEFREQ',
'HAWAIIANPUNCHFREQ', 'HAWAIIANPUNCHQUAN', 'HICFREQ', 'HICQUAN', 'ORANGEJUICEFREQ', 'ORANGEJUICEQUAN', 'OTHERJUICEFREQ',
'OTHERJUICEQUAN', 'BANANASFREQ', 'BANANASQUAN', 'APPLESPEARSFREQ', 'APPLESPEARSQUAN', 'ORANGESFREQ', 'ORANGESQUAN',
'STRAWBERRYFREQ', 'STRAWBERRYQUAN', 'CANNEDFRUITFREQ', 'CANNEDFRUITQUAN', 'OTHERFRUITFREQ', 'OTHERFRUITQUAN',
'PANCAKEFREQ', 'PANCAKEQUAN', 'BARSFREQ', 'BARSQUAN', 'EGGSFREQ', 'EGGSQUAN', 'BACONFREQ', 'COOKEDCEREALFREQ',
'COOKEDCEREALQUAN', 'COLDCEREALFREQ', 'COLDCEREALQUAN', 'COLDCEREALCODE', 'MILKONCEREALFREQ', 'GREENSALADFREQ',
'GREENSALADQUAN', 'SALADDRESSINGFREQ', 'BEANSPEASFREQ', 'BEANSPEASQUAN', 'PINTOBEANSFREQ', 'PINTOBEANSQUAN',
'REFRIEDBEANSFREQ', 'REFRIEDBEANSQUAN', 'CORNFREQ', 'CORNQUAN', 'TOMATOESFREQ', 'TOMATOESQUAN', 'GREENSFREQ',
'GREENSQUAN', 'BROCCOLIFREQ', 'BROCCOLIQUAN', 'CARROTSFREQ', 'CARROTSQUAN', 'SWEETPOTATOESFREQ', 'SWEETPOTATOESQUAN',
'FRIESFREQ', 'FRIESQUAN', 'WHITEPOTATOESFREQ', 'WHITEPOTATOESQUAN', 'OTHERVEGGIESFREQ', 'OTHERVEGGIESQUAN',
'RICEFREQ', 'RICEQUAN', 'SALSAFREQ', 'SPAGHETTIFREQ', 'SPAGHETTIQUAN', 'CHEESEDISHFREQ', 'CHEESEDISHQUAN',
'PIZZAFREQ', 'PIZZAQUAN', 'BURGERFREQ', 'BURGERQUAN', 'BURGERTYPE', 'TACOSFREQ', 'TACOSQUAN', 'TACOTYPE',
'HOTPOCKETFREQ', 'BEEFFREQ', 'BEEFQUAN', 'HAMBURGERHELPERFREQ', 'HAMBURGERHELPERQUAN', 'PORKFREQ', 'PORKQUAN',
'FRIEDCHICKENFREQ', 'FRIEDCHICKENQUAN', 'NOTFRIEDCHICKENFREQ', 'NOTFRIEDCHICKENQUAN', 'ANYFISHFREQ', 'ANYFISHQUAN',
'HOTDOGFREQ', 'HOTDOGQUAN', 'HAMFREQ', 'HAMQUAN', 'VEGGIESOUPFREQ', 'VEGGIESOUPQUAN', 'OTHERSOUPFREQ', 'OTHERSOUPQUAN',
'SALTYSNACKSFREQ', 'SALTYSNACKSQUAN', 'CRACKERSFREQ', 'CRACKERSQUAN', 'NACHOSFREQ', 'NACHOSQUAN', 'ICECREAMFREQ', 'ICECREAMQUAN',
'COOKIESFREQ', 'COOKIESQUAN', 'DOUGHNUTSFREQ', 'DOUGHNUTSQUAN', 'CAKEFREQ', 'CAKEQUAN', 'PIEFREQ', 'PIEQUAN', 'CHOCOLATECANDYFREQ',
'CHOCOLATECANDYQUAN', 'CANDYFREQ', 'CANDYQUAN', 'BISCUITSFREQ', 'BISCUITSQUAN', 'WHOLEWHEATBREADFREQ', 'WHOLEWHEATBREADQUAN',
'WHITEBREADFREQ', 'WHITEBREADQUAN', 'TORTILLASFREQ', 'TORTILLASQUAN', 'MARGARINEFREQ', 'MARGARINEQUAN', 'CHEESEFREQ',
'CHEESEQUAN', 'MAYOFREQ', 'PEANUTBUTTERFREQ', 'PEANUTBUTTERQUAN', 'JELLYFREQ', 'NUTSFREQ', 'NUTSQUAN', 'Description']

# get index
print(header_list.index('SLURPEEFREQ'))
import json

with open('mapping_longitudinal_asd_severity_only_distance_matrix_'
          'calculations.txt', 'r') as fin:
    next(fin)
    mapping = fin.readlines()

asd_dict = {}

for line in mapping:
    splitline = line.strip().split('\t')
    sample_id = splitline[0]

    print(sample_id + '\t' + splitline[header_list.index('Hyperactivity')])
    asd_dict[sample_id] = {
        'subject': splitline[header_list.index('Subject')],
        'sample_number': splitline[header_list.index('Sample_Number')],
        'irritability': splitline[header_list.index('Irritabilty')],
        'lethargy': splitline[header_list.index('Lethargy')],
        'stereotypy': splitline[header_list.index('Stereotypy')],
        'hyperactivity': splitline[header_list.index('Hyperactivity')],
        'inapp_speech': splitline[header_list.index('Inapp_Speech')],
        'slurpee': splitline[header_list.index('SLURPEEFREQ')],
    }

differences_dict_double = {}
differences_dict_half = {}

for k1, v1 in asd_dict.items():
    # print(key_original, value_original)
    for k2, v2 in asd_dict.items():
        if k1 != k2 and v1['subject'] == v2['subject']:

            if int(v1['sample_number']) < int(v2['sample_number']):
                irritability_diff = int(v1['irritability']) - int(v2['irritability'])
                lethargy_diff = int(v1['lethargy']) - int(v2['lethargy'])
                stereotypy_diff = int(v1['stereotypy']) - int(v2['stereotypy'])
                hyperactivity_diff = int(v1['hyperactivity']) - int(v2['hyperactivity'])
                inapp_speech_diff = int(v1['inapp_speech']) - int(v2['inapp_speech'])
                slurpee_diff = int(v1['slurpee']) - int(v2['slurpee'])
                name_string = str(k1) + '__' + str(k2)
                differences_dict_half[name_string] = {
                    'first_comparison': k1,
                    'second_comparison': k2,
                    'irritability_diff': irritability_diff,
                    'lethargy_diff': lethargy_diff,
                    'stereotypy_diff': stereotypy_diff,
                    'hyperactivity_diff': hyperactivity_diff,
                    'inapp_speech_diff': inapp_speech_diff,
                    'slurpee_diff': slurpee_diff,
                }
            else:
                irritability_diff = int(v2['irritability']) - int(v1['irritability'])
                lethargy_diff = int(v2['lethargy']) - int(v1['lethargy'])
                stereotypy_diff = int(v2['stereotypy']) - int(v1['stereotypy'])
                hyperactivity_diff = int(v2['hyperactivity']) - int(v1['hyperactivity'])
                inapp_speech_diff = int(v2['inapp_speech']) - int(v1['inapp_speech'])
                slurpee_diff = int(v2['slurpee']) - int(v1['slurpee'])

            name_string = str(k1) + '__' + str(k2)
            differences_dict_double[name_string] = {
                'first_comparison': k1,
                'second_comparison': k2,
                'irritability_diff': irritability_diff,
                'lethargy_diff': lethargy_diff,
                'stereotypy_diff': stereotypy_diff,
                'hyperactivity_diff': hyperactivity_diff,
                'inapp_speech_diff': inapp_speech_diff,
                'slurpee_diff': slurpee_diff
            }

# print(json.dumps(differences_dict, sort_keys=True, indent=4))

dm_irritability = ''
dm_hyperactivity = ''
dm_stereotypy = ''
dm_inapp_speech = ''
dm_lethargy = ''
dm_slurpee = ''

column_headers = []
row_headers = []

for key1 in sorted(asd_dict.keys()):
    for key2 in sorted(asd_dict.keys()):

        if str(key1) + '__' + str(key2) in differences_dict_double:

            irritability_value = differences_dict_double[str(key2) + '__' + str(key1)]['irritability_diff']
            dm_irritability += str(-irritability_value) + '\t'

            hyperactivity_value = differences_dict_double[str(key2) + '__' + str(key1)]['hyperactivity_diff']
            dm_hyperactivity += str(-hyperactivity_value) + '\t'

            stereotypy_value = differences_dict_double[str(key2) + '__' + str(key1)]['stereotypy_diff']
            dm_stereotypy += str(-stereotypy_value) + '\t'

            inapp_speech_value = differences_dict_double[str(key2) + '__' + str(key1)]['inapp_speech_diff']
            dm_inapp_speech += str(-inapp_speech_value) + '\t'

            lethargy_value = differences_dict_double[str(key2) + '__' + str(key1)]['lethargy_diff']
            dm_lethargy += str(-lethargy_value) + '\t'

            slurpee_value = differences_dict_double[str(key2) + '__' + str(key1)]['slurpee_diff']
            dm_slurpee += str(-slurpee_value) + '\t'

        else:
            dm_irritability += '0\t'
            dm_hyperactivity += '0\t'
            dm_stereotypy += '0\t'
            dm_lethargy += '0\t'
            dm_inapp_speech += '0\t'
            dm_slurpee += '0\t'

    dm_irritability += '\n'
    dm_hyperactivity += '\n'
    dm_stereotypy += '\n'
    dm_lethargy += '\n'
    dm_inapp_speech += '\n'
    dm_slurpee += '\n'

# print('\t'.join(sorted(asd_dict.keys())))
print('dm_irritability')
print(dm_irritability)

print('dm_hyperactivity')
print(dm_hyperactivity)

print('dm_stereotypy')
print(dm_stereotypy)

print('dm_lethargy')
print(dm_lethargy)

print('dm_inapp_speech')
print(dm_inapp_speech)


def print_graph_values(asd_severity_metric):
    """
    print just the values for Excel or R graphs
    """
    print('\n')
    print(asd_severity_metric)
    for key, value in sorted(differences_dict_half.items()):
        print(key + '\t' + str(-(value[asd_severity_metric + '_diff'])))

asd_severity_list = ['irritability', 'hyperactivity', 'stereotypy', 'inapp_speech', 'lethargy', 'slurpee']



for i in asd_severity_list:
    print_graph_values(i)

