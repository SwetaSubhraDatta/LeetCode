class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        sub_strings = []
        length_of_longest, start_pos, cur_pos = 0
        w_ = []
        while cur_pos <= len(s):
            if cur_pos == len(s):
                if length_of_longest < len(sub_strings):
                    length_of_longest = len(sub_strings)
                break
            each_string = s[cur_pos]
            if each_string in sub_strings:
                start_pos = start_pos + 1
                if length_of_longest < len(sub_strings):
                    length_of_longest = len(sub_strings)
                w_.append("".join(map(str, sub_strings)))
                sub_strings.clear()
                cur_pos = start_pos
                continue
            cur_pos = cur_pos + 1
            sub_strings.append(each_string)
        return length_of_longest

    def length_of_longest_optimised(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)
            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1
        return ans
    
    def length_of_longest_optimised_2(self, s: str) -> int:
        mp_distinct=set()
        w_s=0
        max_length=0
        for i in range(0,len(s)):
            while s[i] in mp_distinct:
                mp_distinct.remove(s[w_s])
                w_s+=1
            mp_distinct.add(s[i])
            max_length=max(max_length,i-w_s+1)
        return max_length


Soln = Solution()
print(Soln.length_of_longest_optimised("dvdf"))


