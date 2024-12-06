from LinkedBinaryTree import LinkedBinaryTree as Tree

tree = Tree()
print("Vertex: r a b c d e f g h")
print("L.C     a b - e - - - - - ")
print("R.C     - c d f - g - h - ")
tree._add_root('r')
tree._add_left(tree.root(), 'a')
tree._add_left(tree.left(tree.root()), 'b')
tree._add_right(tree.left(tree.root()), 'c')
tree._add_right(tree.left(tree.left(tree.root())), 'd')
tree._add_left(tree.right(tree.left(tree.root())), 'e')
tree._add_right(tree.right(tree.left(tree.root())), 'f')
tree._add_right(tree.left(tree.right(tree.left(tree.root()))), 'g')
tree._add_right(tree.right(tree.left(tree.right(tree.left(tree.root())))), 'h')


#use the preorder traversal to print the tree
print("Preorder traversal: ", end = " ")
for i in tree.positions():
    print(i.element(), end = " ")
print()

#use the post order traversal to print the tree
print("Postorder traversal: ", end = " ")
for i in tree.postorder():
    print(i.element(), end = " ")
print()
print()

tree = Tree()
print("Vertex: r a b c d e f g ")
print("L.C     a c - - - - - -  ")
print("R.C     b d e - - f g -  ")
tree._add_root('r')
tree._add_left(tree.root(), 'a')
tree._add_right(tree.root(), 'b')
tree._add_left(tree.left(tree.root()), 'c')
tree._add_right(tree.left(tree.root()), 'd')
tree._add_right(tree.right(tree.root()), 'e')
tree._add_right(tree.right(tree.right(tree.root())), 'f')
tree._add_right(tree.right(tree.right(tree.right(tree.root()))), 'g')

#use the preorder traversal to print the tree
print("Preorder traversal: ", end = " ")
for i in tree.positions():
    print(i.element(), end = " ")
print()

#use the post order traversal to print the tree
print("Postorder traversal: ", end = " ")
for i in tree.postorder():
    print(i.element(), end = " ")
print()
print()

tree = Tree()
print("Vertex: r a b c d e f")
print("L.C     a - d f - - - ")
print("R.C     b c e - - - - ")
tree._add_root('r')
tree._add_left(tree.root(), 'a')
tree._add_right(tree.root(), 'b')
tree._add_left(tree.left(tree.root()), 'c')
tree._add_left(tree.right(tree.root()), 'd')
tree._add_right(tree.right(tree.root()), 'e')
tree._add_left(tree.left(tree.left(tree.root())), 'f')



#use the preorder traversal to print the tree
print("Preorder traversal: ", end = " ")
for i in tree.positions():
    print(i.element(), end = " ")
print()

#use the post order traversal to print the tree
print("Postorder traversal: ", end = " ")
for i in tree.postorder():
    print(i.element(), end = " ")
print()
print()

tree = Tree()
print("Vertex: r a b c d e f g h i")
print("L.C     a c f g - i - - - -")
print("R.C     b d f h - - - - - -")
tree._add_root('r')
tree._add_left(tree.root(), 'a')
tree._add_right(tree.root(), 'b')
tree._add_left(tree.left(tree.root()), 'c')
tree._add_right(tree.left(tree.root()), 'd')
tree._add_left(tree.right(tree.root()), 'e')
tree._add_right(tree.right(tree.root()), 'f')
tree._add_left(tree.left(tree.left(tree.root())), 'g')
tree._add_right(tree.left(tree.left(tree.root())), 'h')
tree._add_left(tree.left(tree.right(tree.root())), 'i')


#use the preorder traversal to print the tree
print("Preorder traversal: ", end = " ")
for i in tree.positions():
    print(i.element(), end = " ")
print()

#use the post order traversal to print the tree
print("Postorder traversal: ", end = " ")
for i in tree.postorder():
    print(i.element(), end = " ")
print()
print()

#add an inorder algorithm for the tree
#The following equations should be written into a binary tree
#Equation 1: (3 * 5) - ((4 * 5) + (6 - 7))
#Equation 2: ((a + b) * c) - (d - e)
#Equation 3: ((a ^ b) + (c + d)) + ((e * f) / (g + h)
#Equation 4: (a + b) / (c * (d - (e ^ f)))
#Equation 5: ((a - b) + c) * ((d + e) * (f / g))
#Equation 6: (((5+2) ∗ (2−1))/((2+9) + ((7−2)−1)) ∗ 8)
