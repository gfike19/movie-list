fileList = open("yuge-list.txt", "r+")
print("File opened. . .")

lst = []
for line in fileList:
    lst.append(line)
fileList.close()
print("File close. Contents of file loaded onto list. . .")

lst.sort()
print("List has been sorted . . .")
zeroWhite = []

for line in lst:
        if line != "\n":
                tempWord = ""
                for char in line:
                        if(not char.isspace()):
                                tempWord += char
                zeroWhite.append(tempWord)

print("Whitespace has been removed. . .")

i = 0
zeroDup = []
while i + 1 < len(zeroWhite):
        word1 = zeroWhite[i]
        word2 = zeroWhite[i + 1]
        if word1 != word2 and word2 not in word1 and word2 is not word1:
                zeroDup.append(zeroWhite[i])
        i += 1

print("Duplicates have been removed. . . ")

# finalList = []
# for line in zeroDup:
#         for char in line:
#                 if char.isupper() and line.find(char) != 0:
#                         pos = line.find(char)
#                         first = line[:pos]
#                         first += (" " + line[pos:])
#                         finalList.append(first)

for each in zeroDup:
        print(each)