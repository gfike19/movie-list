# def removeSpChar(word):
#     newWord = ""

#     for char in word:
#         if char.isalnum():
#             newWord = newWord + char
    
#     return newWord

# print("Getting all movies. . . ")
yuge_list = open("yuge-list.txt", "r+")

cleanList = []

#puts all movie titles from txt into a list
# TODO need to remove spaces and non alpha num but then put back spaces for readability
for line in yuge_list:
    if line != "\n":
        newLine = ""
        for char in line:
            if char.isalnum():
                

yuge_list.close()
cleanList.sort()

# print("Removing duplicates. . . .")

#doesn't work

# for i in range(len(cleanList) - 1):
#     movie1 = cleanList[i]
#     movie2 = cleanList[i + 1]

#     if movie1.find(movie2) ==  True:
#         cleanList.remove(movie2)

# does work

# print("Creating new file. . . ")
# try:
#     new_yuge_list = open("new_yuge_list.txt", "w+")
# except Exception as e:
#     str_exc = str(e)
#     print(str_exc)

# print("Writing to new file. . .")
# for each in cleanList:
#     new_yuge_list.write(each)

# print("Process completed")


