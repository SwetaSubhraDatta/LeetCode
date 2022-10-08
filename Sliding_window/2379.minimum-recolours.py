import math


def minimumRecolors(s: str, k: int) -> int:
        res=math.inf
        for i in range(0,len(s)):
            x=s[i:k+i]
            if len(x)==k:
                g=x.count("W")
            else:
                break
            res=min(res,g)
        return res







           


def main():
    d= minimumRecolors(s="WBWBBBW", k=4)
    print(d)
main()
    