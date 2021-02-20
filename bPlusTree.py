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
            c.parent = parent
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
        node = self.getCorrectLeaf(self.root, key)
        node.add(key)
        self.count[key]=1
        while self.checkOverflow(node) == True:
            if node.parent == None:
                node = node.split()
                self.root = node
            else:
                parent = node.parent
                node = node.split()
                index = self.findNodeIndex(parent, node.keys[0])
                self.sendUp(parent, node, index)
                node = parent


    def range(self,start,end):
        node = self.getCorrectLeaf(self.root,start)
        pos = 0
        countRange=0
        while node!=None:
            while pos<len(node.keys):
                if node.keys[pos] >= start and node.keys[pos]<=end:
                    countRange+=self.count[node.keys[pos]]
                pos+=1
            node = node.nextLeaf
            pos = 0
        self.storeResult(str(countRange))
        print(str(countRange))
        
            
    
    def search(self,key):
        node = self.getCorrectLeaf(self.root,key)
        if node.findKey(key) != -1:
            print("YES")
            self.storeResult("YES")
        else:
            print("NO")
            self.storeResult("NO")

    def countKey(self,key):
        if key in self.count.keys():
            print(self.count[key])
            self.storeResult(str(self.count[key]))
        else:
            print("0")
            self.storeResult("0")

    #helpers
    def printTree(self,node):
        print(node.keys)
        for c in node.children:
            self.printTree(c)

    def storeResult(self,msg):
        f2.write(msg+"\n")

    def openFile(self):
        global f2
        f2 = open("output1.txt", 'w+')

    def closeFile(self):
        f2.close()

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
