class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        distance = [float('inf')] * (n + 1)
        distance[k] = distance[0] =  0
        for u,v,w in times:
            graph[u].append((v,w))
        min_heap = [(0,k)] # (distance,node)

        
        while min_heap:
            curr_dis, curr_node = heapq.heappop(min_heap)

            if curr_dis > distance[curr_node]:
                continue
            for nei,weight in graph[curr_node]:
                nei_distance = curr_dis + weight
                if nei_distance < distance[nei]:
                    distance[nei] = nei_distance
                    heapq.heappush(min_heap,(nei_distance,nei))
        
        ans = float('-inf')
        for dist in range(1,len(distance)):
            if distance[dist] == float('inf'):
                return -1
            else:
                ans = max(ans,distance[dist])
        return ans

        
