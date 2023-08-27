import hashlib
import timeit
import random
import string
import matplotlib.pyplot as plt

def build_merkle_tree(data):
    tree = [hashlib.sha256(str(item).encode()).hexdigest() for item in data]
    
    while len(tree) > 1:
        new_level = []
        for i in range(0, len(tree), 2):
            if i + 1 < len(tree):
                combined_hash = hashlib.sha256((tree[i] + tree[i + 1]).encode()).hexdigest()
                new_level.append(combined_hash)
            else:
                new_level.append(tree[i])
        tree = new_level
        
    return tree[0]

cadena = ['manzana', 'banina', 'ignacio', 'hola', 'jajaja']

merkle = build_merkle_tree(cadena)

print("Raiz de merkle : " + merkle)