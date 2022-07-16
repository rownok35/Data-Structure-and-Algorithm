def insertion_sort(L):
    n = len(L)

    for i in range(1, n):
        # assign l[i] in item
        item = L[i]
        # Now we need to find the suitable place for the item
        j = i-1

        while j >= 0 and L[j] > item:
            # putting L[j] in his next position
            L[j+1] = L[j]
            j -= 1
            # now L[j+1] is the suitable place for the item
            L[j+1] = item

if __name__ == '__main__':
    L = [4,5,1,9,2]
    print("Brfore sorting", L)
    insertion_sort(L)
    print("After sorting", L)

