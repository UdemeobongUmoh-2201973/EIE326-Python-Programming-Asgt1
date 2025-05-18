"Casear cipher."

default_alpha_list = "abcdefghijklmnopqrstuvwxyz"

def caesar_cipher_char(character: str, incr: int):
    """
    Checks if an alphanumeric character.
    If yes, it applies the shift function to it.
    If no, it just returns the character on its own.
    """
    
    if character.isalpha():
        old_index = default_alpha_list.index(character.lower())

        new_index = old_index + incr

        while new_index >= 26:
            new_index -= 26
        while new_index <= -1:
            new_index += 26

        if character.isupper():
            return default_alpha_list[new_index].upper()
        else:    
            return default_alpha_list[new_index]
        
    return character
    

def return_caesar_cipher(text: str, incr: int):
    "Runs this Caesar cipher code for all the characters in string."
    
    new_text = str()

    for char in text:
        new_text += caesar_cipher_char(char, incr)

    return new_text



input_text = input("Input your text here: ")
incr = int(input("Input your increment no.(an integer between -26 and 26): "))

print(f"\nCiphered Text: {return_caesar_cipher(input_text, incr)}")

run_again = input("Do you wish to run again:(Y or N): ")


# Loop that runs until user input says no.

while run_again.lower() != "n":
    input_text = input("\nInput your text here: ")
    incr = int(input("Input your increment no.(an integer between -26 and 26): "))

    print(f"\nCiphered Text: {return_caesar_cipher(input_text, incr)}")

    run_again = input("Do you wish to run again:(Y or N): ")

quit()