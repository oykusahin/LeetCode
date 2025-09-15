class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split(' ')
        count=0
        for t in text:
            isBroken = False
            for b in list(brokenLetters):
                print('Broken letter: ',b)
                if b in t:
                    isBroken = True
            if isBroken is False:
                count+=1
        return count