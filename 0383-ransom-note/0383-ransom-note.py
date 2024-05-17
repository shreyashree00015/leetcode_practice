class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_dic = {}
        m_dic = {}
        for i in range(len(ransomNote)):
            if ransomNote[i] in r_dic.keys():
                r_dic[ransomNote[i]] +=1
            else:
                r_dic[ransomNote[i]] = 1

        for i in range(len(magazine)):
            if magazine[i] in m_dic.keys():
                m_dic[magazine[i]] +=1
            else:
                m_dic[magazine[i]] = 1

        for keys in r_dic.keys():
            if keys in m_dic:
                if r_dic[keys] > m_dic[keys]:
                    return False
            else:
                return False
        return True
