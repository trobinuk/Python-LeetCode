temp_list = []
with open('C:\\Users\\trobi\\Desktop\\Projects\\DSA\\weather_sample.csv','r') as file:
    print(file)
    for idx,line in enumerate(file):
        print(line)
        tokens = line.rstrip('\n').split(',')
        day = tokens[0]
        if idx != 0:
            temperature = float(tokens[1])
        else:
            temperature = tokens[1]
        temp_list.append((day,temperature))

print(temp_list)

#What was the average temperature in first week of Jan
total_temp = 0
for idx,i in enumerate(temp_list):
    if idx > 0:
        total_temp += i[1]
    if idx == 8:
        break
print(total_temp/7)



#What was the maximum temperature in first 10 days of Jan
max_temp = 0
for idx,i in enumerate(temp_list):
    if idx > 0:
        if i[1] >= max_temp:
            max_temp = i[1]
        if idx == 11:
            break
print(max_temp)

#What was the temperature on Jan 9?
temp_list = {}
with open('C:\\Users\\trobi\\Desktop\\Projects\\DSA\\weather_sample.csv','r') as file:
    print(file)
    for idx,line in enumerate(file):
        print(line)
        tokens = line.rstrip('\n').split(',')
        day = tokens[0]
        if idx != 0:
            temperature = float(tokens[1])
        else:
            temperature = tokens[1]
        temp_list[day] = temperature

print(temp_list)

print(temp_list['9-Jan-22'])

#What was the temperature on Jan 4?
print(temp_list['4-Jan-22'])

#poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.

with open('C:\\Users\\trobi\\Desktop\\Projects\\DSA\\poems.txt','r') as file:
    print(file)
    words_list = []
    for line in file:
        words_list.extend(line.rstrip('\n').split(' '))

out_dict = {}       
for i in words_list:
    if i in out_dict:
        out_dict[i] = out_dict[i]+1
    else:
        out_dict[i] = 1

print(out_dict)

#Implement hash table where collisions are handled using linear probing. We learnt about linear probing in the video tutorial. Take the hash table implementation that uses chaining and modify methods to use linear probing. Keep MAX size of arr in hashtable as 10.
class HashTable:
    def __init__(self):
        self.max_cnt = 10
        self.arr = [None for i in range(self.max_cnt)]

    def get_hash_val(self,key):
        tot_val = 0
        for i in key:
            tot_val += ord(i)
        return tot_val%self.max_cnt

    def __getitem__(self,key):
        idx = self.get_hash_val(key)
        return self.arr[idx]

    def __setitem__(self,key,val):
        idx = self.get_hash_val(key)
        if self.arr[idx] is None:
            self.arr[idx] = val
            return
        j = idx+1
        if j > self.max_cnt-1:
            j = 0
        for i in range(self.max_cnt):
            if self.arr[j] is None:
                self.arr[j] = val
                break
            if j == self.max_cnt-1:
                j = -1
            j += 1

    def __delitem__(self,key):
        idx = self.get_hash_val(key)
        del self.arr[idx]


hashtable = HashTable()
hashtable['march 6'] = 25
hashtable['march 7'] = 24
hashtable['march 8'] = 89

print(hashtable.arr)

hashtable['march 17'] = 8985
