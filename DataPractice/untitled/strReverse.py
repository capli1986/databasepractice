#  -*- coding:utf8 -*-

def  get_str(S):
    if  S=="":
        return 0
    else:
        #RS = reversed(S)
        RS=''.join(reversed(S))
        i=1
        NS=[]
        print  "RS",RS
        while(i<=len(S)):
            NS.append(RS[0:i])
            print  "NS",NS
            S=S[0:len(S)-i]
            print  "SSS",S
            RS ="".join(reversed(S))
            i=i+1
        return  NS

if  __name__== '__main__':
    NS = get_str("daahhh")
    print  NS