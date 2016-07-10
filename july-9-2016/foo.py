def at_end_of_list(i, list_element):
    return i >= len(list_element) - 1


def is_list(element):
    return isinstance(element, list)


def p_flat(input_list, output_list=[], i=0):

    if is_list(input_list[i]):
        p_flat(input_list[i], output_list)
    else:
        output_list.append(input_list[i])

    if not at_end_of_list(i, input_list):
        p_flat(input_list, output_list, i+1)

    return output_list


# some test cases
#_input= ['a', ['b', ['c', 'd'], 'e']]
#_input= ['a','b', ['c'], 'e']
_input = ['p', 'y', ['t', ['h', ['o']], 'n']]

print p_flat(_input)
