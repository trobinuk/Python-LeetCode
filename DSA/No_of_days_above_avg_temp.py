from array import *

print('How many day\'s temperature?')
int_day = int(input())
arr_ex = array('i',[])
cnt = 0

for i in range(int_day):
    print('Day '+str(i+1)+'\'s high temp')
    days_temp = int(input())
    arr_ex.append(days_temp)

average_temp = sum(arr_ex)/len(arr_ex)
for i in arr_ex:
    if i > average_temp:
        cnt += 1
        #print(arr_ex.index(i)+1) If we want to know which day it was

print('Average = '+str(average_temp))
print(str(cnt)+' day (s) above average')
