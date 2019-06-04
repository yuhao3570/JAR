class Node:
    def __init__(self, n):
        self.n = n
        self.left_child, self.right_child = None, None

    def set_left_child(self, n):
        self.left_child = Node(n)
        return self.left_child

    def set_right_child(self, n):
        self.right_child = Node(n)
        return self.right_child

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root:
            current = self.root
            while True:
                if val == current.n:
                    return
                if val < current.n and current.left_child is not None:
                    current = current.left_child
                elif val > current.n and current.right_child is not None:
                    current = current.right_child
                else:
                    break
            if val < current.n:
                current.set_left_child(val)
            else:
                current.set_right_child(val)
        else:
            self.root = Node(val)

def main():
    t = BinarySearchTree()
    t.add(4)
    t.add(8)
    t.add(2)
    print(t.root.n)
    print(t.root.left_child.n)
    print(t.root.right_child.n)

if __name__ == '__main__': main()
