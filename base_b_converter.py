# Base-b to DEC convertor, suitable for Whole numbers only [0, infinity)     10-SEP-2022
def main():
    i, dec_value = 0, 0
    in_number, base = input("Enter the number: "), int(input("Enter base: "))
    num_length = len(in_number)
    if base == 16:
        while i <= num_length - 1:
            position = num_length - 1 - i
            if not in_number[i].isnumeric() and ord(in_number[i].upper()) < 71:
                hex_letter = ord(in_number[i].upper()) - 55
                dec_value += hex_letter * (base ** position)
            elif in_number[i].isnumeric(): dec_value += int(in_number[i]) * (base ** position)
            else: print("Invalid HEX number")
            i += 1
    else:
        while i <= num_length - 1:
            position = num_length - 1 - i
            dec_value += int(in_number[i]) * (base ** position)
            i += 1
    print("{} in base {} = {} in decimal.".format(in_number, base, dec_value))
    another_number = input("Another number (y/n)? ").lower()
    if another_number == 'y': main()
    else: pass


if __name__ == '__main__': main()
