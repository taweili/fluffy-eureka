# write a bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# write a quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)]
        less = []
        greater = []
        for x in arr[:-1]:
            if x < pivot:
                less.append(x)
            else:
                greater.append(x)
                return quick_sort(less) + [pivot] + quick_sort(greater)

