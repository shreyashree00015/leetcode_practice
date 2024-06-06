from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to map sorted tuple of characters to list of anagrams
        anagrams = defaultdict(list)
        
        for s in strs:
            # Sort the string and use it as a key
            key = tuple(sorted(s))
            anagrams[key].append(s)
        
        # Return the values of the dictionary which are the grouped anagrams
        return list(anagrams.values())