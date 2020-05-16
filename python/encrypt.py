def encrypt(txt, encode=True, rotation=21):
    """
    by Daniel Bezerra dos Santos... dbsantos1981@gmail.com

    This function implements a simple version of "Caesar's Cryptography"

    :param txt: text to be encrypted or decrypted
    :param encode: if encode is true, it will encrypt. Otherwise it will decrypt
    :param rotation: how many characters will be used in encryption
    :return: the input text encrypted or decrypted, depending on your choice

    Usage examples:

    original = "Daniel is cool"
    encrypted = encrypt(original)
    decrypted = encrypt(encrypted, encode=False)

    Seeing the results:

    print(original)     Daniel is cool
    print(encrypted)    YvIDzGpDNpxJJG
    print(decrypted)    Daniel is cool
    """

    # imports
    import string

    # definitions
    everything = string.ascii_letters + string.punctuation + string.digits + string.whitespace
    result = ''

    # encode or decode ?
    if encode == False:
        rotation = rotation * -1

    # encoding loop
    for char in txt:
        if char in everything:
            # known char
            position = everything.find(char)
            position = (position + rotation) % 100     # 100 is the sum of all char
            result = result + everything[position]
        else:
            # unknown char
            result = result + char

    # returns the result
    return result
