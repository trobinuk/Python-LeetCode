array_ex = [1,3,7,45,11,25]

print(array_ex)

output_array = []
for i in range(0,len(array_ex)): 
    #print(len(array_ex)-cnt-1)
    #print(array_ex[len(array_ex)-cnt-1])
    output_array.append(array_ex[len(array_ex)-i-1])
    #print(i)
print(output_array)
