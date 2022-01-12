def get_key(message, key):
    key = list(key)
    if len(message) == len(key):
        return(key)
    else:
        for i in range(len(message) -len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def encrypted(message, key):
    encrypted_text = []
    for i in range(len(message)):
        x = (ord(message[i]) + ord(key[i])) % 26
        x += ord('A')
        encrypted_text.append(chr(x))
    """
    res = " "
    res = res.join(encrypted_text)
    """
    return encrypted_text

def original(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))

if __name__ == "__main__":
    message = input("Message for Encryption: ")
    keyword = input("Enter Key: ")
    key = get_key(message, keyword)
    cipher_text = encrypted(message,key)
    res = " "
    print("Ciphertext :", res.join(cipher_text))
    print("Original :", original(cipher_text, key))
