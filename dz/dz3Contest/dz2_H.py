from itertools import chain
mas1 = [chr(i) for i in (range(ord('0'), ord('9') + 1))]
mas2 = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
mas3 = [chr(i) for i in range(ord('a'), ord('z') + 1)]
ind2char = {x: y for (x, y) in enumerate(chain(mas1, mas2, mas3))}
char2ind = {y: x for (x, y) in enumerate(chain(mas1, mas2, mas3))}


class Node:
    def __init__(self, tek_letter='!', fath=None):
        self.mas_of_children = [None for i in range(len(char2ind))]
        self.father = fath
        self.my_letter = tek_letter
        self.is_end_of_word = 0

    def get_prefix(self):
        if self.father is None:
            return ''
        else:
            return self.father.get_prefix() + self.my_letter

    def get_cnt_children(self):
        len1 = len(list(filter(lambda x: x is None, self.mas_of_children)))
        return len(self.mas_of_children) - len1


class Trie:
    def __init__(self, words=[]):
        self.root = Node()
        self.length = 0
        for w in words:
            self.add(w)

    def add(self, w):
        curr = self.root
        for c in w:
            if (curr.mas_of_children[char2ind[c]] is None):
                curr.mas_of_children[char2ind[c]] = Node(c, curr)
            curr = curr.mas_of_children[char2ind[c]]
        if (curr.is_end_of_word == 1):
            return
        elif (len(w) > 0):
            curr.is_end_of_word = 1
            self.length += 1

    def __len__(self):
        return self.length

    def __iter__(self):
        return TrieIterator(self.root)

    def find_word(self, w):
        candidat_node = self.find_node_by_prefix(w)
        if (candidat_node is not None and candidat_node.is_end_of_word == 1):
            return True
        else:
            return False

    def __contains__(self, w):
        return self.find_word(w)

    def find_node_by_prefix(self, w):
        curr = self.root
        for c in w:
            curr = curr.mas_of_children[char2ind[c]]
            if (curr is None):
                return None
        return curr

    def starts_with(self, prefix):
        candidat_node = self.find_node_by_prefix(prefix)
        if (candidat_node is not None):
            return TrieIterator(candidat_node)
        else:
            return TrieIterator()

    def pop(self, w):
        if (w not in self):
            raise KeyError(w)
        candidat_node = self.find_node_by_prefix(w)
        if (candidat_node.get_cnt_children() != 0):
            candidat_node.is_end_of_word = 0
            self.length -= 1
            return
        curr = candidat_node
        self.length -= 1
        while (curr.my_letter != '!'):
            if (curr.father.get_cnt_children() > 1 or curr.father.is_end_of_word == 1):
                curr.father.mas_of_children[char2ind[curr.my_letter]] = None
                return
            curr.father.mas_of_children[char2ind[curr.my_letter]] = None
            curr = curr.father


class TrieIterator():
    def __init__(self, node=None):
        if (node is None):
            self.list = []
        else:
            self.list = [node]

    def get_next_node(self):
        if (len(self.list) == 0):
            raise StopIteration
        tek_node = self.list.pop(0)
        for nd in tek_node.mas_of_children:
            if (nd is not None):
                self.list.append(nd)
        return tek_node

    def __next__(self):
        while True:
            tek_node = self.get_next_node()
            if (tek_node.is_end_of_word == 1):
                return tek_node.get_prefix()

    def __iter__(self):
        return self
