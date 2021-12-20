class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # Method of double pointer
        # Find the min distance between heaters and houses
        # in order to simplify the problem, we put two virtue heaters at the begining and end
        heaters = [-sys.maxsize] + heaters + [sys.maxsize]    # two virtue heaters will not affect the answer
        # Here is an unordered example
        houses.sort()
        heaters.sort()
        len_houses = len(houses)
        len_heaters = len(heaters)
        r = 0
        j = 0   # j: index of heaters
        for i in range(len_houses):
            while j < len_heaters:
                if heaters[j] >= houses[i]:
                    break
                j += 1
            r = max(r, min(houses[i]-heaters[j-1], heaters[j]-houses[i]))
        return r
     
'''
Problem 475.Heaters, the basic idea is quiet simple: find the maximum distance between heaters and houses, we iterate the houses,
for each house, we find a nearest heater (min of two nearby heaters) for it, the min radius is the max of that distance. 

It has been quiet a while for the boundary condition, finally, we fixed it by adding two virtue heaters (far enough, therefore, it will not affect our result)

RESULT:
执行用时: 88 ms   81%
内存消耗: 17.4 MB 93%
'''
