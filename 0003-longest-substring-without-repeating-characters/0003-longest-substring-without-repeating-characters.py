class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s를 돌면서 알파벳 하나씩 딕셔너리에 저장
        dict = {}
        start = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] in dict:
                start = max(start,dict[s[i]] + 1)

            dict[s[i]] = i
            max_length = max(max_length,i - start + 1)

        return max_length
