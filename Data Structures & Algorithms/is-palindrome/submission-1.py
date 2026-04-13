class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove whitespace
        # left /right pointer
        # while left < right
         # left += 1, right -= 1, 
         # if left != right return false
         # make sur to convert to lowercase
        final_s = "".join(char.lower() for char in s if char.isalnum())
        left = 0
        right = len(final_s) - 1
        while left < right:
            if final_s[left] != final_s[right]:
                return False
            left += 1
            right -= 1
        return True
