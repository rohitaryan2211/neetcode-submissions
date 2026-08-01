class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_space = s.replace(' ', '').lower()
        s_text = re.sub(r'[^a-zA-Z0-9]', '', s_space)
        s_list = list(s_text)
        print(s_list)

        for i in range(len(s_list)//2):
            if s_list[i] != s_list[-1-i]:
                return False
        return True