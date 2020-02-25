class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums :return -1
        start=0
        end=len(nums)-1
        if nums[start]==target:return start
        if nums[end]==target:return end
        while end-start+1>=2:
            if nums[start]==target:return start
            if nums[end]==target:return end
            if nums[start]>nums[end]:
                if nums[start]>target and nums[end]<target:return -1
                if target==nums[(start+end+1)//2]:return (start+end+1)//2
                if nums[start]<nums[(start+end+1)//2]:
                    if target>nums[start] and target<nums[(start+end+1)//2]:
                        end=(start+end+1)//2
                        start+=1
                    else:
                        start=(start+end+1)//2
                        end-=1
                else:
                    if target<nums[end] and target>nums[(start+end+1)//2]:
                        start=(start+end+1)//2
                        end-=1
                    else:                   
                        end=(start+end+1)//2
                        start+=1
            else:
                if target<nums[start] or target>nums[end]:return -1
                if target==nums[(start+end+1)//2]:return (start+end+1)//2
                if target<nums[(start+end+1)//2]:
                    end=(start+end+1)//2
                    start+=1
                else:
                    start=(start+end+1)//2
                    end-=1
        return -1