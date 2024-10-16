import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        # 노드의 개수
        self.n = int(input())
        self.graphs = set()

        # 각 노드의 부모가 주어진다
        arr = list(map(int, input().split()))
        for i in range(len(arr)):
            if arr[i] == -1:
                self.root_node = i
                continue
            self.graphs.add((arr[i], i))

        # 지울 노드의 번호
        self.kill = int(input())
        self.is_leaf = [True for _ in range(self.n)]

    def recursion(self, node):
        # 모든 자식 노드들과 연결된 간선을 제거
        for child_node in range(self.n):
            if (node, child_node) in self.graphs:
                self.graphs.remove((node, child_node))
                self.recursion(child_node)

    def run(self):
        if self.kill == self.root_node:
            print(0)
            return

        # 지울 노드부터 이어진 모든 자식 노드들 제거
        self.recursion(self.kill)

        # 지울 노드와 부모 노드 사이의 간선 제거
        for node in range(self.n):
            if (node, self.kill) in self.graphs:
                self.graphs.remove((node, self.kill))

        self.real_nodes = set()
        for edge in self.graphs:
            self.real_nodes.add(edge[0])
            self.real_nodes.add(edge[1])

        if not self.real_nodes:
            print(1)
            return

        # 리프 노드 세기
        for parent_node in range(self.n):
            if parent_node not in self.real_nodes:
                self.is_leaf[parent_node] = False
                continue
            for child_node in range(self.n):
                if (parent_node, child_node) in self.graphs:
                    self.is_leaf[parent_node] = False

        print(self.is_leaf.count(True))

def main():
    instance = Problem()
    instance.run()

if __name__ == "__main__":
    main()