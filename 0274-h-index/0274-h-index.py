class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h_idx = len(citations)
        for i in range(len(citations)):
            if (citations[i]<h_idx):
                h_idx -= 1
        return h_idx