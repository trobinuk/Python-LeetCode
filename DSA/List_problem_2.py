'''
def f(i,values=[]):
    print('The value of i is ',str(i))
    print('The values of list is ',values)
    values.append(i)
    print(values)
    return values

f(1)
f(2)
f(3)
'''

a = [1,2,3,4,5]
print(a[3:(0):-1])

print(a[0])

print(a[0:2])

v=44
print(v[0])

def f(value,values):
    v = 1
    values[0] = 44

t = 3
v = [1,2,3]
print(v)
f(t,v)
print(v)
print(type(v))