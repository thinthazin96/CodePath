#Create Node class with two fields: value and next
class Node(object):
    def __init__(self, v):
        self.val = v
        self.next = None # next is None by default

    #this function is just for present better
    def __repr__(self):
        return f"{self.val} --> {self.next}"

    #insert function for singly linked list
    def insert(self, v):
        n = Node(v) #create an instance of Node
        n.next = self #the previous node become the next node of the instance
        return n 

#this function give the length of the singly linked list
def get_len(ll):
    l = 0 # to track the count of Node
    while ll: #loop ll is not None,
        l += 1 
        ll = ll.next #next node of previous node become the current node
    return l #Return l value if ll is None.

#This function make the same length if one of them is shorter or longer 
def make_same_length(ll1, ll2):
    len1 = get_len(ll1)
    len2 = get_len(ll2)
    if len1 > len2:
        long_ll, short_ll = ll1, ll2
        long_len, short_len = len1, len2
    else:
        long_ll, short_ll = ll2, ll1
        long_len, short_len = len2, len1
    while long_len > short_len:
        long_len -= 1
        long_ll = long_ll.next
    return short_ll, long_ll

common = Node('c1')
short = common.insert('a2').insert('a1')
long = common.insert('b3').insert('b2').insert('b1')
make_same_length(short, long)