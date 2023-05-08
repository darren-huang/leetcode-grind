"""10:12am - 10:30
resume 10:50
finish 10:56 start last check check done 10:58

pass with no mistakes"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        substring = ""

        curr_first_index = 0
        curr_last_index = -1

        t_letters_count = {}
        t_letters_left = 0
        for char in t:
            if char in t_letters_count:
                t_letters_count[char] += 1
            else:
                t_letters_count[char] = 1
                t_letters_left += 1

        while curr_last_index < len(s) - 1:

            # update last letter
            curr_last_index += 1
            last_char = s[curr_last_index]
            if last_char in t_letters_count:
                t_letters_count[last_char] -= 1
                if t_letters_count[last_char] == 0:
                    t_letters_left -= 1

            # update first letter
            while curr_first_index < curr_last_index:
                first_char = s[curr_first_index]
                if first_char not in t_letters_count:
                    curr_first_index += 1
                else:
                    if t_letters_count[first_char] < 0:
                        curr_first_index += 1
                        t_letters_count[first_char] += 1
                    else:
                        break

            # check if it fits
            new_substring = s[curr_first_index:curr_last_index + 1]
            if t_letters_left == 0 and (not substring or len(substring) > len(new_substring)):
                substring = new_substring
        
        return substring

            
