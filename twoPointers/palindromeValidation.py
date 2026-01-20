# Leet code - No.125 : To check whether a give string is palindrom or not

class Solution:
    def isPalindrome(self, s: str):
        left,right = 0, len(s)-1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
                
                left += 1
                right -= 1

            return True

solution = Solution()
print (solution.isPalindrome("Kayak"))
print (solution.isPalindrome("Kathmandu is big"))



        

