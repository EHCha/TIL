<<<<<<< HEAD
def SelectionSort(xs):
    if xs != []: # xs가 빈리스트가 아니라면?
        smallest = min(xs) # xs에서 가장 작은 원소를 찾아 smallest 지정
        xs.remove(smallest) # xs에서 smallest 제거후 xs를 재귀로 정렬하고
        return [smallest] + SelectionSort(xs) # smallest와 정렬된 xs를 나란히 붙여서 리턴한다
    else:
        return [] # 정렬할 원소가 없다면 []를 그대로 리턴.
=======
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



    
>>>>>>> 8ffe72917eb6f730a7610b6ba98d32daad78ec97
