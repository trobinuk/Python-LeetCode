class Solution:
    
    def replace_all(self,s:str) -> str:
        dict_val = {"IV":'4,',"IX":'9,',"XL":'40,',"XC":'90,',"CD":'400,',"CM":'900,'}
        dict_val_1 = {"I":'1,',"V":'5,',"X":'10,',"L":'50,',"C":'100,',"D":'500,',"M":'1000,'}
        for i,j in dict_val.items():
            s=s.replace(i,j)
        for i,j in dict_val_1.items():
            s=s.replace(i,j)
        return s[0:len(s)-1]
            
    def romanToInt(self, s: str) -> int:
        replaced_val = self.replace_all(s)
        y = 0
        for i in replaced_val.split(','):
            y = y+int(i) 
        return y
        
         
'''
dict_val = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
dict_val_1 = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
s = "MCMXCIV"
s = s.replace("IV",'4,')
s = s.replace("IX",'9,')
s = s.replace("XL",'40,')
s = s.replace("XC",'90,')
s = s.replace("CD",'400,')
s = s.replace("CM",'900,')
print(s)
s = s.replace("I",'1,')
s = s.replace("V",'5,')
s = s.replace("X",'10,')
s = s.replace("L",'50,')
s = s.replace("C",'100,')
s = s.replace("D",'500,')
s = s.replace("M",'1000,')
print(s)
s = s[0:len(s)-1]
print(s)
y = 0
for i in s.split(','):
    #print(i,' i',)
    print(int(i))
    y = y+int(i) 
print(y)
'''

def romanToInt_I(self, s: str) ->int:
        # create a dictionary translation
        roman_to_int_dict = {'I':1, "V":5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        # convert roman to int
        list_of_num = [roman_to_int_dict[char] for char in s]
        
        # modify numbers based on current number and last number
        list_of_num = [list_of_num[index] - 2 * list_of_num[index - 1] 
                       if list_of_num[index - 1] < list_of_num[index] and index != 0
                       else list_of_num[index]
                       for index in range(len(list_of_num))]
        # return sum of list
        return sum(list_of_num)