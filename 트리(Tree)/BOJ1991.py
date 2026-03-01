# 백준 -> 트리 순회
N = int(input())
tree = {}

def preorder(nodes):
    if nodes == '.':
        return
    print(nodes,end="") # 루트 노드 먼저 출력
    preorder(tree[nodes][0]) #왼쪽 노드로 이동
    preorder(tree[nodes][1]) # 오른쪽 노드로 이동


def inorder(nodes):
    if nodes == '.':
        return
    inorder(tree[nodes][0])  # 왼쪽 노드 재귀
    print(nodes, end='')     # 루트 노드 출력
    inorder(tree[nodes][1])  # 오른쪽으로 재귀

def postorder(nodes):
    if nodes == '.':
        return
    postorder(tree[nodes][0]) # 왼쪽 노드 재귀
    postorder(tree[nodes][1]) # 오른쪽 노드 재귀
    print(nodes, end="") # 루트 노드 출력

for _ in range(N):
    node, left, right = input().split()
    tree[node] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')
