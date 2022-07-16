def selection_sort(L):
    n = len(L)
    
    for i in range(0, n-1):
        index_min = i

        for j in range(i+1, n):
            if L[index_min] > L[j]:
                index_min = j
            
            if index_min != i:
                L[i], L[index_min] = L[index_min], L[i]

if __name__ == '__main__':
    L = [4,5,1,9,2]
    print("Brfore sorting", L)
    selection_sort(L)
    print("After sorting", L)

