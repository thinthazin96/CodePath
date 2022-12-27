'''
Top K Frequent Elements: https://leetcode.com/problems/top-k-frequent-elements/

Time complexity: 
'''
def topKFrequent(nums, k):
        d = {}      # dictionary to track frequency of each integer
        freq = [[] for i in range(len(nums) + 1)] # create same size as input list to 

        for n in nums:
            d[n] = 1 + d.get(n, 0)

        for key, value in d.items(): #map count as index with its value
            freq[value].append(key)

        res = []
        for i in range(len(freq) -1, 0, -1): #loop backwards
            for j in freq[i]:               #loop a sublist
                res.append(j)               #if there is element in sublist, append into res.
                if len(res) == k:           #loop stop if the len == k
                    return res


print(topKFrequent([1,1,1,2,2,3],2))