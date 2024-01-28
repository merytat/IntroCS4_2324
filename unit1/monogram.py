#asking for input for the full name
name = input("Enter full name: ")

#extract first letter of full name [0]
first = name[0]

#convert to capital case and print
print(first.upper())

#create a var that holds the index of space
index = name.find(" ")

#create a new text that starts at space until the end
middleUp = name[index+1:]

#create a var that holds the second space
index2 = middleUp.find(" ")

#create a var that holds the middle name
middleName = middleUp[0:index2-1]

#extract the middle character

#print in capital letter

#variable that holds the length of full name

#extract the letter at lenght -1

#print as capital