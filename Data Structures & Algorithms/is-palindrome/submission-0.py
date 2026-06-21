class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        reversed_string = cleaned_string[::-1]

        print(reversed_string)
        print()

        if reversed_string == cleaned_string:
            return True
        
        return False
        