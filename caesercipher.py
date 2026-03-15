alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encode(plain_text,shift_key):
    cipher_text = ""    #empty string which will store the encoded text
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char) #position variable will store index number of alphabet
            new_position = (position+shift_key)%26  # new_position variable store the index of alphabet after shifting 
            cipher_text += alphabet[new_position]    # after shifting letters encoded letters are stored in cipher_text
        else:  #else condition for symbols and numbers
            cipher_text += char
    print(f"Here's the text after encoding: {cipher_text}")

def decode(cipher_text,shift_key):
    plain_text = ""  #empty string which will store the decoded text
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)  #position variable will store index number of alphabet
            new_position = (position-shift_key)%26 # new_position variable store the index of alphabet after shifting 
            plain_text += alphabet[new_position]   # after shifting letters decoded letters are stored in plain_text
        else:
            plain_text += char #else condition for symbols and numbers
    print(f"Here's the text after decoding: {plain_text}")

end = False
while not end:   #while loop is used for continuous generation of code
    what_to_do = input("type 'encode' for encoding , type 'decode' for decoding:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Enter shift key:\n"))
    if what_to_do == "encode":
        encode(plain_text=text,shift_key=shift)
    elif what_to_do == "decode":
        decode(cipher_text=text,shift_key=shift)
    generate_again = input("Type 'yes' to continue, type 'no' to exit.\n")
    if generate_again == 'no':
        end = True
        print("Have a nice day! Bye..")
