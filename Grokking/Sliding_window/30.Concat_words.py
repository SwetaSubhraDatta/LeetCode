
def findSubstring(s:str, words: list):
    mp_words={}
    mp_string={}
    word_len=len(words[0])
    ans=[]
    window_size=len(words)*word_len
    for i in words:
        mp_words[i]=mp_words.get(i,0)+1

    for r in range(0,len(s)-window_size+1):
        temp=s[r:r+window_size]
        if(len(mp_string)>0):
            mp_string.clear()
        while temp:
            if temp[:word_len] in mp_words:
                mp_string[temp[:word_len]]=mp_string.get(temp[:word_len],0)+1
            temp=temp[word_len:]
        if mp_string==mp_words:
            ans.append(r)
    return ans


        

def main():
    d=findSubstring("mindrabooowifoonglingdingbarrwingmonkeypoundcake",words=["fooo","barr","wing","ding","wing"])
    print(d)

main()