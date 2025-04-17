bubble_arry = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(bubble_arry)
for i in range(n-1):
    for j in range(n-i-1):
        if bubble_arry[j] > bubble_arry[j+1]:
            bubble_arry[j], bubble_arry[j+1] = bubble_arry[j+1], bubble_arry[j]

print("Here is the Sorted array:", bubble_arry)