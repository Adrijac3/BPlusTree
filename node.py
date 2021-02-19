class nonLeafNode:
    def __init__(self,order):
        self.keys = []
        self.children = []
        self.order = order
        self.parent: nonLeafNode = None     #self referential pointer
        self.count = 0
    
    def find(self, key):
        pass

    def split(self):
        pass

    def overFlow():
        pass



class leafNode(nonLeafNode):

    def __init__(self,order):
        super().__init__(order)
        self.nextLeaf: LeafNode = None

    def split(self):
        #create a new intermediate node to merge later to parent


    def add(self, key, child):
        if len(self.keys == 0):      #empty leaf node.. 1st time insertion being done
            self.keys.append(key)
            self.values.append(value)
        else:
            i=0
            added = False
            for k in self.keys:
                if key == k:   #key already present. Add to count
                    self.count+=1
                    return
                elif key < k:  #insert key at appropriate position
                    self.keys = self.keys[:i] + [key] +self.keys[i:]
                    self.children = self.children[:i] + [child] + self.children[i:]
                    return
                else:
                    i+=1
            #key is bigger than all other keys, so add at last
            self.keys.append(key)
            self.children.append(child)