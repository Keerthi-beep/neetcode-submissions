import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        n = len(intervals)     
        pq = []
        ans = 0
        for i in range(n):
            if pq == [] or pq[0]>intervals[i].start:
                heapq.heappush(pq,intervals[i].end)
            else:
                heapq.heappop(pq)
                heapq.heappush(pq,intervals[i].end)
            print(len(pq))
            ans = max(ans,len(pq))
            
        return ans
