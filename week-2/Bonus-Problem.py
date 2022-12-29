"""
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Understand:
1. Input is nested list
2. Output is string

Match: 
Hash table
Similar problem: Paring who the date

Plan:
1. create an emtpy dictionary and loop through the input list
2. Another loop inside the nested list and store the first element as key and store the second element as value.
3. Check if the key already exists in the dictionary.
4. if yes, append the value to the dictionary.

Time Complexity:
Space Complexity:
"""

def city_path(arr):
    dic = {} 

    # loop through each list in the list
    for cities in arr:
        #set the 1st element of the sublist as first pointer
        p1 = cities[0]
        #set the 2nd element of the sublist as second pointer
        p2 = cities[1]
        #Check the 1st element of the sublist already exist as key in the dictionary
        if p1 not in dic:
            #if not, set it as a key along with empty list as value
            dic[p1] = [] 
        #if yes, add 2nd element of the sublist into its value list
        dic[p1].append(p2)
        #Check the 2nd element of the sublist already exist as key in the dictionary
        if p2 not in dic:
            #if not, set it as a key along with empty list as value
            dic[p2] = []
        #if yes, add 1st element of the sublist into its value list
        dic[p2].append(p1)
                
    
    for k, v in dic.items():
        if k in v:
            
    return dic


print(city_path([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))