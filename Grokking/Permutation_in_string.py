from collections import Counter
import collections


def find_permutation(str1, pattern):
    l = 0  # left pointer
    mp = []  # set of matched characters
    pattern = list(pattern)
    for r in range(len(str1)):
        mp.append((str1[r]))
        while (r - l + 1) >= len(pattern):
            if sorted(mp) == sorted(pattern):
                return True
            mp.remove(str1[l])
            l += 1
    return False


def find_anagrams(str1, pattern):
    l = 0  # left pointer
    mp = []  # set of matched characters
    ouput = []  # stores the index of the character where the anagram position is found
    pattern = list(pattern)
    for r in range(0, len(str1)):
        mp.append(str1[r])
        while (r - l + 1) >= len(pattern):
            # Check if its an anagram or not
            if sorted(mp) == sorted(pattern):
                ouput.append(l)
            mp.remove(str1[l])
            l += 1
    return ouput


def find_anagrams_optimised(s, p):
    res = []
    sdict, pdict = {}, {}
    l = 0

    # Put all charactersof the pattern into dictionary
    for char in p:
        pdict[char] = pdict.get(char, 0) + 1

    for r in range(len(s)):
        # Move right window/add character to dictionary
        sdict[s[r]] = sdict.get(s[r], 0) + 1

        # Once window is correct length
        if (r - l + 1) == len(p):

            # Append starting index if is anagram
            if sdict == pdict:
                res.append(l)

            # Remove letters from dictionary and left window
            sdict[s[l]] -= 1
            if sdict[s[l]] == 0:
                del sdict[s[l]]
            left += 1

    return res


def smallest_substring_window_L(str1, pattern):
    window_start, matched, substr_start = 0, 0, 0
    min_length = len(str1) + 1
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    # try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] >= 0:  # Count every matching of a character
                matched += 1

        # Shrink the window if we can, finish as soon as we remove a matched character
        while matched == len(pattern):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start

            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                # Note that we could have redundant matching characters, therefore we'll decrement the
                # matched count only when a useful occurrence of a matched character is going out of the window
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    if min_length > len(str1):
        return ""
    return str1[substr_start : substr_start + min_length]


def smallest_substring_window(s, p):
    """
    We are going to follow the sliding window approach for substrings.
    As we need to keep count of number of characters we will use two hashmaps.
    One to keep char frequency and other to remove and add characters.
    Here the only difference we need to keep track of the exact matched charcaters
    as there may be redundant characters.

    for r in range(0,len(s)):
        #add elements to list or hashmap
        while condition is not met:
            #increase the left pointer or shift the window
        return

    #Step 1: Populate the hashmap with the characters of the pattern.
    #Step 2: Iterate over the string and add each character to the strings hashmap
    #Step 3: When a value of character in dict pattern exactly matches with the value in the strings hashmap,we have match
    # Step 4: Until the no of matches becomes equal to the length of the pattern
        # Step 5: We will keep track of the minimum length of the substring 
        # Step 6: We will keep track of the starting index of the min substring
        # Step 7: pop out the first character
        # Step 8: The most important step if that character is already in the pattern and is valid,decrement the match
        # Step 9: increase the left pointer
    Goto step 1 again until r reaches the end of string
    Unpack the right pointer and left pointer from the list and return the substring
                  
    """
    # Add Step 0 to handle a stupid edge case
    if p=="":
        return ""
    
    mp_pattern, mp_string = {}, {} # Hashmap to keep track of the characters in the pattern and string

    l = 0 # left pointer

    matched = 0 # matched characters

    min_length = float("infinity") # minimum length of the substring init to infinity
    res=[-1,-1]

    # Populate the hashmap with the characters of the pattern.
    for i in range(len(p)):
        mp_pattern[p[i]] = mp_pattern.get(p[i], 0) + 1 # add to the hashmap

    # Iterate over the string and add each character to the strings hashmap.
    for r in range(len(s)):
        mp_string[s[r]] = mp_string.get(s[r], 0) + 1 # add to the hashmap

        if s[r] in mp_pattern and mp_pattern[s[r]] == mp_string[s[r]]: # if the character is in the pattern and matches with the string
            matched += 1 # increment the matched characters
            
        while matched == len(mp_pattern): # UNTIL the matched characters are equal to the length of the pattern

            if r-l+1<min_length: # if the length is less than the min length
               res=[l,r]#starting index
               min_length=r-l+1 # update the min length

            mp_string[s[l]] -= 1 # pop the first character
            if s[l] in mp_pattern and mp_string[s[l]] < mp_pattern[s[l]]: # if the character is in the pattern and matches with the string
                matched -= 1 #As the matched string is popped also decrement the matched counter
                
            l += 1 #increase the left pointer
    l,r=res
    return s[l:r+1] if min_length != float("infinity") else "" # return the min window if its infinity means no min window was found
    



def main():
    # find_permutation("bcdxabcdy", "bcdy")
    # find_anagrams("abcdefghicba", "abc")
    d = smallest_substring_window("cabwefgewcwaefgcf","cae")
    print(d)


main()
