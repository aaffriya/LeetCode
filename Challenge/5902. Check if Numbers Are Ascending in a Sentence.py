class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split()
        res = []
        for i in range(len(s)):
            try:
                c = int(s[i])
                res.append(c)
            except:
                continue
        for i in range(len(res)-1):
            if res[i] >= res[i+1]:
                return False
        else:
            return True
