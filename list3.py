L = [3, 7, 1, 8, 2, 569, 785]
print("Original List: ", L)
count = 0

for i in L:
    count += i
 
avg = count / len(L)
print("Sum = ", count)
print("Average = ", avg)

L.sort()
print("Smallest element is: ", L[0])
print("Greatest element is: ", L[-1])