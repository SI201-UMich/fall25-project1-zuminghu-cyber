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
        return dict
    except FileNotFoundError:
        print(f"read file failed")
        return None

def file_information(file):
    # file information
    #first_row = file.readline()

    pass

def main():
    file = load_file("penguins.csv")
    file_information(file)
main()