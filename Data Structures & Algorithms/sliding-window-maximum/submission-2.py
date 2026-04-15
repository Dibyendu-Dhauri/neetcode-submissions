class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = collections.deque()
        left = right = 0

        while right < len(nums):

            # 1) Ensure the values of the deque maintain a monotonic decreasing order
            # by removing candidates <= the current candidate

            while dq and dq[-1][0] <= nums[right]:
                dq.pop()
            
            # 2) Add the current candidate

            dq.append((nums[right],right))

            # if the window is of lenght 'k', record the maximum of the window.
            if right - left + 1 == k:

                # 3) Remove values whose indexes occur outside the wndow.
                if dq and dq[0][1] < left:
                    dq.popleft()
                
                # The maximum value of this window is the left mose value in the deque.
                res.append(dq[0][0])

                # Slide the window by advancing both 'left' and 'right'.
                # The right pointer always gets advanced so we just need to advance 'left'.
                left += 1
            right += 1
        return res
