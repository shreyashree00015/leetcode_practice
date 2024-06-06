from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for s in strs:
            key = ''.join(sorted(s))  # Sort the string and join back to form the key
            anagrams[key].append(s)
        
        return list(anagrams.values())
