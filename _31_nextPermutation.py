class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:return
        for i in range(len(nums)-1):
            if nums[-1-i]>nums[-2-i]:
                for j in range(len(nums[-1-i:])):
                    if nums[-1-j]>nums[-2-i]:
                        mind=nums[-1-j]
                        nums[-1-j]=nums[-2-i]
                        nums[-2-i]=mind
                        for k in range(len(nums[-1-i:])//2):
                            mind=nums[-1-k]
                            nums[-1-k]=nums[-1-i+k]
                            nums[-1-i+k]=mind
                        return 
        for j in range(len(nums)//2):
            mind=nums[j]
            nums[j]=nums[-1-j]
            nums[-1-j]=mind
        return