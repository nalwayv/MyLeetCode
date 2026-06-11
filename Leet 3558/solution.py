class Solution:
    def get_max_depth(self, tree: dict[int, list[int]], root: int) -> int:
        if tree and root not in tree:
            return 0
        
        count: int = 0
        for child in tree[root]:
            count = max(count, self.get_max_depth(tree, child) + 1)

        return count

    def build_tree(self, edges: list[list[int]]) -> tuple[dict[int, list[int]], int]:
        tree: dict[int, list[int]] = {}
        root: int = 0
        
        for edge in edges:
            if len(edge) != 2:
                continue
            
            parent: int = edge[0]
            child: int = edge[1]
        
            if parent not in tree:
                tree[parent] = []
                root += parent

            if child not in tree:
                tree[child] = []
                root += child

            tree[parent].append(child)
            root -= child
        
        return tree, root

    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        tree, root = self.build_tree(edges)
        max_depth: int = self.get_max_depth(tree, root)
        return 2 ** (max_depth - 1) % 1000000007


def main() -> None:
    print("3558. Number of Ways to Assign Edge Weights I")
    
    solution = Solution()
    result: int = solution.assignEdgeWeights([[1,2],[1,3],[3,4],[3,5]])
    # result: int = assignEdgeWeights([[2,3],[1,2]])
    # result: int = solution.assignEdgeWeights([[1,2]])
    # result: int = solution.assignEdgeWeights([[3,2],[2,1]])
    print(f"Result: {result}")


if __name__ == "__main__":
    main()