class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # The only invariant between anagrams is the freq_table of characters
        # We can use it as a key to store the words associated in a list.
        # freq_table -> list with strs
        # Finally for each freq_table we a have sublist.
        # We just return the values of that dictionary.
        hash_map = {}
        
        for word in strs:
            freq_table = {}
            for letter in word:
                if letter not in freq_table:
                    freq_table[letter]=0
                freq_table[letter]+=1
            
            key = frozenset(freq_table.items())
            if key not in hash_map:
                hash_map[key]=[]
            hash_map[key].append(word)

        return list(hash_map.values())



        