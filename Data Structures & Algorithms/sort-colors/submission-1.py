class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_cnt = 0
        for num in nums:
            if num == 0:
                zero_cnt += 1
        
        i = 0
        for idx,num in enumerate(nums):
            if num == 0:
                nums[i],nums[idx] = nums[idx],nums[i]
                i += 1
        print(nums)
        one_index = zero_cnt 
        j = zero_cnt
        for i in range(one_index,len(nums)):
            if nums[i] == 1:
                nums[i],nums[j] = nums[j],nums[i]
                j += 1
        print(nums)