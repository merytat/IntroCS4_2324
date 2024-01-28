#read input
text = input("Enter a word: ")

#calculate the middle
middle = len(text)//2

#print the letters before, middle and after
print(text[middle-1:middle+2])