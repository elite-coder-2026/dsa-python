from enum import Enum
from typing import Optional, Generic, TypeVar

T = TypeVar('T')

class Color(Enum):
    RED = 1
    BLACK = 2

class RedBlackTreeNode(Generic[T]):
    def __init__(self, data: T, color: Color = Color.RED, left: Optional[T] = None, right: Optional[T] = None, parent: Optional[T] = None):
        self.data = data
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

class RedBlackTree(Generic[T]):
    def __init__(self):
        self.nil = RedBlackTreeNode[T](None, Color.BLACK)
        self.root = self.nil

    def insert(self, data: T):
        pass

    def fix_insert(self, data: T) -> None:
        pass

    def left_rotate(self, data: T) -> None:
        pass

    def right_rotate(self, y: RedBlackTreeNode[T]):
        x = y.right
        y.left = x.left

        if x.right is not self.nil:
            x.right.parent = y

        elif y.parent is self.nil:
            x.parent.left = y

        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    def search(self, data: T) -> Optional[T]:
        curr = self.root

        while curr is not self.nil:
            if data is curr.data:
                return curr
            elif data < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def inorder(self) -> list[T]:
        res = []
        self.inorder_util(self.root, res)
        return res

    def inorder_util(self, node: RedBlackTreeNode[T], result: list[T]) -> None:
        if node is self.nil:
            self.inorder_util(node.left, result)
            result.append(node.data)
            self.inorder_util(node.right, result)