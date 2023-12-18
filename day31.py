#Write a program to count the number of words in a text file.
print ("\nWilson - Day 31 of #100DaysOfCode\n") 
print("\ncount the number of words in a text file\n")

file_path = 'sample.txt'
file = open(file_path,'r')
content = file.read()
words = content.split()
num_words = len(words)
print("The number of words in the file is: ", num_words)

#Write a program to copy the contents of one text file to another.
print("\ncopy the contents of one text file to another.")

first_file = 'one.txt'
second_file = 'two.txt'
file1 = open(first_file,'r')
file1content = file1.read()
file2 = open(second_file,'w')
file2 = write(file1)


