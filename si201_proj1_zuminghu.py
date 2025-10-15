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
            datas = line.rstrip('\n').split(',')
            dict['species'].append(to_str_or_minus1(datas[1]))
            dict['island'].append(to_str_or_minus1(datas[2]))
            dict['bill_length_mm'].append(to_num_or_minus1(datas[3], float))
            dict['bill_depth_mm'].append(to_num_or_minus1(datas[4], float))
            dict['flipper_length_mm'].append(to_num_or_minus1(datas[5], float))
            dict['body_mass_g'].append(to_num_or_minus1(datas[6], int))
            dict['sex'].append(to_str_or_minus1(datas[7]))
            dict['year'].append(to_num_or_minus1(datas[8], int))
        f.close()
        return dict
    except FileNotFoundError:
        print(f"read file failed")
        return None

def to_num_or_minus1(s, caster):
    v = s.strip().strip('"')
    if v == '' or v == 'NA':
        return -1
    try:
        return caster(v)
    except ValueError:
        return -1

def to_str_or_minus1(s):
    v = s.strip().strip('"')
    return '-1' if v == '' or v == 'NA' else v

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
        if (dict['body_mass_g'][i] != -1) and (dict['sex'][i] == 'male') and (dict['island'][i] == 'Torgersen'):
            total += dict['body_mass_g'][i]
            count += 1
    return total / count

def cal_length_diff(dict):
    # The diﬀerence between the average bill length for diﬀerence species on Dream island?
    num_chinstrap = 0
    total_len_chinstrap = 0
    total_len_adelie = 0
    num_adelie = 0
    for i in range(len(dict['island'])):
        if (dict['island'][i] == 'Dream') and (dict['bill_length_mm'][i] != -1):
            if dict['species'][i] == 'Chinstrap':
                num_chinstrap += 1
                total_len_chinstrap += dict['bill_length_mm'][i]
            if dict['species'][i] == 'Adelie':
                num_adelie += 1
                total_len_adelie += dict['bill_length_mm'][i]
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