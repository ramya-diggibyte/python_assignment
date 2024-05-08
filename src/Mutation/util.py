def mutate_string(string, position, character):
    string_to_list = list(string)
    string_to_list[position] = character
    mutate = ''.join(string_to_list)
    return mutate