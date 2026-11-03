def minimum_Chips(N : int) -> int :

    chip_set = [100, 50, 25, 10, 5, 1]

    chip_count = 0

    for chip in chip_set:
        chip_count +=  N // chip
        N %= chip

    return chip_count
        

print(minimum_Chips(126))
