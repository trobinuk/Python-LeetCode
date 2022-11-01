class Hashtable:
    def __init__(self):
        arr_cnt = 100
        self.data = ['' for i in range(arr_cnt)]

    def hash_function(self,data_key):
        tot_val = 0
        for i in data_key:
            tot_val += ord(i)
        return (tot_val%10)

    def insert_values(self,data):
        index = self.hash_function(data[0])
        self.data[index] = data[1]

    def get_values(self,data_key):
        index = self.hash_function(data_key)
        return self.data[index]

hashtable = Hashtable()

hashtable.insert_values(['Name','Robinson'])
hashtable.insert_values(['Age',27])
hashtable.insert_values(['Height',6])

#for i in range(len(hashtable.data)):
#    print(hashtable.data)

print(hashtable.get_values('Name'))