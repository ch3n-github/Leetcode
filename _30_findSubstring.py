class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:return []
        l0=len(words[0])
        l=l0*len(words)
        if not s or len(s)<l:return []
        words.sort()
        res=[]
        for i in range(len(s)-l+1):
            ex=[]
            for j in range(len(words)):
                ex.append(s[i+j*l0:i+(j+1)*l0])
            ex.sort()

            if ex==words:
                res.append(i)
        return res