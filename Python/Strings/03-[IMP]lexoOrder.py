def lexicographicalOrder(chars,output=""):
    if len(output) == len(chars):
        print(output,end = '')
        return
    
    i = 0
    while i < len(chars):
        while i + 1 <len(chars) and chars[i] == chars[i+1]:
            i = i+1 
        lexicographicalOrder(chars,output+chars[i])
        i = i+1

def findlexicographic(s):
        if not s:
            return 
        chars = sorted(list(s))
        lexicographicalOrder(chars)