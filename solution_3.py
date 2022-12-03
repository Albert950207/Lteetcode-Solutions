'''Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        for i in range(1,len(s)):
            new_index = s.index(s[i])
            if i != new_index:
                result = i
                repeat_list = s[new_index+1:]
                return max(result, self.lengthOfLongestSubstring(repeat_list))
        return len(s)



'''
class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        max_sequence = ""
        current_sequence = ""
        for ch in s:
            if ch in current_sequence:
                if len(current_sequence) > len(max_sequence):
                    max_sequence = current_sequence
                current_sequence = current_sequence[current_sequence.index(ch) + 1:] + ch
            else:
                current_sequence += ch
        return max(len(max_sequence), len(current_sequence))

'''·
