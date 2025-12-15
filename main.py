#!/usr/bin/env python3
import os
import argparse
import sys

ascii_art = r"""
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿⣿⢿⡶⠆⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⡿⠻⠋⣠⠀⢀⣶⠇⢠⣾⡿⠁⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⢀⣼⠟⠋⠻⢁⣴⠀⣾⣿⠀⠾⠟⠀⠈⣉⣠⣦⡤⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠸⠃⣠⡆⠀⣿⡟⠀⠛⠃⠀⠀⣶⣶⣦⣄⠉⢁⡄⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⣰⡀⢰⣿⠇⠀⢉⣀⣀⠛⠿⠿⠦⠀⢀⣠⣤⣴⣾⡇⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⣿⠃⠀⠠⣴⣦⡈⠙⠛⠓⠀⢰⣶⣶⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀
                    ⠀⠀⢀⣤⠦⡀⠰⢷⣦⠈⠉⠉⠀⣰⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀
                    ⠀⠀⠈⠁⠀⠘⣶⣤⣄⣀⣨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠃⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣯⡈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⣿⣿⣷⣤⣈⡉⠛⠛⠛⠛⠻⠟⠛⠛⠛⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
   _____                              _____            _               
  / ____|                            / ____|          | |              
 | |     __ _  ___  ___  __ _ _ __  | |    _   _ _ __ | |__   ___ _ __ 
 | |    / _` |/ _ \/ __|/ _` | '__| | |   | | | | '_ \| '_ \ / _ \ '__|
 | |___| (_| |  __/\__ \ (_| | |    | |___| |_| | |_) | | | |  __/ |   
  \_____\__,_|\___||___/\__,_|_|     \_____\__, | .__/|_| |_|\___|_|   
                                            __/ | |                    
                                           |___/|_|                    
"""
# ASCII art credits: https://emojicombos.com/caesar-ascii-art

englishABC = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
hungarianABC = [" ", "a", "á", "b", "c", "d", "e", "é", "f", "g", "h", "i", "í", "j", "k", "l", 
                "m", "n", "o", "ó", "ö", "ő", "p", "r", "s", "t", "u", "ú", "ü", "ű", "v", "z"]


def terminalClear():
    os.system("clear" if os.name != "nt" else "cls")


def getABC(language_code):
    if language_code.lower() in ["en", "english", "1"]:
        return englishABC
    elif language_code.lower() in ["hu", "hungarian", "2"]:
        return hungarianABC
    else:
        print(f"Error: Unknown language '{language_code}'. Use 'en' or 'hu'")
        sys.exit(1)


def encode(message, key, alphabet):
    encoded = ""
    for char in message:
        char_lower = char.lower()
        if char_lower in alphabet:
            index = alphabet.index(char_lower)
            encoded += alphabet[(index + key) % len(alphabet)]
        else:
            encoded += char
    return encoded


def decode(message, key, alphabet):
    decoded = ""
    for char in message:
        char_lower = char.lower()
        if char_lower in alphabet:
            index = alphabet.index(char_lower)
            decoded += alphabet[(index - key) % len(alphabet)]
        else:
            decoded += char
    return decoded


def decodeAllKeys(message, alphabet):
    print(f"\n{'Shift Key':<10} | {'Decoded string'}")
    print("-" * 50)
    for key in range(1, len(alphabet)):
        decoded = decode(message, key, alphabet)
        print(f"{key:^10} | {decoded}")


def runArguments(args):
    if args.encode:
        if not args.key:
            print("Error: Provide the shift key! Use -k or --key")
            sys.exit(1)
        if not args.abc:
            print("Error: Provide the alphabet language! Use -a or --abc")
            sys.exit(1)
        
        alphabet = getABC(args.abc)
        encoded_message = encode(args.encode, args.key, alphabet)
        print(f"Encoded string: {encoded_message}")
    elif args.decode:
        if not args.abc:
            print("Error: Provide the alphabet language! Use -a or --abc")
            sys.exit(1)
        
        alphabet = getABC(args.abc)
        
        if args.key:
            decoded_message = decode(args.decode, args.key, alphabet)
            print(f"\nDecoded string: {decoded_message}")
        else:
            decodeAllKeys(args.decode, alphabet)
    
    else:
        print("Error: Provide either -e/--encode or -d/--decode")
        sys.exit(1)


def runInteractive():
    while True:
        terminalClear()
        print(ascii_art)
        
        action = input("Encode(1)/Decode(2)/Quit(3)\n\n//:")
        
        if action == "3":
            print("Goodbye!")
            break
        
        if action not in ["1", "2"]:
            print("Choose from the options!")
            input("\nPress enter to continue")
            continue
        
        lang_choice = input("\nChoose your ABC language\n\nEnglish(1)/Hungarian(2): ")
        if lang_choice == "1":
            alphabet = englishABC
        elif lang_choice == "2":
            alphabet = hungarianABC
        else:
            print("Invalid choice!")
            input("\nPress enter to continue")
            continue
        
        if action == "1":
            key = int(input("\nShift key: "))
            user_input = input("\nEncode: ")
            
            encoded_string = encode(user_input, key, alphabet)
            print(f"\nEncoded string: {encoded_string}")
            input("\nPress enter to continue")
        
        elif action == "2":
            decode_input = input("\nDecode: ")
            is_shift_known = input("\nDo you know the shift key? Y/n: ")
            
            if is_shift_known.lower() == "y":
                caesar_shift = int(input("\nShift key: "))
                decoded_string = decode(decode_input, caesar_shift, alphabet)
                print(f"\nDecoded string: {decoded_string}")
            else:
                decodeAllKeys(decode_input, alphabet)
            
            input("\nPress enter to continue")


def main():
    parser = argparse.ArgumentParser(
        description="Caesar Cipher - Encode and decode messages",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Encode:  %(prog)s -e "hello world" -k 5 -a en
  Decode:  %(prog)s -d "mjqqt btwqi" -k 5 -a en
  Decode:  %(prog)s -d "mjqqt btwqi" -a en  (tries all keys)
        """
    )
    parser.add_argument("-e", "--encode", type=str, help="Message to encode")
    parser.add_argument("-d", "--decode", type=str, help="Message to decode")
    parser.add_argument("-k", "--key", type=int, help="Shift key (required for encoding)")
    parser.add_argument("-a", "--abc", type=str, help="Alphabet language: 'en' for English, 'hu' for Hungarian")
    
    args = parser.parse_args()
    
    if any([args.encode, args.decode, args.key, args.abc]):
        runArguments(args)
    else:
        runInteractive()


if __name__ == "__main__":
    main()
