class Node:
    def __init__(self, tek_letter='!', father=0):
        self.mas_of_children=[0 for i in range(4)]
        self.my_int=ord(tek_letter)
        self.father=father

    def getpref(self):
        if self.father == 0:
            return ''
        return self.father.getpref() + chr(self.my_int)

class TreeIterator:
    def __init__(self, tree):
        self.list = [tree.root]

    def __next__(self):
        if len(self.list) > 0:
            curr = self.list.pop(0)
            for child in curr.mas_of_children:
                if child != 0:
                    self.list.append(child)
            return curr.getpref()
        else:
            raise StopIteration

class Tree:
    def __init__(self, words):
        self.root=Node()
        for w in words:
            curr=self.root
            for c in w:
                if (curr.mas_of_children[ord(c)-ord('a')] == 0):
                    curr.mas_of_children[ord(c)-ord('a')]=Node(tek_letter=c, father=curr)
                curr=curr.mas_of_children[ord(c)-ord('a')]

    def __iter__(self):
        return TreeIterator(self)


def printtree(koren, offset):
    for i in range(offset):
        print("-----;",end='');
    if (koren==0):
        print('*')
        return

    #print(chr(koren.my_int))
    print(koren.getpref())

    printtree(koren.mas_of_children[3],offset+1)
    printtree(koren.mas_of_children[2],offset+1)
    printtree(koren.mas_of_children[1],offset+1)
    printtree(koren.mas_of_children[0],offset+1)

