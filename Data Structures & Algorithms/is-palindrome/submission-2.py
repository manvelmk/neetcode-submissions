class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        left = 0
        right = length - 1
        
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False # no point in continuing, already fails palindrome constraint
            
        return True