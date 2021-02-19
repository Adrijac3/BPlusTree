class nonLeafNode:
    def __init__(self,order):
        self.keys = []
        self.children = []
        self.order = order
        self.parent: nonLeafNode = None     #self referential pointer

    def split(self):
        #create new left and right nodes around pivot
        print("non leaf splitting")
        left = nonLeafNode(self.order)
        right = nonLeafNode(self.order)
        mid = self.order//2
        #set their appropriate values
        left.keys = self.keys[:mid]
        left.children = self.children[:mid+1]
        left.parent = self
        right.keys = self.keys[mid+1:]
        right.children = self.children[mid+1:]
        right.parent = self
        #remove left and right values from self
        self.keys = [self.keys[mid]]
        self.children.clear()
        self.children.append(left)
        self.children.append(right)
        #TODO check if condition necessary or not
        #set correct parent for the children
        for c in left.children:
            if isinstance(c,nonLeafNode):
                c.parent = left
        for c in right.children:
            if isinstance(c,nonLeafNode):
                c.parent = right

        return self

class leafNode(nonLeafNode):

    def __init__(self,order):
        super().__init__(order)
        self.nextLeaf: LeafNode = None
    #TODO remove garbage values of children from leaf nodes
    def split(self):
        #create a new intermediate node to hold pivot and merge it later to parent
        temp = nonLeafNode(self.order)
        #create new leaf node to put right half of pivot, store left half in self
        right = leafNode(self.order)
        mid = self.order//2

        #set up temp node
        temp.keys.append(self.keys[mid])
        temp.children.append(self)
        temp.children.append(right)

        #set appropriate values to the left and right nodes
        right.keys = self.keys[mid:]
        # right.children = self.children[mid:]
        right.parent = temp
        right.nextLeaf = self.nextLeaf

        self.keys = self.keys[:mid]
        # self.children= self.children[:mid]
        self.parent = temp
        self.nextLeaf = right
        return temp

    def add(self, key):
        if len(self.keys) == 0:      #empty leaf node.. 1st time insertion being done
            self.keys.append(key)
            # self.values.append(child)
        else:
            i=0
            for k in self.keys:
                if key == k:   #key already present. Add to count
                    return
                elif key < k:  #insert key at appropriate position
                    self.keys = self.keys[:i] + [key] +self.keys[i:]
                    # self.children = self.children[:i] + [child] + self.children[i:]
                    return
                else:
                    i+=1
            #key is bigger than all other keys, so add at last
            self.keys.append(key)
            # self.children.append(child)

    def findKey(self, key):
        i=0
        for k in self.keys:
            if key == k:
                return i
            else:
                i+=1
        return -1
