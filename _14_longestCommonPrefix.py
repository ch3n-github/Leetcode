class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:return ''
        l=0
        for i in zip(*strs):
            if len(set(i))==1:
                l+=1
            else:
                break
        return strs[0][:l]