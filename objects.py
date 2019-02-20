def make_set():

def make_variable():
    value = ''

    for char in input:
        if char == ' ' and value != '':
            break

        if char == '\n':
            break

        if char == ',':
            if value == '':
                print('ERROR: Line ended while interpreting a variable!')
                # TODO: Raise error.
            else:
                break

        if char == '{':
            if value == '':
                make_set(input)
            else:
                print('ERROR: Attempting to define multiple variables on one line.')
                # TODO: Raise error.

        else:
            value += char
    
    return value