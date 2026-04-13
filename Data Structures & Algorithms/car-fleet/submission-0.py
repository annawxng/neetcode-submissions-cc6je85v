class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # n cars
        # pos = [n], speed = [n]
        pair = [[p, s] for p, s in zip(position, speed)] # need to remb this python syntax
        stack = [] # time = (target - pos) / speed
        for p, s in sorted(pair)[::-1]: # Reverse order - i need to remb this
            # mistake: need to append first before popping, or else u cant compare with the prev car
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)