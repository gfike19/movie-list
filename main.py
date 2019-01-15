fileList = open("yuge-list.txt", "r+")

lst = []
for line in fileList:
    lst.append(line)
fileList.close()
cleanList = []

idx = 0

while idx < len(lst) - 1:
    for line in lst:
        if "\n" not in line or lst[idx] not in lst[idx + 1]:
            cleanList.append(line)
    idx += 1

newFile = open("test.txt", "a+")

for each in cleanList:
    newFile.write(each)

newFile.close()