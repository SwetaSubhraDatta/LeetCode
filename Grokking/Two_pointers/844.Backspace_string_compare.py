#backspace string compare

def backspace_compare(s:str,t:str):
    s_list=[]
    t_list=[]
    for i in range(len(s)):
        if s[i]=="#":
            if s_list:
                s_list.pop()
        else:
            s_list.append(s[i])
    for i in range(len(t)):
        if t[i]=="#":
            if t_list:
                t_list.pop()
        else:
            t_list.append(t[i])
    return s_list==t_list

def main():
    print(backspace_compare("ab#c","ad#c"))
main()