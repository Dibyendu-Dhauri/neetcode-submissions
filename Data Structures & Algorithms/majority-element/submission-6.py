class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        cnt = 0
        maj_element = 0
        for num in nums:
            if cnt == 0:
                maj_element = num
            cnt += 1 if num == maj_element else -1
        return maj_element