def longestword(wordlist):
    wordlength=[]
    for n in wordlist:
        wordlength.append((len(n),n))
    wordlength.sort()
    return wordlength[-1][1]
    
    

longestword(['rajesh','acadgild','trainer'])