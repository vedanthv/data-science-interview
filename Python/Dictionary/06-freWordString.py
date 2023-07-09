test_string=raw_input("Enter string:")
l=[]
l=test_string.split()

wordFreq = [l.count(p) for p in l]
print(dict(zip(l,wordfreq)))