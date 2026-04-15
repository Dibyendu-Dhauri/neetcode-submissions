class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            alive = True 
            #for keeping the track, current element should be insert into the stack or not
            while alive and stack and a < 0 and stack[-1] > 0:
                if stack[-1] < abs(a):
                    stack.pop()
                elif stack[-1] == abs(a):
                    stack.pop()
                    alive = False
                else:
                    alive = False
            
            if alive:
                stack.append(a)
        return stack
