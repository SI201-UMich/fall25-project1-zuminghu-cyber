# =========================================================
# SI 201: Project 1 – Data Analysis
# Name: Zuming Hu
# Student ID: 32862457
# Email: zuminghu@umich.edu
# Collaborators: Used GenAI to debug
# =========================================================

def load_file(filename):
    try:
        dict = {}
        f = open(filename, 'r')
        first_row = f.readline()
        seperated = first_row.split(',')
        for key in seperated[1:]:
            dict[key.strip('\n').strip('"')] = []

        for line in f:
            datas = line.split(',')
            dict['species'].append(datas[1].strip('\n').strip('"'))
            dict['island'].append(datas[2].strip('\n').strip('"'))
            dict['bill_length_mm'].append(datas[3].strip('\n').strip('"'))
            dict['bill_depth_mm'].append(datas[4].strip('\n').strip('"'))
            dict['flipper_length_mm'].append(datas[5].strip('\n').strip('"'))
            dict['body_mass_g'].append(datas[6].strip('\n').strip('"'))
            dict['sex'].append(datas[7].strip('\n').strip('"'))
            dict['year'].append(datas[8].strip('\n').strip('"'))
        f.close()
        return dict
    except FileNotFoundError:
        print(f"read file failed")
        return None

def file_information(dict):
    # file information
    print(f"The names of each column are:", end = '')
    for name in list(dict.keys()):
        print(' ', name, end = '')
    print(f"\n\nThe number of rows: {len(dict[list(dict.keys())[1]])}")
    print("\nSample row: ", end = '')
    for key in dict.keys():
        print(dict[key][0], end = ' ')
    
    print(dict['body_mass_g'])
    print(len(dict['body_mass_g']))
    pass

def cal_ave_mass(dict):
    # Average body mass for male penguins on Torgersen island
    total = 0
    count = 0
    for i in range(len(dict['body_mass_g'])):
        if (dict['body_mass_g'][i] != 'NA') and (dict['sex'][i] == 'male') and (dict['island'][i] == 'Torgersen'):
            total += int(dict['body_mass_g'][i])
            count += 1
    return total / count

def cal_length_diff(dict):
    # The diﬀerence between the average bill length for diﬀerence species on Dream island?
    num_chinstrap = 0
    total_len_chinstrap = 0
    total_len_adelie = 0
    num_adelie = 0
    for i in range(len(dict['island'])):
        if (dict['island'][i] == 'Dream') and (dict['bill_length_mm'][i] != 'NA'):
            if dict['species'][i] == 'Chinstrap':
                num_chinstrap += 1
                total_len_chinstrap += float(dict['bill_length_mm'][i])
            if dict['species'][i] == 'Adelie':
                num_adelie += 1
                total_len_adelie += float(dict['bill_length_mm'][i])
    ave_len_chinstrap = total_len_chinstrap / num_chinstrap
    ave_len_adelie = total_len_adelie / num_adelie
    diff = ave_len_chinstrap - ave_len_adelie
    return diff

def generate_report(dict):
    f = open("output.txt", "w")
    ave_mass = cal_ave_mass(dict)
    f.write(f"Average body mass for male penguins on Torgersen island is {ave_mass:.2f} grams.\n")
    diff = cal_length_diff(dict)
    f.write(f"The diﬀerence between the average bill length for Chinstrap and Adelie on Dream island is {diff:.2f} mm.\n")
    f.close()

def main():
    dict = load_file("penguins.csv")
    file_information(dict)
    generate_report(dict)
main()