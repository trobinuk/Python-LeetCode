int_list = [2,6,3,9,11,7]
tar_num = 9
int_list.sort()
print(int_list)

output_list = []
for i in int_list:
    for j in int_list:
        if j >= i and i+j == tar_num:
            output_list.append((i,j))

print(output_list)

def findpairs(nums,target):
    nums.sort()

    output_list = []
    for i in int_list:
        for j in int_list:
            if j >= i and i+j == target:
                output_list.append((i,j))

    return output_list

int_list = [2,6,3,9,11,7]
tar_num = 9
result = findpairs(int_list,tar_num)
print(result)
