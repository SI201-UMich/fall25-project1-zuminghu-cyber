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
        
    pass

def generate_report():
    f = open("output.txt", "w")
    f.write("Hello world")
    f.close()

def main():
    file = load_file("penguins.csv")
    file_information(file)
    generate_report()
main()