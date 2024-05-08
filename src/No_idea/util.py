def happiness_noidea(n, m, input_array, A, B):
    happiness = 0
    set_A = set(A)
    set_B = set(B)

    for num in input_array:
        if num in set_A:
            happiness += 1
        elif num in set_B:
            happiness -= 1

    return happiness