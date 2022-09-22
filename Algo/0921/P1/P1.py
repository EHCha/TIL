def selectionsort(arr, s):
    n = len(arr)
    if s == n-1:  # Recursion ends here
        return

    mini = s  # declare s as mini
    for i in range(s, n):
        if arr[mini] > arr[i]:  # if [mini] of arr is greater than [i],
            mini = i  # update mini with i

    arr[s], arr[mini] = arr[mini], arr[s]  # rearrange array according to new index

    selectionsort(arr, s+1)


arr = [2, 4, 6, 1, 9, 8, 7, 0]  # array A
selectionsort(arr, 0)
print(arr)



    
