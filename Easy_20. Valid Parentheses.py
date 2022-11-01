class Solution:
    def isValid(self, s: str) -> bool:
        l_str = [i for i in s]
        dict_paran = {"(":")","[":"]","{":"}"}
        print('l_str ',l_str)
        
        stack_list = []
        for i in l_str:
            if i in ('(','[','{'):
                stack_list.append(i)
            elif i in (')',']','}'):
                if not stack_list:
                    print('Error 0')
                    return False
                j = stack_list.pop()
                k = dict_paran.get(j)
                print('i ',i,' j ',j,' k ',k)
                if k != i:
                    print('Error 1')
                    return False
            else:
                return False
        if not stack_list:
            return True
 /           
class Solution:
    def isValid(self, s: str) -> bool:
        #s = "()[]{}"
        #print(s)
        dict_paran = {"(":")","[":"]","{":"}"}
        
        i = 0
        while len(s) > 0:
            opp_paran = dict_paran.get(s[i:i+1])
            #print(opp_paran)
            if s.find(opp_paran) >= 0:
                s = s.replace(opp_paran,"")
                #print('After opp_paran ',s)
                s = s.replace(s[i:i+1],"")
                #print('s ',s)
                #print('The Len of S is ',len(s))
            else:
                return False
            #i += 1
        return True
        
/

class Solution:
    def isValid(self, s: str) -> bool:
        #s = "()[]{}"
        #print(s)
        dict_paran = {"(":")","[":"]","{":"}",")":"(","]":"[","}":"{"}
        s_len = len(s)
        if s_len%2 != 0:
            return False
        s_even = ''
        s_odd = ''
        for idx,j in enumerate(s):
            if idx%2 == 0:
                s_even = s_even+j
            else:
                s_odd = s_odd+j
        print(s_even,' ',len(s_even))
        print(s_odd,' ',len(s_odd))
        
        i = 0
        while len(s_even) > 0 and len(s_odd) > 0:
            opp_paran = dict_paran.get(s_even[i:i+1])
            print('opp_paran ',opp_paran)
            if s_odd.find(opp_paran) >= 0:
                s_odd = s_odd.replace(opp_paran,"")
                print('s_odd ',s_odd)
                s_even = s_even.replace(s_even[i:i+1],"")
                print('s_even ',s_even)
                #print('The Len of S is ',len(s))
            else:
                return False
            #i += 1
        return True
/
class Solution:
    def isValid(self, s: str) -> bool:
        #s = "()[]{}"
        #print(s)
        dict_paran = {"(":")","[":"]","{":"}"}
        
        i = 0
        while len(s) > 0:
            try:
                opp_paran = dict_paran.get(s[i:i+1])
                y = s.index(opp_paran)
                print(opp_paran)
                if s.find(opp_paran) >= 0:
                    if y%2 != 0:
                        s = s.replace(opp_paran,"",1)
                        print('After opp_paran ',s)
                        s = s.replace(s[i:i+1],"",1)
                        print('s ',s)
                        #print('The Len of S is ',len(s))                        
                else:
                    return False
                #i += 1
            except:
                return False
        return True
/
class Solution:
    def isValid(self, s: str) -> bool:
        l_str = [i for i in s]
        dict_paran = {"(":")","[":"]","{":"}"}
        print(l_str)
        while len(l_str) > 0:
            try:
                str_1 = l_str[0]
                q = 0
                l_opp_idx = []
                if str_1 in ('(','[','{'):
                    opp_paran = dict_paran.get(str_1)
                    for idx,i in enumerate(l_str):
                        if i == opp_paran:
                            l_opp_idx.append(idx)
                    if not l_opp_idx:
                        print('Error 0')
                        return False
                    for p in l_opp_idx:
                        if p%2 != 0:
                            q = p
                    if q == 0:
                        print('Error 1')
                        return False
                    l_str.pop(q)
                    l_str.pop(0)
                    print('l_str ',l_str)
                else:
                    print('Error 2)
                    return False
            except:
                print('Exception')
                return False
        return True
 
/
class Solution:
    def isValid(self, s: str) -> bool:
        l_str = [i for i in s]
        dict_paran = {"(":")","[":"]","{":"}"}
        print(l_str)
        while len(l_str) > 0:
            try:
                str_1 = l_str[0]
                q = 0
                l_opp_idx = []
                if str_1 in ('(','[','{'):
                    opp_paran = dict_paran.get(str_1)
                    for idx,i in enumerate(l_str):
                        if i == opp_paran:
                            l_opp_idx.append(idx)
                    if not l_opp_idx:
                        print('Error 0')
                        return False
                    for p in l_opp_idx:
                        if p%2 != 0:
                            q = p
                    if q == 0:
                        print('Error 1')
                        return False
                    l_str.pop(q)
                    l_str.pop(0)
                    print('l_str ',l_str)
                else:
                    print('Error 2')
                    return False
            except:
                print('Exception')
                return False
        return True