class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # It would be useful to have a map that for each letters tells me the
        # freq of them. 
        # We can just sort them and check if the list are equals.
        freq1= {}
        if len(s) != len(t):
            return False
        for letter in s:
            if letter in freq1.keys():
                freq1[letter]+=1
            else:
                freq1[letter]=1
        for letter in t:
            if letter in freq1.keys() and freq1[letter]!=0:
                freq1[letter]-=1
            else:
                return False
        return True

        

        