# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 11:33:27 2021

@author: Nilesh
"""
import queue


class Tree:
    def __init__(self):
        self.root_node = None
        self.nodes = []
        self.pre_string = ""
        self.post_string = ""
        self.levl_string = ""
        self.in_string = ""
        self.q = []
        self.pp = []
        
    def preorder(self,node):
        if node:
            self.pre_string += str(node.val) + " "
            self.preorder(node.left)
            self.preorder(node.right)
    
    def inorder(self,node):
        if node:
            
            self.inorder(node.left)
            self.in_string += str(node.val) + " "
            self.inorder(node.right)
    
    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            self.post_string += str(node.val) + " "
            
    def preorder_itr(self,node):
        
        while node or len(self.q):
            if node:
                self.pre_string += str(node.val) + " "
                self.q.append(node)
                node = node.left
                
            else:
                node = self.q.pop()
                self.pp.append(node)
                node = node.right
    
    def postorder_itr(self,node):
        temp = {}
        while node or len(self.q):
            if node:
                self.q.append(node)
                node = node.left
                
            else:
                node = self.q.pop()
                if node not in temp:
                    temp[node] = 1
                    self.q.append(node)
                    node = node.right
                else:
                    self.post_string += str(node.val) + " "
                    temp.pop(node)
                    node= None
                    
    def level_traversal(self):
        l = [[self.root_node]]
        
        indexer = 0
        while True:
            temp = []
            for i in l[indexer]:
                self.levl_string += str(i.val) + " "
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            if len(temp):
                l.append(temp)
                indexer += 1
            else:
                break
    
    def height_tree(self, node):
        x = 0
        y = 0
        if node:
            x = self.height_tree(node.left)
            y = self.height_tree(node.right)
            if x > y:
                return x + 1
            else:
                return y + 1
        else:
            return 0
        
    def count_nodes(self, node):
        
        if node:
            x = self.count_nodes(node.left)
            y = self.count_nodes(node.right)
            return x + y + 1
        else:
            return 0
    
    def count_leaf_nodes(self,node):
        
        if node:
            x = self.count_leaf_nodes(node.left)
            y = self.count_leaf_nodes(node.right)
            
            if x == 0 and y == 0:
                return x + y + 1
            else:
                return x + y
        
        else:
            return 0
        
            
class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def createTree():
    root = int(input("Enter the root node value: "))
    q = queue.Queue()
    bt = Tree()
    rn = Node(root)
    bt.root_node = rn
    q.put(bt.root_node)
    
    while not q.empty():
        p = q.get()
        rv = int(input("Enter right node of {}: ".format(p.val)))
        if rv != -1:
            bt.nodes.append(Node(rv))
            p.right = bt.nodes[-1]
            q.put(bt.nodes[-1])
        
        lv = int(input("Enter left node of {}: ".format(p.val)))
        if lv != -1:
            bt.nodes.append(Node(lv))
            p.left = bt.nodes[-1]
            q.put(bt.nodes[-1])
    
    
    return(bt)

bt = createTree()
bt.preorder_itr(bt.root_node)
print("Pre order: ", bt.pre_string)
bt.inorder(bt.root_node)
print("in order: ", bt.in_string)
bt.postorder_itr(bt.root_node)
print("Post order: ", bt.post_string)
bt.level_traversal()
print("Level Traversal: ", bt.levl_string)

print("Height of tree: ", bt.height_tree(bt.root_node))
print("Number of nodes: ",bt.count_nodes(bt.root_node))
print("Number of leaf node: ", bt.count_leaf_nodes(bt.root_node))
