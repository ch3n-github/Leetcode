class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:return None
        l=len(nums)
        start=0
        while start<l:
            if nums[start]==val:
                l-=1
                nums[start:l]=nums[start+1:l+1]
            else:
                start+=1
        return l