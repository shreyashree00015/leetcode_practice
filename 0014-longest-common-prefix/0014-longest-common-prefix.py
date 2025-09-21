class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        prefix = ''
        first_string = strs[0]
        for i in range(len(first_string)):
            current_char = first_string[i]
            for other_strings in strs:
                if i>=len(other_strings) or other_strings[i]!=current_char:
                    return prefix
            prefix += current_char
        return prefix