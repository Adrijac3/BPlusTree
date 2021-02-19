from node import nonLeafNode, leafNode
class bPlusTree:
    def __init__(self,order):
        self.root = leafNode(order)     #very first node is leaf
        self.count = {}                 #dict to store duplicate key's count

    ### function that takes us to desired leaf for that key related operation
    def getCorrectLeaf(self, node, key):
        while not isinstance(node, leafNode):
            node = self.findNode(node, key)
        return node
    ### function to check if the node is full
    def checkOverflow(self, node):
        if len(node.keys) == node.order:
            return True
        else:
            return False
    
    ###Function to send the splitted node up to its parent
    def sendUp(self,parent, temp, pos):
        parent.children.pop(pos)
        #set correct parent of children of temp
        for c in temp.children:
            if isinstance(c, nonLeafNode):
                c.parent = parent
            else:
                continue
        i=0
        for k in parent.keys:
            if temp.keys[0] < k:
                parent.keys = parent.keys[:i] + [temp.keys[0]] + parent.keys[i:]
                parent.children = parent.children[:i] + temp.children + parent.children[i:]
                return
            else:
                i+=1
        parent.keys.append(temp.keys[0])
        for c in temp.children:
            parent.children.append(c)
        return

    def insert(self,key):
        if key in self.count.keys():
            self.count[key]+=1
            return
        # print("key to insert in bptree is: ",key)
        node = self.getCorrectLeaf(self.root, key)
        node.add(key)
        self.count[key]=1
        while self.checkOverflow(node) == True:
            print(node.keys)
            if node.parent == None:
                node = node.split()
                self.root = node
                print("root at present= ",self.root.keys)
                print("parent of root= ", self.root.parent)
            else:
                parent = node.parent
                node = node.split()
                index = self.findNodeIndex(parent, node.keys[0])
                self.sendUp(parent, node, index)
                node = parent


    def range(self,start,end):
        # print("range to search in bptree is: ",start,end)
        node = self.getCorrectLeaf(self.root,start)
        pos = node.findKey(start)
        if pos == -1:
            print("Invalid start key")
            return
        countRange=0
        print("pos= ",pos)
        while node!=None:
            while pos<len(node.keys) and node.keys[pos]<=end:
                if node.keys[pos] == end:
                    countRange+=self.count[node.keys[pos]]
                    print(countRange)
                    return
                countRange+=self.count[node.keys[pos]]
                pos+=1
            node = node.nextLeaf
            pos = 0
        print("Invalid end key")
        
            
    
    def search(self,key):
        # print("search key: ",key)
        node = self.getCorrectLeaf(self.root,key)
        print("node fetched to search: ",node.keys)
        if node.findKey(key) != -1:
            print("Present\n")
        else:
            print("Absent\n")

    def countKey(self,key):
        if key in self.count.keys():
            print("Count of key: ",key, "=", self.count[key])
        else:
            print("Key not present in this tree")

    #helpers
    def printTree(self,node):
        print(node.keys)
        for c in node.children:
            self.printTree(c)

    @staticmethod
    def findNode(node, key):
        i=0
        for k in node.keys:
            if key < k:
                return node.children[i]
            else:
                i+=1
        return node.children[i]
    @staticmethod
    def findNodeIndex(node, key):
        i=0
        for k in node.keys:
            if key < k:
                return i
            else:
                i+=1
        return i
