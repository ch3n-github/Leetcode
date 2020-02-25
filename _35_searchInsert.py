class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:return 0
        i=0
        while i<len(nums) and nums[i]<=target:
            if nums[i]==target:
                return i
            i+=1
        return i