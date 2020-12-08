class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
        
     #traversing list     
    def listprint(self):
        temp = self.headval
        while temp is not None:
            print (temp.dataval)
            temp = temp.nextval
     #insert front       
    def insert_frount(self, item):
    	new = Node(item)
    	new.nextval= self.headval
    	self.headval = new
    #insert rear	
    def insert_r(self, item):
    	new = Node(item)
    	if self.headval == None:
    		self.headval = new
    		return
    	temp = self.headval
    	while temp.nextval is not None:
    		temp = temp.nextval
    	temp.nextval = new
    	
    def delete_front(self):
    	if self.headval == None:
    		prin("list is empty")
    		return	
    	temp = self.headval
    	self.headval = temp.nextval
    	print("the deleted front element is ", temp.dataval)
    	del temp
    	
    def delete_rear(self):
    	if self.headval == None:
    		prin("list is empty")
    		return
    	temp = self.headval
    	previous = None 
    	while temp.nextval is not None:
    		previous = temp 
    		temp = temp.nextval
    	print("the deleted rear element is ", temp.dataval)
    	del temp
    	previous.nextval = None	
		
		
list1 = SLinkedList()
list1.insert_frount(10)
list1.insert_frount(20)
list1.insert_r(30)
list1.insert_r(40)
list1.insert_frount(50)
list1.delete_front()
list1.delete_rear()
list1.delete_front()


list1.listprint()