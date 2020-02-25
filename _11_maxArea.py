class Solution:
	#双指针
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        maxa=min(height[0],height[-1])*(l-1)
        start=0
        end=0
        while(start+end+2<l):
            if height[start]>height[-end-1]:
                end0=end+1
                while(height[-end0-1]<height[-end-1] and start+end0+2<l):
                    end0+=1
                end=end0
                maxa=max(maxa,min(height[start],height[-end-1])*(l-start-end-1))
            else:
                start0=start+1
                while(height[start0]<height[start] and start0+end+2<l):
                    start0+=1
                start=start0
                maxa=max(maxa,min(height[start],height[-end-1])*(l-start-end-1))
        return maxa