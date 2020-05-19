# Helper Function
# Merges 2 sorted piecs back together into a single sorted list
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements # initializing an array

    l = r = 0 #index of left an right array

    for i in range(elements): # i is index of new array, [0,0,...]
        if l >= len(arrA): 
            merged_arr[i] = arrB[r]
            r += 1
        elif r >= len(arrB):
            merged_arr[i] = arrA[l]
            l += 1
        
        if arrA[l] < arrB[r]:
            merged_arr[i] = arrA[l]
            l += 1
        else:
            merged_arr[i] = arrB[r]
            r += 1

    #starting at the beggining on arrA and arrB

    

    return merged_arr


# Divides the original list into sublists
# Until there's only 1 item in the list
def merge_sort(arr):
    # Base Case
    if len(arr) > 1: # keep splitting in half
       
        #find middle index
        middle = arr[0] + len(arr) // 2
        # call merge_sort on Left
        left = merge_sort(arr[0:middle])
        # call merge_sort on Right
        right = merge_sort(arr[middle+1:])
        # merge sorted sides
        arr = merge(left, right)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr


