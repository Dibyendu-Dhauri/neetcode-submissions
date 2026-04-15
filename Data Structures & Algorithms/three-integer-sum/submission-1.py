class Solution:
    def pair_sum(self,nums,left,right,target):
        pairs = []
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == target:
                pairs.append([nums[left],nums[right],-target])
                left += 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            elif curr_sum > target:
                right -= 1
            else:
                left += 1
        return pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            pairs = self.pair_sum(nums,i+1,len(nums)-1,-nums[i])
            for pair in pairs:
                triplets.append(pair)
        return triplets