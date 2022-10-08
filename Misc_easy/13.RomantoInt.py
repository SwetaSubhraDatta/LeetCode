def romantoint(s:str):
    mp_roman={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000     
    }
    res=0
    for i in range(len(s)):
        if i>0 and mp_roman[s[i]]>mp_roman[s[i-1]]:
            res+=mp_roman[s[i]]-2*mp_roman[s[i-1]]
        else:    
            res+=mp_roman[s[i]]
    return res


def romantoint(s:str):

    sum_list=[]
    mp_roman={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000     
    }
    res=0
    for i in range(len(s)):
        sum_list.append(mp_roman[s[i]])
    
    for j in range(len(sum_list)):
        if j>0:
            sum_list[j]=sum_list[j+1]-sum_list[j]
 



def main():
    print(romantoint("XIV"))
main()