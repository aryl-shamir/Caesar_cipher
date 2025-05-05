from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def ceaser(original_text, shift_amount, encode_or_decode):
    cipher_text = ""
    if encode_or_decode == 'decode':
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % len(alphabet)
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f'Here is your encoded result {cipher_text}')


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number: \n"))

    ceaser(text, shift, direction)
    restart = input("Type 'yes' if you want to go again, otherwise type 'no'").lower()

    if restart == 'no':
        should_continue = False
        print('Good bye, see you next time.')


