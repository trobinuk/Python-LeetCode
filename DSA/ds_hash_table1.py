class HashTable:
    def __init__(self):
        self.cnt = 100
        self.arr = [None for i in range(self.cnt)]

    def hash_function(self,inp_key):
        tot_val = 0
        for i in inp_key:
            tot_val += ord(i)
        return tot_val%self.cnt

    def __setitem__(self,key,val):
        hash_val = self.hash_function(key)
        self.arr[hash_val] = val

    def __getitem__(self,inp_key):
        hash_val = self.hash_function(inp_key)
        return self.arr[hash_val]

    def __delitem__(self,inp_key):
        hash_val = self.hash_function(inp_key)
        self.arr[hash_val] = None

hashtable = HashTable()

print(hashtable.arr)

hashtable['Name'] = 'Robinson'
hashtable['Age'] = 27
hashtable['Gender'] = 'M'

print(hashtable.arr)

print(hashtable['Age'])

del hashtable['Age']

print(hashtable['Age'])

print(hashtable.get_data('Name'))

stock_prices = []
with open('C:\\Users\\trobi\\Desktop\\Projects\\DSA\\StockPrices.csv','r') as file:
    print(file)
    for line in file:
        tokens = line.split(',')
        day = tokens[0]
        price = tokens[1]
        stock_prices.append([day,price])

print(stock_prices)

stock_prices = {}
with open('C:\\Users\\trobi\\Desktop\\Projects\\DSA\\StockPrices.csv','r') as file:
    for line in file:
        tokens = line.split(',')
        day = tokens[0]
        price = tokens[1]
        stock_prices[day] = price

print(stock_prices['9-Mar-22'])