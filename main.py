morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

def convert_to_morse(word):
    morse_code = ""
    for char in word.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + " "
        else:
            morse_code += " "
    return morse_code

word = input("Please enter a word to convert into Morse Code: ")

morse_code = convert_to_morse(word)

if morse_code == " ":
    print("There were no characters to convert into Morse Code")
else:
    print(f"Your word's Morse Code is: {morse_code}")




