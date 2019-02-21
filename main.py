import sys
from objects import test_levels

def initialize_program():
    """Reads the input and handles basic errors like
    - When a file name isn't provided;
    - When the provided file name cannot be found;
    """
    args = sys.argv[1:]
    print(args)
    if len(args) == 0:
        print('ERROR: No file provided! Please provide us with a file!')
        # TODO: Write program info instead of giving an error.
    
    else:
        data_strip = read_file(args[0])
        print(data_strip)
        print(test_levels(data_strip))
    
def read_file(file_name):
    """Reads through the file and asks to interpret the file."""
    long_string = []

    comment = False
    lin = 0

    try:
        for line in open(file_name):
            lin += 1
            col = 0
            for char in line:
                col += 1
                if comment or char == '$':
                    comment = True
                    if char == '\n':
                        comment = False
                
                elif char not in [' ','\n','\t']:
                    long_string.append((char,lin,col))
    except FileNotFoundError:
        print('Oh no! This file doesn\'t exist! Or, I cannot find it, at least.')
        # TODO: Write program that handles non-existent files.
    
    return long_string

if __name__ == "__main__":
    initialize_program()