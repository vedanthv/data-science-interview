test_string=raw_input("Enter string:")
l=test_string.split()
d={}

for word in l:
    if(word[0] not in l):
        if(word[0] not in dict.keys()):
            d[word[0]] = []
            d[word[0].append(word)]
        else:
            if word not in d[word[0]]:
                d[word[0]].append(word)
for k,v in d.items():
    print(k + ":" + v)
            