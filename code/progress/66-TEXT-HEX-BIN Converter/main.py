# author : gamingdy

import sys


class Converter:
    def text_to_hex(user_string):
        return user_string.encode("utf-8").hex()

    def text_to_bin(user_string):
        bin_text = ""
        for char in user_string:
            bin_number = bin(ord(char))[2:]
            if len(bin_number) < 8:
                bin_number = "0" * (8 - len(bin_number)) + bin_number

            bin_text += bin_number + " "
        return bin_text

    def hex_to_text(user_string):
        return bytes.fromhex(user_string).decode("utf-8")

    def hex_to_bin(user_string):
        return Converter.text_to_bin(Converter.hex_to_text(user_string))

    def bin_to_text(user_string):
        user_string = user_string.replace(" ", "")
        final_string = ""
        for i in range(0, len(user_string), 8):
            result = user_string[i : i + 8]
            final_string += chr(int(result, 2))
        return final_string

    def bin_to_hex(user_string):
        pass


all_option = {
    "1": ("Convert text to hex", Converter.text_to_hex),
    "2": ("Convert text to bin", Converter.text_to_bin),
    "3": ("Convert hex to text", Converter.hex_to_text),
    "4": ("Convert hex to bin", Converter.hex_to_bin),
    "5": ("Convert bin to text", Converter.bin_to_text),
    "6": ("Convert bin to hex", Converter.bin_to_text),
    "0": ("Exit",),
}


def print_option():
    sep = 1
    for i in all_option:
        print(f"[{i}] : {all_option[i][0]}")
        sep += 1
        if sep > 2:
            print("-" * 20)
            sep = 1
    print()


while True:
    print_option()
    user_choice = input("Choose an option: ")
    if user_choice in all_option:
        if user_choice == "0":
            sys.exit()
        user_string = input(f"String to {all_option[user_choice][0].lower()}: ")
        result = all_option[user_choice][1](user_string)
        print("This is your result:", result)
