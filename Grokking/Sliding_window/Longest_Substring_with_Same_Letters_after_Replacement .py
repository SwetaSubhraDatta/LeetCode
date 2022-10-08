# The goal is to find the longest substring after replacement

# Step 1: Take Two pointers l and the for loop from 0 to len(s)-1 as r
# Step 2: Keep a map or lut for every occurence of a character in the string
# Step 3: if in a given window the most no of occurence of character is more than k,we can slide the window
# else
# we find the length of longest substing and retun it


def characterReplacement(s: str, k: int) -> int:
    mp_freq = {}  # map to store the frequency of each character in the string
    l = 0  # left pointer
    max_length = 0  # max length of the substring
    for r in range(0, len(s)):  # `r` is the right pointer
        mp_freq[s[r]] = 1 + mp_freq.get(
            s[r], 0
        )  # Add 1 to the count of the current character if the character
        # is not found in the map,init it with a 0
        while (r - l + 1) - max(
            mp_freq.values()
        ) > k:  # If the window size is greater than k,we can slide the window
            mp_freq[
                s[l]
            ] -= 1  # Decrement the count of the character at the left of the window
            l += 1  # Move the left pointer to the next character
        max_length = max(max_length, r - l + 1)  # Update the max length
    return max_length  # The goal is to find the longest substring after replacement


def main():
    print("Length of the longest substring: " + str(characterReplacement("araaci", 2)))
    print("Length of the longest substring: " + str(characterReplacement("araaci", 1)))
    print("Length of the longest substring: " + str(characterReplacement("cbbebi", 3)))


main()
