class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for index, task in enumerate(tasks):
            tasks[index].append(index)
        tasks.sort(key=lambda t: t[0])
        i , time = 0, tasks[0][0]

        res, minHeap = [],[]

        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap,[tasks[i][1],tasks[i][2]])
                i += 1
            
            if not minHeap:
                time = tasks[i][0]
            else:
                process_time, index = heapq.heappop(minHeap)
                time += process_time
                res.append(index)
        
        return res