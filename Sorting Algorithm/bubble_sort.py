def bubble_sort(L):
    n = len(L)
    
    for i in range(0, n):
        for j in range(0, n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
            
if __name__ == '__main__':
    L = [4,5,1,9,2]
    print("Brfore sorting", L)
    bubble_sort(L)
    print("After sorting", L)