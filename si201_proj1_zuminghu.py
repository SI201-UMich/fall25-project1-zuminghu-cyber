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
        print(dict)

        col = 1
        for idx in dict.keys():
            for line in f:
                dict[idx].append(line.split(',')[col].strip('\n').strip('"'))
            col += 1
        print(dict)


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