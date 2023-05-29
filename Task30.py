class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i in range(n):
            if group[i] == -1: group[i] = i + m  # re-group

        graph0 = {}  # digraph of groups
        indeg0 = [0] * (m + n)  # indegree of groups

        graph1 = {}  # digrpah of items
        indeg1 = [0] * n  # indegree of items

        for i, x in enumerate(beforeItems):
            for xx in x:
                if group[xx] != group[i]:
                    graph0.setdefault(group[xx], []).append(group[i])
                    indeg0[group[i]] += 1
                graph1.setdefault(xx, []).append(i)
                indeg1[i] += 1

        def fn(graph, indeg):
            """Return topological sort of graph using Kahn's algo."""
            ans = []
            stack = [k for k in range(len(indeg)) if indeg[k] == 0]
            while stack:
                n = stack.pop()
                ans.append(n)
                for nn in graph.get(n, []):
                    indeg[nn] -= 1
                    if indeg[nn] == 0: stack.append(nn)
            return ans

        tp0 = fn(graph0, indeg0)
        if len(tp0) != len(indeg0): return []

        tp1 = fn(graph1, indeg1)
        if len(tp1) != len(indeg1): return []

        mp0 = {x: i for i, x in enumerate(tp0)}
        mp1 = {x: i for i, x in enumerate(tp1)}

        return sorted(range(n), key=lambda x: (mp0[group[x]], mp1[x]))