# https://leetcode.com/problems/license-key-formatting/
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = list(s.upper().replace("-", ""))[::-1]
        l = len(s)
        for x, y in zip(range(k, l, k), range(l//k)):
            s.insert((x+y), "-")
        return "".join(s[::-1])
