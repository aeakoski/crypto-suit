import sys
import base64
filename = sys.argv[1]

fd = open(filename, 'r')

lines = fd.readlines()

alphabet = {}
nr_of_chars = 0.0
chiphertext = ""

for line in lines:
    chiphertext = chiphertext + line.strip()
    for i in range(1, len(line), 2):
        nr_of_chars += 1
        char = line[i-1] + line[i]
        try:
            alphabet[char]
            alphabet[char] += 1
        except KeyError:
            alphabet[char] = 1

freqlist = []
sum_fi = 0.0
print("Char\tOcc\tFreq %")
for key in alphabet.keys():
    sum_fi += alphabet[key] * (alphabet[key]-1)
    freqlist.append((key, round(alphabet[key] / nr_of_chars, 3)))
    # print(key + "\t" + str(ord(key)) + "\t" + str(alphabet[key]) + "\t" + str(round(alphabet[key] / nr_of_chars, 3)))
freqlist.sort(key =lambda x : x[1]) # Sort on frequency
freqlist.reverse()
for char in freqlist:
    key = char[0]
    print(key + "\t" + str(alphabet[key]) + "\t" + str(char[1]))
print("Number of chars: " + str(int(nr_of_chars)))
print("Number in alphabet: " + str(len(freqlist)))
print("Index of coincidence:" + str(round(sum_fi / ( nr_of_chars * ( nr_of_chars - 1 ) ), 4 ) ) )

print("")
fd.close()
