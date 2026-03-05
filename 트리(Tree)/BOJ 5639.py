import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

class Node:
    
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    # 초기에 아무 노드도 없는 상태
    def __init__(self):
        self.root = None
    # 루트 노드부터 시작해서 이진 탐색 트리 규칙에 맞는 위치에 노드 삽입
    def insert(self, key):
        #루트 노드가 없는 경우 새로운 노드를 루트 노드로 추가
        if not self.root:
            self.root = Node(key)
        else:
            curr = self.root
            while True:
                # 삽입하려는 값이 현재의 노드 보다 작은 경우 왼쪽 자식 노드로 이동
                if key < curr.val:
                    if curr.left:
                        curr = curr.left
                    else:
                        #현재 노드의 왼쪽 자식이 없는 경우 새로운 노드 추가
                        curr.left = Node(key)
                        break
                else:
                    # 삽입하려는 값이 현재 노드의 보다 큰 경우 오른쪽 자식 노드로 이동
                    if curr.right:
                        curr = curr.right
                    else:
                        # 현재 노드의 오른쪽 자식 노드가 없는 경우 새로운 노드 추가
                        curr.right = Node(key)
                        break

    # 이진 탐색 규칙에 따라 특정값이 있는 지 확인(루트노드부터 시작)
    def search(self,key):
        curr = self.root
        
        # 현재 노드 존재, 찾으려는 값이 같지 않은 경우 반복
        while curr and curr.val != key:
            # 찾으려는 값이 현재 노드보다 작은 경우
            if key < curr.val:
                curr = curr.left
            else:
                #찾으려는 값이 현재 노드의 값보다 큰 경우 오른쪽 자식 노드
                curr = curr.right
        return curr
    
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val)
        

nodes = []

while True:
    line = input().strip() #\n 제거
    if not line: # EOF 빈 문자열 반환
        break
    nodes.append(int(line))
    
bst = BST()

for node in nodes:
    bst.insert(node)

postorder(bst.root)