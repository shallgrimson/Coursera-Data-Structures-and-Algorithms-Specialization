'''
Problem 1: turn an array to a min heap
'''







#build heap
def buildHeap(n, heapArray):
    #sift down if children is less than parent
    def siftDown(i):
        maxIndex = i
        numSwaps = 0

        #check left child
        l = 2*i+1
        if l < n and heapArray[l] < heapArray[maxIndex]:
            maxIndex = l
        
        #check right child
        r = 2*i+2
        if r < n and heapArray[r] < heapArray[maxIndex]:
            maxIndex = r

        if i != maxIndex:
            swaps.append([i, maxIndex])
            heapArray[i], heapArray[maxIndex] = heapArray[maxIndex], heapArray[i]
            siftDown(maxIndex)


    swaps = []
    for i in range(n//2-1,-1,-1): ###if have issues go to n//2
        siftDown(i)
    
    return len(swaps), swaps 

    


if __name__ == "__main__":
    print(buildHeap(5,[5,4,3,2,1]))
    print(buildHeap(5, [1,2,3,4,5]))
    print(buildHeap(4, [15,30,10,5]))