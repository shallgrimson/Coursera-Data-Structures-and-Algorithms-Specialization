import random

'''
Problem 1 - Binary Search
'''
def binary_search_recursive(seq, low, high, key):  #maybe want to change to iterative approach (non recursive)
    if high < low:
        return -1
    
    mid = low + int((high-low)/2)
    
    if key == seq[mid]:
        return mid
    elif key < seq[mid]: #key is in left half
        return binary_search(seq, low, mid-1, key)
    else: #key is in right half
        return binary_search(seq,mid+1, high, key)
    

def problem_1_init(find_array, sequence_array):
    indexes = []
    sequence_array_sorted = sequence_array[1:]
    sequence_array_sorted.sort()

    for key in find_array[1:]:
        print(key)
        indexes.append(binary_search(sequence_array_sorted, 0, sequence_array[0]-1, key))

    return indexes

'''
Problem 2 - Majority Element
Majority rule is a decision rule that selects the alternative which has a majority, that is more than half the votes
Goal: Use divide and conquer to determine if there is a majority of elements
'''
def check_majority(len, seq):
    return int(helper(seq, 0, len-1) > 0)
    
def helper(seq, low, high):
    
    if low == high: ##if only have one element
        return seq[low]

    mid = low + int((high-low)/2)
    left_maj = helper(seq, low, mid) #explore left side
    right_maj = helper(seq, mid+1, high) #explore right side


    if left_maj == right_maj: #if both halves have the same majority return it
        return left_maj

    #return if one is higher
    left_cnt = sum([1 for i in range(low, high+1) if seq[i] == left_maj])
    right_cnt = sum([1 for i in range(low, high+1) if seq[i] == right_maj])
    # if left_cnt == right_cnt:
    #     return None
    if left_cnt == right_cnt:
        return 0

    return left_maj if left_cnt > right_cnt else right_maj #return larger one


'''
Problem 3 - Quick Sort Improved
To force the given implementation of the quick sort algorithm to efficiently process sequences with
few unique elements, your goal is replace a 2-way partition with a 3-way partition. That is, your new
partition procedure should partition the array into three parts: < 𝑥 part, = 𝑥 part, and > 𝑥 part.

#done by putting < x elements to the left of the array and if they = x put them at the end and move the pivot down one.  Then swap the elements that =x with those > x to \
create 3 regions

Again this input with have to change for the input
'''
def randomized_quick_sort(arr,low, high):

    if low >= high:
        return

    arr, leftRegion, rightRegion = partition3(arr, low, high)
   
    randomized_quick_sort(arr, low, leftRegion) #sort left region
    randomized_quick_sort(arr, rightRegion, high) #sort right region

    return arr


#now just need to swap the equal elements with the greater ones
def partition3(arr, low, high):
    pivot = random.randint(low, high) #get random pivot
    # arr[randIndex], arr[high] = arr[high], arr[randIndex] #get random pivot
    arr[pivot], arr[high] = arr[high], arr[pivot] #get random pivot

    left, cur, p = low, low, high #left side of region, current index, pivot index

    while cur < p:
        if arr[cur] < arr[p]:
            arr[left], arr[cur] = arr[cur], arr[left]
            left = left + 1
            cur = cur + 1

        elif arr[cur] == arr[p]:
            p = p-1
            arr[cur], arr[p] = arr[p], arr[cur]
            
        else:
            cur = cur + 1
    
    #swap elements that =x with those >x
    right = left
    for i in range(p, high+1):
        arr[right], arr[i] = arr[i], arr[right]
        right = right + 1

    return arr, left-1, right #return arr, end of left region and beginnign of right region


'''
Problem 4 - Number of Inversions
-count number of inversions needed to sort an array, gives idea of how sorted an area is
[[left,mid][mid+1,right]] -> how merge sort splits cells

-could really make numInv and arr globals or wrap them all into a function rather than continully passing them 
'''
def MergeSort_Inversion(arr, left, right, numInv):
    if left >= right:
        return arr, 0

    mid = left + int((right-left)/2)

    arr, numInv = MergeSort_Inversion(arr, left, mid, numInv)
    arr, numInv = MergeSort_Inversion(arr, mid+1, right, numInv)

    return Merge_Inversion(arr, left, mid, right, numInv)

def Merge_Inversion(arr, left, mid, right, numInv):
    i, j = left, mid+1
    A = []

    while i < mid+1 or j < right+1:
        if j >= right+1 or (i < mid+1 and arr[i] < arr[j]):
            A.append(arr[i])
            i = i + 1
        else:
            if j < right+1 and i < mid+1: #check if it is an inversion or the first half of the array is just out of elements
                numInv = numInv + 1

            A.append(arr[j])
            j = j + 1

    for i, e in enumerate(A, start=left):
        arr[i] = e
    
    return arr, numInv


'''
Problem 5 - Organizing a Lottery
-seperate points and segements into an array and keep track if it is a point, left end of segement or right end of segement
-so then get matrix like (5,p),(8,p),(3,p),(4,l),(10,r),(2,l),(6,r) and then sort it to get (2,l),(3,p),(4,l),(5,p),(6,r),(8,p),(10,r)
finally can matrix

0-left side
1-right side
2-points
'''
def lotteryProblem(numSegs, segements, points):
    #crate matrix
    arr = []
    winnings = [0 for i in range(len(points))] #array of winnings for each point

    for i in segements:
        arr.append([i[0], 'l'])
        arr.append([i[1], 'r'])
    
    for ind, p in enumerate(points): #save index in original array as well
        arr.append([p, 'p', ind])

    arr = MergeSort_lottery(arr, 0, len(arr)-1)

    score = 0
    for element in arr:
        if element[1] == 'l':
            score = score + 1
        elif element[1] == 'r':
            score = score -1
        else:
            winnings[element[2]] = winnings[element[2]] + score

    return winnings
    
#sort above matrix using randomized merge sort, this can be changed to a faster one
def MergeSort_lottery(arr, left, right):
    if left >= right:
        return arr

    mid = left + int((right-left)/2)

    arr = MergeSort_lottery(arr, left, mid)
    arr = MergeSort_lottery(arr, mid+1, right)

    return Merge_lottery(arr, left, mid, right)

def Merge_lottery(arr, left, mid, right):
    i, j = left, mid+1
    A = []

    while i < mid+1 or j < right+1:
        if j >= right+1 or (i < mid+1 and arr[i][0] < arr[j][0]):
            A.append(arr[i])
            i = i + 1
        else:
            A.append(arr[j])
            j = j + 1

    for i, e in enumerate(A, start=left):
        arr[i] = e
    
    return arr



'''
Problem 6 - Closest Points
-Note that I did not do this one as I had to look at the Solution but notes about it:
Once len(points) <= 3 bruteforce to find the smallest d within those 2 or 3 points
The at most check 7 points is because you restrict x to within d and then sort Y.  From this sorted Y to start at index 0, thus all other points of Y are above this point (or below depending how the arr is sorted),
that means that there are at most 7 points that need to be checked as they are indisguishable when we restrict x within d and sort Y
'''
def findClosestPoint(points, left, right):
    points = MergeSort_points(points, 0, len(points)-1, 0) #sort x-axis
    

    print(MergeSort_points(points, 0, len(points)-1, 1))

def findMinDistance(points, low, high):
    if len(points[low:high]+1 <= 3):
        return

    mid = low + int((high-low)/2)

    dl = findMinDistance(points, low, mid)
    dr = findMinDistance(points, mid+1, high)

#sort above matrix using randomized merge sort, this can be changed to a faster one
#axis is used to sort by x-axis (0) or y-axis (1)
def MergeSort_points(arr, left, right, axis):
    if left >= right:
        return arr

    mid = left + int((right-left)/2)

    arr = MergeSort_points(arr, left, mid, axis)
    arr = MergeSort_points(arr, mid+1, right, axis)

    return Merge_points(arr, left, mid, right, axis)

def Merge_points(arr, left, mid, right, axis):
    i, j = left, mid+1
    A = []

    while i < mid+1 or j < right+1:
        if j >= right+1 or (i < mid+1 and arr[i][axis] < arr[j][axis]):
            A.append(arr[i])
            i = i + 1
        else:
            A.append(arr[j])
            j = j + 1

    for i, e in enumerate(A, start=left):
        arr[i] = e
    
    return arr


if __name__ == "__main__":
    # sequence = [5,1,5,8,12,13]
    # find = [5,8,1,23,1,11]
    # print(problem_1_init(find, sequence))

    # print(check_majority(5, [2,3,9,2,2]))
    # print(check_majority(6, [3,3,1,9,2,2]))
    # print(check_majority(4,[1,2,3,4]))
    # print(check_majority(1,[1]))
    # print(check_majority(4,[1,2,3,1]))

    
    #print(randomized_quick_sort([1,9,7,4,3,4,2,4], 0, 7))
    #print(randomized_quick_sort([2,3,9,2,2], 0, 4))

    # print(MergeSort_Inversion([2,3,9,2,9], 0, 4, 0))
    #print(Merge_Inversion([2,2,9],[2,3,9]))

    # print(lotteryProblem(2, [[0,5],[7,10]], [1,6,11]))
    # print(lotteryProblem(1, [[-10, 10]], [-100, 100, 0]))
    # print(lotteryProblem(3, [[0, 5], [-3, 2], [7,10]], [1,6]))


    print(findClosestPoint([[7,7],[1,100],[7,7], [4,8]]))