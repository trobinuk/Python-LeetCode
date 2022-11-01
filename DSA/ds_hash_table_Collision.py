class HashTable:
    def __init__(self):
        self.cnt = 10
        self.arr = [[] for i in range(self.cnt)] 

    def get_hash_val(self,key):
        tot_val = 0
        for i in key:
           tot_val += ord(i)
        return tot_val%self.cnt

    def __getitem__(self,key):
        idx = self.get_hash_val(key)
        if len(self.arr[idx]) > 0:
            for inner_idx,list_val in enumerate(self.arr[idx]):
                if key == list_val[0]:
                    return self.arr[idx][inner_idx][1]
            return self.arr[idx][1]

    def __delitem__(self,key):
        idx = self.get_hash_val(key)
        for inner_idx,list_val in enumerate(self.arr[idx]):
            if key == list_val[0]:
                del self.arr[idx][inner_idx]
                return
        del self.arr[idx]
    
    def __setitem__(self,key,val):
        idx = self.get_hash_val(key)
        found = False
        #if len(self.arr[idx]) == 0:
        #    self.arr[idx].append((key,val))
        #    return

        for inner_idx,list_val in enumerate(self.arr[idx]):
            if key == list_val[0]:
                self.arr[idx][inner_idx] = (key,val)
                found = True
                break  
        if not found:
            self.arr[idx].append((key,val))

hashtable = HashTable()
print(hashtable.arr)
hashtable.get_hash_val('march 6')
hashtable.get_hash_val('march 17')

hashtable['march 6'] = 25
hashtable['march 7'] = 24
hashtable['march 8'] = 89

print(hashtable.arr)

hashtable['march 17'] = 8985

print(hashtable['march 8'])

del hashtable['march 8']
del hashtable['march 6']
    