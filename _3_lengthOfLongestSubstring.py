#Author：chen
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        #滑动窗口
        stringwindow = list()
        n=len(s)
        maxlen=0
        winlen=0
        for j in range(n):
            if s[j] not in stringwindow:
                stringwindow.append(s[j])
                winlen+=1
            else:
                ind=stringwindow.index(s[j])
                stringwindow=stringwindow[ind+1:]
                stringwindow.append(s[j])
                winlen=len(stringwindow)
            if winlen>maxlen:maxlen=winlen
        return maxlen