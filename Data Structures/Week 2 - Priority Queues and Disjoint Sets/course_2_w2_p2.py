from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

'''
Problem 2 - Parallel Processing
Soln-
-Priority queue for the threads - min heap
-stack for the process
'''
class minHeap:
    def __init__(self, nThreads):
        self.n = nThreads
        self.heapArray = [0 for i in range(nThreads)]
        self.threadArray = [i for i in range(nThreads)]

    ##create class maybe
    #pi - parent index, ci - child index
    def compare(self, parent, pi, child, ci): #tells if need to swap two nodes
        if parent == child:
            return ci < pi
        
        return parent > child
        

    #sift down if children is less than parent
    def siftDown(self, i):
        maxIndex = i
        numSwaps = 0

        #check left child
        l = 2*i+1
        if l < self.n and self.compare(self.heapArray[maxIndex], self.threadArray[maxIndex], self.heapArray[l], self.threadArray[l]):
            maxIndex = l
        
        #check right child
        r = 2*i+2
        if r < self.n and self.compare(self.heapArray[maxIndex], self.threadArray[maxIndex], self.heapArray[r], self.threadArray[r]):
            maxIndex = r

        if i != maxIndex:
            self.heapArray[i], self.heapArray[maxIndex] = self.heapArray[maxIndex], self.heapArray[i] #perform swap if needed
            self.threadArray[i], self.threadArray[maxIndex] = self.threadArray[maxIndex], self.threadArray[i] #swap thread indexes
            self.siftDown(maxIndex)


# def buildHeap(n, heapArray):
#     for i in range(n//2-1,-1,-1): ###if have issues go to n//2
#         siftDown(i)
    
#     return heapArray 

def assignJobs(nWorks, jobs):
    jobHeap = minHeap(nWorks)
    result = []
    for job in jobs:
        result.append([jobHeap.threadArray[0], jobHeap.heapArray[0]])
        jobHeap.heapArray[0] += job
        jobHeap.siftDown(0)
    
    return result



def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs
    # n_workers = 2
    # jobs = [1,2,3,4,5]
    assigned_jobs = assignJobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job[0], job[1])


if __name__ == "__main__":
    main()