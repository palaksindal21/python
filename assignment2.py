# 1. Write a program to count word frequencies in a given text

# text = input("Enter a sentence or paragraph: ")

# punctuations = "!()-[]{};:'\"\\,<>./?@#$%^&*_~"
# clean_text = ""
# for char in text:
#     if char not in punctuations:
#         clean_text = clean_text + char
# clean_text = clean_text.lower()

# words = clean_text.split()


# word_counts = {}
# for word in words:
#     if word in word_counts:
#         word_counts[word] = word_counts[word] + 1
#     else:
#         word_counts[word] = 1
        

# print("\nWord Frequencies:")
# for word in word_counts:
#     print(word, ":", word_counts[word])

# 2.Palindrome Checker
# Write a program that checks if a given word is a palindrome.
num = int(input("Enter number:")) #taking input from user
temp = num
sum = 0

while num>0:
    num1 = num % 10
    sum = (sum*10) + num1
    num = num//10
if temp == sum:
    print("Given number is a pallindrom.")
else:
    print("Given number is not a pallindrome.")

#Create a list of numbers, then write a program that prints the square of each number in the list.
list=[1,2,3,4,5,6,7,8,9,10]
print(list)
for i in list:
    square = i**2
    print("Square of",i,"is",square,".")




