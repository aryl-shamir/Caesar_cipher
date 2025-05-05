
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number: \n"))


def encode(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % len(alphabet)
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f'Here is your encoded result {cipher_text}')


def decode(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift_amount) % len(alphabet)
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f'Here is your decoded result {cipher_text}')
