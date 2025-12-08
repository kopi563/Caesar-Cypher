#catch mistypes
#proper bruteforce
#make interface cleaner simpler
#do something better with space and uppercase letters
#on terminal use with arguemnts
#import all languages
import os

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
#ascii art credits: https://emojicombos.com/caesar-ascii-art

def terminalClear():
    os.system("clear")
    
encodedString = ""

global englishABC
englishABC = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
                
global hungarianABC
hungarianABC = [" ", "a", "á", "b", "c", "d", "e", "é", "f", "g", "h", "i", "í", "j", "k", "l", 
                "m", "n", "o", "ó", "ö", "ő", "p", "r", "s", "t", "u", "ú", "ü", "ű", "v", "z",]


while True:
    terminalClear()

    print(ascii_art)

    action = int(input("Encode(1)/Decode(2)/Quit(3)\n\n//:"))

    def abcLanguage():
        global chosenABC
        chosenABC = int(input("\nChoose your ABC language\n\nEnglish(1)/Hungarian(2) "))
        if chosenABC == 1:
            chosenABC = englishABC
        elif chosenABC == 2:
            chosenABC = hungarianABC
                
    if action == 1:
        abcLanguage()
        key = int(input("\nShift key: "))
        userInput = str(input("\nEncode: "))
        
        for i in userInput:
            i = i.lower()
            index = chosenABC.index(i)
            encodedString += chosenABC[(index+key) % len(chosenABC)]
        print(f"\nEncoded string: {encodedString}")
        input("\nPress enter to continue")
        encodedString = ""
    elif action == 2:
        abcLanguage()
        def decoding(string, isKeyKnown=None):
            decodeResult = ""
            if isKeyKnown == None:
                print("\nShift Key | Decoded string")
                print("-" * 40)
                for i in range(len(chosenABC)):
                    for j in string:
                        j = j.lower()
                        index = chosenABC.index(j)
                        decodeResult += chosenABC[(index - i) % len(chosenABC)]
                        print(f"{i:9} | {decodeResult}")
                input("\nPress enter to contiue")
            else:
                decodeResult = ""
                for i in string:
                    i = i.lower()
                    index = chosenABC.index(i)
                    decodeResult += chosenABC[index-isKeyKnown]
            print(f"\nDecoded string: {decodeResult}")
            input("\nPress enter to continue")
        def prompting(previous=None):
            if previous == None:
                decodingString = str(input("\nDecode: "))
            else:
                decodingString = encodedString
            isShiftKnown = str(input("\nDo you know the shift key? Y/n "))
            if isShiftKnown == "Y" or isShiftKnown == "y":
                caesarShift = int(input("\nShift key: "))
                decoding(decodingString, caesarShift)
            elif isShiftKnown == "N" or isShiftKnown == "n":
                decoding(decodingString)    
        prompting()     
        encodedString = ""       
    elif action == 3:
        print("Goodbye!")
        break;
    else:
        print("Choose from the options!")
