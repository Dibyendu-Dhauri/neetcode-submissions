class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r = 0, len(nums) -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            elif nums[l] < nums[mid]: #left part is sorted
                if target >= nums[l] and target < nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1
            elif nums[l] > nums[mid]: # right part is sorted
                if target <= nums[r] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid -1
            else:
                l += 1
        return False