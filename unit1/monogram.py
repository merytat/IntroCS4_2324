#read full name as an input
name = input("Write your Full Name: ")
#create a new variable with a substring for index [0]
first_letter = name[0]
#convert to capital letter and print the first letter
print(first_letter.upper())
#create a new variable that holds the index of the first space
indexSpace = name.find(" ")
#create a new text that starts at space+1 and goes until the end
middleup = name[indexSpace+1:]  #johanna tellez
#create a var that finn the space on the new text
indexspace2 = middleup.find(" ")  #7
#create a var that holds the middle name (sub string from 0, space)
middle_name = middleup[0:indexspace2]  #johanna
#create a var that holds the index of the middle of the lenght of middle name
middle_letter = len(middle_name) // 2  #3
#convert to capital and print the middle letter at that index
print(middle_name[middle_letter].upper()) # a
#create a var and calculate the lenght of full name
length = len(name)  #19
#convert to upper and print the letter at position len-1
print(name[length -1].upper())