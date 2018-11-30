import sys
import base64
filename = sys.argv[1]

fd = open(filename, 'r')

lines = fd.readlines()

ciphertext = ""

for line in lines:
    ciphertext = ciphertext + line.strip()

fd.close()
fd2 = open("must2.cry", 'w')
for b in base64.b64decode(ciphertext):
    h = hex(ord(b))[2:]
    if len(h) == 1:
        h = "0" + h
    fd2.write(h)

fd2.close()
print("Done decrypting!")
