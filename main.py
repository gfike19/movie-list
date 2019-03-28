def removeWS(word):
    return word.replace(" ", "")

fileList = open("yuge-list.txt", "r+")

lst = []
for line in fileList:
    lst.append(line)
fileList.close()
cleanList = []

# idx = 0

# while idx < len(lst) - 1:
#     for line in lst:
#         if "\n" not in line.strip() or lst[idx].strip() not in lst[idx + 1].strip():
#             cleanList.append(line)
#     idx += 1

for each in lst:
    if each != "\n" or each != "\r":
        if removeWS(each) != removeWS(next(iter(lst))):
            cleanList.append(each)

cleanList.sort()

newFile = open("test.txt", "a+")

for each in cleanList:
    newFile.write(each)

newFile.close()