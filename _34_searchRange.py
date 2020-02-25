class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums :return [-1,-1]
        if len(nums)==1 and nums[0]==target:return [0,0]
        a=-1
        b=-1
        start0=0
        end0=len(nums)-1
        if target<nums[start0] or target>nums[end0]:return [-1,-1]
        while end0-start0+1>=2:
            if nums[start0]==target:
                a=start0
                start0=end0
            else:
                if nums[(start0+end0+1)//2]==target and nums[(start0+end0+1)//2-1]<target:
                    a=(start0+end0+1)//2
                    start0=end0
                else:
                    if nums[(start0+end0+1)//2-1]>=target:
                        end0=(start0+end0+1)//2-1
                    else:
                        start0=(start0+end0+1)//2
        start0=0
        end0=len(nums)-1
        while end0-start0+1>=2:
            print(start0,end0)
            if nums[end0]==target:
                b=end0
                start0=end0
            else:
                if nums[(start0+end0-1)//2]==target and nums[(start0+end0-1)//2+1]>target:
                    b=(start0+end0-1)//2
                    start0=end0
                else:
                    if nums[(start0+end0-1)//2+1]<=target:
                        start0=(start0+end0-1)//2+1
                    else:
                        end0=(start0+end0-1)//2
        return [a,b]