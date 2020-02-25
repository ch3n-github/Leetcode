#Author：chen
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #合并列表
        nums=[]
        i=0
        j=0
        l1=len(nums1)
        l2=len(nums2)
        while i!=l1 and j!=l2:
            if nums1[i]<=nums2[j]:
                nums.append(nums1[i])
                i+=1
            else:
                nums.append(nums2[j])
                j+=1
        if i==l1:
            for k in range(j,l2):
                nums.append(nums2[k])
        else:
            for k in range(i,l1):
                nums.append(nums1[k])
        #取中位数
        lennum=len(nums)
        if lennum%2==0:
            return (nums[int(lennum/2)]+nums[int(lennum/2-1)])/2
        else:return nums[lennum//2]