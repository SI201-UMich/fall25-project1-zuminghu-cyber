# =========================================================
# SI 201: Project 1 – Data Analysis
# Name: Zuming Hu
# Student ID: 32862457
# Email: zuminghu@umich.edu
# Collaborators: Used GenAI to debug
# =========================================================

def read_file(filename):
    try:
        f = open(filename, 'r')
        return f
    except FileNotFoundError:
        print(f"read file failed")
        return None

def file_information(file):
    # file information
    first_row = file.readline()
    
    pass

def main():
    file = read_file("penguins.csv")
    file_information(file)
main()