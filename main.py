print("--- Step 1: Books List ---\n")
all_books = [
    "Hamlet",
    "Rebecca",
    "Dracula",
    "Matilda",
    "Frankenstein",
    "Carrie",
    "Emma",
]
print(all_books, "\n")

print("--- Step 2: Stack (Undo Delete) ---\n")
topElement = all_books[-1]
popedElement = all_books.pop()
print(f"Deleted book: {popedElement}")
print(f"Undo delete: {topElement} added back")
all_books.append(topElement)
print(all_books, "\n")

print("--- Step 3: Queue (Borrow Requests) ---\n")
Borrowqueue = ["Alice", "Bob", "Charlie"]
print(f"Borrow queue: {Borrowqueue}")
topElement = Borrowqueue[0]
print(f"Next to borrow: {topElement}")
popedElement = Borrowqueue.pop(0)
print(f"Queue after serving: {Borrowqueue}\n")

print("--- Step 4: Linked List (Borrowers) ---")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def travereseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end="=>")
        currentNode = currentNode.next
    print("Borrow")


node1 = Node("Hamlet")
node2 = Node("Rebecca")
node3 = Node("Dracula")

node1.next = node2
node2.next = node3

travereseAndPrint(
    node1,
)

my_books = {
    101: "Hamlet",
    102: "Rebecca",
    103: "Dracula",
}
print("\n--- Step 5: Hash Table (Books by ID) ---")
print("Book 101: ", my_books[101])
print("Book 102: ", my_books[102])
print("Book 103: ", my_books[103], "\n")


tree = {
    "Fiction": {
        "Gothic": ["Dracula", "Frankenstein"],
        "Classic": ["Hamlet", "Rebecca"],
    },
    "Children": {"Fantasy": ["Matilda"]},
}
print("--- Step 6: Category Tree ---")

print("Fiction: Gothic ->", tree["Fiction"]["Gothic"])
print("Fiction: Classic ->", tree["Fiction"]["Classic"])
print("Children: Fantasy ->", tree["Children"]["Fantasy"], "\n")


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=",")
    inOrderTraversal(node.right)


root = TreeNode("Hamlet")
nodeA = TreeNode("Rebecca")
nodeB = TreeNode("Dracula")
nodeC = TreeNode("Matilda")
nodeD = TreeNode("Frankenstein")

root.left = nodeB
root.right = nodeA

nodeB.right = nodeD
nodeA.left = nodeC
print("--- Step 7: Binary Tree (In-order Traversal) ---")
inOrderTraversal(root)
