# Helper Function
# Merges 2 sorted piecs back together into a single sorted list
def merge(arrA, arrB): # [5]  [9]
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements # initializing an array
    l = r = 0 #index of left an right array

    for i in range(elements): # i is index of new array, [0,0,...]
        if l >= len(arrA): #l is out of range, push r to array
            merged_arr[i] = arrB[r]
            r += 1
        elif r >= len(arrB): #r is out of range, push l to array
            merged_arr[i] = arrA[l]
            l += 1
        
        elif arrA[l] < arrB[r]:
            merged_arr[i] = arrA[l]
            l += 1
        else:
            merged_arr[i] = arrB[r]
            r += 1

    #starting at the beggining on arrA and arrB
    return merged_arr


# Divides the original list into sublists
# Until there's only 1 item in a list
# [4,2,1,6,3]
# [4, 2] [1, 6, 3]
# ...
def merge_sort(arr):
    # Base Case
    if len(arr) > 1: # keep splitting in half
       
        #find middle index
        middle = 0 + len(arr) // 2
        # call merge_sort on Left
        left = merge_sort(arr[0:middle])
        # call merge_sort on Right
        right = merge_sort(arr[middle:])
        # merge sorted sides
        arr = merge(left, right)

    return arr



# implement an in-place merge sort algorithm
# merges the 2 arrays - arr[left...mid] and arr[mid + 1 ... right]
# [3]   [1]   [4]   [2]     [0]
#start        mid  start2   end
def merge_in_place(arr, start, mid, end):
    start2 = mid + 1

    #check if it's already sorted
    if (arr[mid] <= arr[start2]):
        return;
    
    #2 pointers to maintain start of both arrays to merge
    while(start <= mid and start2 <= end): 
        #check if first element is in place
        if (arr[start] <= arr[start2]):
            start += 1
        else:
            value = arr[start2]
            index = start2
            #Swap
            while (index != start):
                arr[index] = arr[index-1]
                index-=1
            arr[start] = value

            #Update pointers
            start += 1
            mid +1
            start2 += 1

def merge_sort_in_place(arr, l, r): 
   if (l < r):
       #find middle
       mid = l + (r-1) // 2
       #recursion on left
       merge_sort_in_place(arr, l, mid)
       #recursion on right
       merge_sort_in_place(arr, mid+1, r)
       #call the merge function to put it back together
       merge_in_place(arr, l, mid, r)

   return arr





#Quicksort  ✔
# [ 5 9 3 7 2 8 1 6 ]
def quicksort(arr):
    # pick first number - it's sorted [5] - it's middle
    # compare the rest of the numbers to 5
    # append smaller to left and bigger to right
    # leftside[3 2 1]  [5]  rightside[9 7 8 6]
    # we have now two unsorted lists: left and rightside
    # use RECURSION in left - 2 is sorted
    # [2 1][3][]       [5]  [9 7 s8 6]
    # Recurse Left again
    # [1][2][]    [3] []       [5]  [9 7 8 6]
    # Recurse Left and find th base case
    # "1 is sorted"
    # recurse right - [] - empty array base case
    # recurse right again - base case - empty array
    # recurse right again - [9 7 8 6]
    # [1][2][][3][]   [5]   [7 8 6][9][]
    # recurse left again - always left first
    # [1][2][][3][]   [5]   [6][7][8] [9][]
    # PLAN
    # Base case: if array length is 0 or 1
    # Return array
    # Else: pick pivot, usually first number
    # put smaller to left and bigger to right array
    # return quicksort(left) + quicksort(right)
    # [1, 2] [null, 3]
    # [1, 2, 3]
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
    for value in arr[1:]:
        if value <= pivot:
            left.append(value)
        else:
            right.append(value)
    
    return quicksort(left) + [pivot] + quicksort(right) 

arr = [45,2,6,21,1,3,9]
arr_size = len(arr)

print(quicksort(arr))

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr


