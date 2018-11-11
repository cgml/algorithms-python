'''
BST: prev / next / range
'''

class BST():
    pass

bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)
bst.insert(25)
bst.insert(10)
bst.insert(45)
bst.insert(35)
bst.insert(33)

print(bst.get_prev_next(45))
print(bst.get_prev_next(35))
print(bst.delete(50))
print(bst.get_prev_next(45))