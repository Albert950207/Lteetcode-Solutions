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
