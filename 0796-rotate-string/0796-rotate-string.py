class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        val = False
        if len(s) == len(goal) and goal in s + s:
            val = True
        return val