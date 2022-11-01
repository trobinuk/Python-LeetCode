list_monthly_exp = [['January',2200],['February',2350],['March',2600],['April',2130],['May',2190]]
'''
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''


feb_expense = -1
jan_expense = -1
for i in list_monthly_exp:
    if i[0] == 'January':
        jan_expense = i[1]
        print('jan_expense ',str(jan_expense))
    if i[0] == 'February':
        feb_expense = i[1]
        print('feb_expense ',str(feb_expense))
    if feb_expense >= 0 and jan_expense >= 0:
        print(feb_expense-jan_expense)
        break

list_monthly_exp = [['January',2200],['February',2350],['March',2600],['April',2130],['May',2190]]
sum_val = 0
for i in range(3):
    print(list_monthly_exp[i])
    sum_val += list_monthly_exp[i][1]

print(sum_val)

list_monthly_exp = [['January',2200],['February',2350],['March',2600],['April',2130],['May',2190]]
result = []
for i in list_monthly_exp:
    print(i[1])
    if i[1] == 2000:
        result.append[i[0]]
print(result)

list_monthly_exp = [['January',2200],['February',2350],['March',2600],['April',2130],['May',2190]]
list_monthly_exp.append(['June',1980])
print(list_monthly_exp)

# 5
list_monthly_exp = [['January',2200],['February',2350],['March',2600],['April',2130],['May',2190]]
for idx,i in enumerate(list_monthly_exp):
    if i[0] == 'April':
        list_monthly_exp[idx][1] =i[1]-200

print(list_monthly_exp)

#Can you change this to O(1) with arrays ds I will not be able to do it because I need to know the index of April If index of April is fixed then I can do it in O(n)
#However if I change the datastructure to dictionary Then I will be able to solve it






