from node import nonLeafNode, leafNode
class bPlusTree:
    def __init__(self,order):
        self.root: nonLeafNode = leafNode(order)     #first node must be leaf to store the data
        self.order = order

    def insert(self,key):
        # print("key to insert in bptree is: ",key)
        
        pass

    def range(self,start,end):
        print("range to search in bptree is: ",start,end)
        pass
    
    def search(self,key):
        print("search key: ",key)
        pass

    def count(self,key):
        print("count key: ",key)
        pass

    #helper

    def merge():
        pass

    def _find():
        pass