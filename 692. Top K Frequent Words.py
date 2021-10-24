# https://leetcode.com/problems/top-k-frequent-words/submissions/
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        words.sort()
        
        c = collections.Counter(words).most_common(k)
        
        return [i[0] for i in c]
