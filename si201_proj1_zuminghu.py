# =========================================================
# SI 201: Project 1 – Data Analysis
# Name: Zuming Hu
# Student ID: 32862457
# Email: zuminghu@umich.edu
# Collaborators: Used GenAI to debug and ask AI how to let the test file to use the file dicionary it is located.
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

    pass

def cal_ave_mass(data):
    total = 0.0
    count = 0
    n = len(data['body_mass_g'])
    for i in range(n):
        mass = data['body_mass_g'][i]
        if (
            mass != -1 and
            data['sex'][i] == 'male' and
            data['island'][i] == 'Torgersen'
        ):
            total += float(mass)
            count += 1
    return total / count if count else 0.0


def cal_length_diff(data, sp_a='Chinstrap', sp_b='Adelie'):
    total_a = total_b = 0.0
    num_a = num_b = 0

    n = len(data['bill_length_mm'])
    for i in range(n):
        if data['island'][i] != 'Dream':
            continue
        bl = data['bill_length_mm'][i]
        if bl == -1:
            continue
        species = data['species'][i]
        if species == sp_a:
            total_a += float(bl)
            num_a += 1
        elif species == sp_b:
            total_b += float(bl)
            num_b += 1

    if num_a == 0 or num_b == 0:
        return 0.0

    ave_a = total_a / num_a
    ave_b = total_b / num_b
    return ave_a - ave_b

def generate_report(dict):
    f = open("output.txt", "w")
    ave_mass = cal_ave_mass(dict)
    f.write(f"Average body mass for male penguins on Torgersen island is {ave_mass:.2f} grams.\n")
    diff = cal_length_diff(dict)
    f.write(f"The diﬀerence between the average bill length for Chinstrap and Adelie on Dream island is {diff:.2f} mm.\n")
    f.close()

def main():
    dict = load_file("penguins.csv")
    # file_information(dict)
    generate_report(dict)
main()