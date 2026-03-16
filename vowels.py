# counting vowels in string

word = input("Enter a word:")
count = 0

for char in word:
    if char in "aeiouAEIOU":
        count = count+1

print("number of vowels:",count)

    
        