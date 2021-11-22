# the ciphertext
ct = '🍕🍔🍆🍌🍁🍇🍛🍂🍁🍓🍅🍄🌿🍅🍍🍏🍊🍉🍓🌿🍇🍏🌿🍚🍏🍏🍍🍝'

# get the diff value
diff = ord(ct[0]) - ord('u')

# reconstruct the plaintext
pt = []

for c in ct:
    char_value = ord(c) - diff
    pt.append(chr(char_value))

print(''.join(pt))
