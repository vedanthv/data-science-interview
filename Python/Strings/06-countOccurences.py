string = raw_input("Enter string")
word = raw_input("Enter Word: ")

a = []
count = 0
a = string.split(" ")

for i in range(0,len(a)):
    if(word==a[i]):
        count=count+1
print("Count of the word is:")
print(count)