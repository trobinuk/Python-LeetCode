def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 

'''
def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp_match_val = ''
        match_val = strs[0]
        for string_val in strs[1:]:
            if string_val == "":
                return ""
            val_range = len(min(match_val,string_val))
            for j in range(val_range):
                if match_val[j] == string_val[j]:
                    temp_match_val = temp_match_val + match_val[j]
                    if j == val_range-1:
                        match_val = temp_match_val
                        temp_match_val = ''
                else:
                    match_val = temp_match_val
                    temp_match_val = ''
                    break
        return match_val
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #strs = ["flower","flow","flight","flood"]
        temp_match_val = ''
        match_val = strs[0]
        print()
        for string_val in strs[1:]:#range(len(strs)-1):
            print(string_val)
            if string_val == "":
                return ""
            for j in range(len(min(match_val,string_val))):
                print('j ',str(j),' match_val ',match_val[j],' string_val ',string_val[j])
                if match_val[j] == string_val[j]:
                    temp_match_val = temp_match_val + match_val[j]
                    print('Temp ',temp_match_val)
                    if j == len(min(match_val,string_val))-1:
                        match_val = temp_match_val
                        temp_match_val = ''
                        print('match val1 is ',match_val)
                else:
                    match_val = temp_match_val
                    temp_match_val = ''
                    print('match val ',match_val)
                    break
        return match_val
'''