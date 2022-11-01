nums = [1,1,2] #[0,0,1,1,1,2,2,3,3,4]
old_len = len(nums)
#print(len(list(set(nums))))
#for i in nums:
nums = list(set(nums))
new_len = len(nums)
diff = old_len-new_len
for i in range(diff):
    nums.append('_')

print(nums)
print(new_len)

nums = [0,0,1,1,1,2,2,3,3,4]
size = len(nums)
insertIndex = 1
for i in range(1, size):
    # Found unique element
    print(nums[i - 1])
    print(nums[i])
    if nums[i - 1] != nums[i]:      
        # Updating insertIndex in our main array
        print('Insert Index ',str(insertIndex),' ',str(nums[i]))
        nums[insertIndex] = nums[i] 
        # Incrementing insertIndex count by 1 
        insertIndex = insertIndex + 1       
    #i = i + 1 
print(nums)              
print(insertIndex) 

nums = [0,0,1,1,1,2,2,3,3,4]
size = len(nums)
insert_index = 1
for i in range(1,size):
    if nums[i] != nums[i-1]:
        nums[insert_index] = nums[i] 
        insert_index += 1

print(nums)
print(insert_index)
y = '1;2;3;'
z = y.split(';')
print(len(z))

n = [1,2,3,4]
print(n[-2])