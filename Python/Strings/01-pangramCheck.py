def checkPangram(s):
    List = []
    # create list of 26 characters and set false each entry
    for i in range(26):
        List.append(False)
 
    # converting the sentence to lowercase and iterating
    # over the sentence
    for c in s.lower():
        if not c == " ":
 
            # make the corresponding entry True
            List[ord(c) - ord('a')] = True
 
    # check if any character is missing then return False
    for ch in List:
        if ch == False:
            return False
    return True
 