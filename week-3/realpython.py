class Node:
    def __init__(self,data, next = None):
        self.data = data
        self.next = None

    #this function just return data of the node
    def __repr__(self):
        return self.data

#Created linked list 
class LinkedList:
    def __init__(self):
        #head is none by default when the linked list is created
        self.head = None

    def __repr__(self):
        node = self.head
        #crated an empty array to store the result
        nodes = []
        #loop if the node is not None
        while node is not None:
            #append the node's data into the array
            nodes.append(node.data)
            #the next node become current node
            node = node.next
        #if the node is None, append "None" to the list
        nodes.append("None")
        #return the list of nodes by using -> in between
        return "->" .join(nodes)

#created a LinkedList | Must create a LinkedList first
llist = LinkedList()
print(llist)

#created the first node using Node class
first_node = Node("a")
#assing the first node to the head of the LinkedList, now the head is not null.
llist.head = first_node
print(llist)

#crated a second_node using Node class
second_node = Node("b")
#creating link between second and first node by assigning the second node as the next of the first node
first_node.next = second_node
print(llist)

#crated a third_node using Node class
third_node = Node("c")
#creating link between second and third node by assigning the third node as the next of the second node
second_node.next = third_node
print(llist)