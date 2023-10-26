def caesar(start_text, shift_number, encrypt_or_decrypt):
    end_text = ""
    if encrypt_or_decrypt == "decode":
        shift_number *= -1
    for letter in start_text:
        letter_value = ord(letter) + shift_number
        end_text += chr(letter_value)

    print(f"The final {encrypt_or_decrypt}d message is: {end_text}")

direction = input(f"Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type your message:\n").lower()
shift = int(input("Type your shift number\n"))

caesar(start_text=message, encrypt_or_decrypt=direction, shift_number=shift)
