def decimal_to_binary(n):
    return bin(n).replace("0b", "")


def bitstring_to_bytes(s):
    # return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')
    return bytes(int(s[i:i + 8], 2) for i in range(0, len(s), 8))


def print_with_new_lines(message):
    print()
    print(message)
    print()
