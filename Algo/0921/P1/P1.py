def SelectionSort(xs):
    if xs != []: # xs가 빈리스트가 아니라면?
        smallest = min(xs) # xs에서 가장 작은 원소를 찾아 smallest 지정
        xs.remove(smallest) # xs에서 smallest 제거후 xs를 재귀로 정렬하고
        return [smallest] + SelectionSort(xs) # smallest와 정렬된 xs를 나란히 붙여서 리턴한다
    else:
        return [] # 정렬할 원소가 없다면 []를 그대로 리턴.
