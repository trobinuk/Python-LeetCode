'''
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
'''
heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))

heros=['spider man','thor','hulk','iron man','captain america']

heros.append('black panther')

print(heros)

heros.pop()
print(heros)

for idx,i in enumerate(heros):
    if i == 'hulk':
        idx_val = idx+1
        break
heros.insert(idx_val,'black panther')

print(heros)
heros.remove('hulk')#.replace('thor','doctor strange')
#heros.replace('thor','doctor strange')
heros = list(map(lambda x: x.replace('thor','doctor strange'),heros))
print(heros)

heros.sort()
print(heros)
dir(heros)

'''
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
'''
def list_of_odd_nos(inp_val):
    list_val = [i for i in range(1,inp_val+1)]
    #print(list_val[::2])
    return list_val[::2]

print(list_of_odd_nos(100))