class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        max = 0
        start = 0
        for i in range(len(s)):
            current_length = 0
            if s[i] in dict and start <= dict[s[i]]:
                current_length = dict[s[i]] - start +1
                start = dict[s[i]]+1
                dict[s[i]] = i
            else :
                dict[s[i]] = i
                current_length = i - start+1

            if max < current_length:
                max = current_length

        return max

s = "pwwkew"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))