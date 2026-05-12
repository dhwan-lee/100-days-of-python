import caeser_cipher_art
print(caeser_cipher_art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True

def caeser(chosen_direction, original_text, shift_amount): 
    output_text = ""
    if chosen_direction == "decode":
            shift_amount *= -1
        
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            i = alphabet.index(letter)
            # one way to do this wihtout modulo
            # if chosen_direction == "encode":
            #     i = i + shift_amount
            # else:
            #     i = i - shift_amount
            
            # the other way
            i = i + shift_amount
            i %= len(alphabet)
            output_text += alphabet[i]

    print(f"Here is the {chosen_direction}d result: {output_text}")

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(direction, text, shift)
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n").lower()
    if restart == "no":
        should_continue = False
        print("Good Bye!")