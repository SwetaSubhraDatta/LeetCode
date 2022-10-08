# Check if a phrase is a valid pallindrome or not

from curses.ascii import isupper


def check_phrase(s:str):
    concat_strings=""
    for words in s:
        if words==" " or (not words.isalnum()):
            continue
        else:
          words=words.lower()
        concat_strings=concat_strings+words
    return(concat_strings==concat_strings[::-1])




def main():
    check_phrase("0P")

main()