class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or haystack==needle:return 0
        if not haystack or len(needle)>len(haystack):return -1

        l=len(needle)
        for i in range(len(haystack)-l+1):
            if haystack[i:i+l]==needle:
                return i
        return -1