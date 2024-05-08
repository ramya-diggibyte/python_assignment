def merge_the_tools(s, k):
    merged_string = []
    for i in range(len(s) // k ):
        empty_list = []
        print(empty_list)
        for j in range(k):
            charac_at_position = s[i*k+j]
            print(charac_at_position)
            if charac_at_position not in empty_list:
                empty_list.append(charac_at_position)
                print((empty_list))
        merged_string.append("".join(empty_list))
    return merged_string
