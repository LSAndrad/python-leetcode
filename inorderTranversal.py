def inorder_recursive(node):
    if not node:
        return
    
    # 1. Processa subárvore esquerda primeiro
    inorder_recursive(node.left)
    
    # 2. Depois processa o nó atual
    print(node.val)  # Aqui você "visita" o nó
    
    # 3. Por último processa subárvore direita
    inorder_recursive(node.right)
    return

root = [5,3,6,2,4,None,None,1]
print(inorder_recursive(root))