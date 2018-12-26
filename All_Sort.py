"""
    Name:Drishak Mohan
	Date: December 1th, 2018
	Description: All type of sorts .
"""


from typing import List

def bubble_sort(L: List[int]) -> None:
    '''Sort the items in L in non-descending order.
    '''
    
    for iteration in range(len(L)):
        for index in range(len(L) - 1 - iteration):
            if L[index] > L[index + 1]:
                L[index], L[index + 1] = L[index + 1], L[index]
   
def insert(L: List[int], index: int) -> None:
    '''Insert the item at position index in list L into the range [0..index] so
    that [0..index] is in sorted order. [0..index-1] is already sorted.
    '''
    
    while index > 0 and L[index - 1] > L[index]:
        L[index], L[index - 1] = L[index - 1], L[index]
        index -= 1

def insertion_sort(L: List[int]) -> None:
    '''Sort the items in L in non-descending order.
    '''
    for index in range(len(L)):
        insert(L, index)
        
def find_min(L: List[int], index: int) -> int:
    '''Return the index of the smallest number in list L that is at or after
    position index.
    '''
    smallest_index = index
    for i in range(index, len(L)):
        if L[smallest_index] > L[i]:
            smallest_index = i
    return smallest_index
                
def selection_sort(L: List[int]) -> None:
    '''Sort the items in L in non-descending order.
    '''
    for index in range(len(L)):
        swap_index = find_min(L, index)
        L[index], L[swap_index] = L[swap_index], L[index]

# ========================================================

def mergesort(L: List[int]) -> List[int]:
    '''Return a list that contains the items in L in non-descending order.
    '''
    
    # Recursive algorithm: base case. 
    if len(L) < 2:
        return L

    # Recursive case. Note how the problem gets smaller (sorting a smaller 
    # list) on each call.  
    midpt = len(L) // 2
    L1 = mergesort(L[: midpt])
    L2 = mergesort(L[midpt: ])
    merged = merge(L1, L2)
    return merged

def merge(L1: List[int], L2: List[int]) -> List[int]:
    '''Return a new list that contains the items in L1 and L2 in 
    non-descending order. L1 and L2 are both already in that order.
    '''
    
    merged = []
    index1, index2 = 0, 0
    # merge the two lists until one is empty
    while index1 < len(L1) and index2 < len(L2):
        if L1[index1] < L2[index2]:
            merged.append(L1[index1])
            index1 += 1
        else:
            merged.append(L2[index2])
            index2 += 1

    # If a list is empty, it doesn't change the accumulated list if we add it.    
    merged += L1[index1:]
    merged += L2[index2:]
    return merged

def quicksort(L: List[int]):
    quick_sort_helper(L,0,len(L)-1)

def quick_sort_helper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quick_sort_helper(alist,first,splitpoint-1)
       quick_sort_helper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

# ========================================================
 
def system_sort(L: List[int]) -> None:
    '''Sort the items in L in non-descending order.
    '''
    L.sort()
        
if __name__ == "__main__":
    from timing import time_listfunc

    bubble_sort([7, 4, -1, 9, 3, 6, 42])

    for sz in range(1000, 8001, 1000):
        print("Bubble Sort on %d items: %f" % (sz, time_listfunc(bubble_sort, sz, 1)))
        print("Selection Sort on %d items: %f" % (sz, time_listfunc(selection_sort, sz, 3)))
        print("Insertion Sort on %d items: %f" % (sz, time_listfunc(insertion_sort, sz, 3)))
        print("Merge Sort on %d items: %f" % (sz, time_listfunc(mergesort, sz, 3)))
        print("Quick Sort on %d items: %f" % (sz, time_listfunc(quicksort, sz, 3)))
        print("System Sort on %d items: %f" % (sz, time_listfunc(system_sort, sz, 3)))
        