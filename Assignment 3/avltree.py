class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.size = 1 

class AVLTree:
    def __init__(self):
        self.root = None

    def find(self, root, key):
        if not root:
            return False
        if root.key == key:
            return True
        elif key < root.key:
            return self.find(root.left, key)
        else:
            return self.find(root.right, key)

    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        root.size = 1 + self.get_size(root.left) + self.get_size(root.right)

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def remove(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.remove(root.left, key)
        elif key > root.key:
            root.right = self.remove(root.right, key)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.remove(root.right, temp.key)

        if not root:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        root.size = 1 + self.get_size(root.left) + self.get_size(root.right)

        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def order_of_key(self, root, key):
        if not root:
            return 0
        if key < root.key:
            return self.order_of_key(root.left, key)
        elif key > root.key:
            return 1 + self.get_size(root.left) + self.order_of_key(root.right, key)
        else:
            return self.get_size(root.left)

    def get_by_order(self, root, k):
        if not root:
            return None
        left_size = self.get_size(root.left)
        if k < left_size:
            return self.get_by_order(root.left, k)
        elif k > left_size:
            return self.get_by_order(root.right, k - left_size - 1)
        else:
            return root.key

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        z.size = 1 + self.get_size(z.left) + self.get_size(z.right)
        y.size = 1 + self.get_size(y.left) + self.get_size(y.right)
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        z.size = 1 + self.get_size(z.left) + self.get_size(z.right)
        y.size = 1 + self.get_size(y.left) + self.get_size(y.right)
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_size(self, root):
        if not root:
            return 0
        return root.size

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)


tree = AVLTree()
root = None


root = tree.insert(root, 10)
root = tree.insert(root, 20)
root = tree.insert(root, 30)
root = tree.insert(root, 40)
root = tree.insert(root, 50)
root = tree.insert(root, 25)


print(tree.find(root, 30))  
print(tree.find(root, 60))  


root = tree.remove(root, 50)


print(tree.order_of_key(root, 25))  
print(tree.get_by_order(root, 2))   
