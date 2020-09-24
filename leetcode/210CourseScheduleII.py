"""
There are a total of n courses you have to take labelled from 0 to n - 1.
Some courses may have prerequisites, for example, if
prerequisites[i] = [ai, bi] this means you must take the course bi before the
course ai.
Given the total number of courses numCourses and a list of the prerequisite
pairs, return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them. If it is impossible to
finish all courses, return an empty array.

M: Topological sort
P:
(1) Construct a graph using the prereqs
(2) Perform topological sort, which means performing a post-order DFS on the
graph from every vertices. The DFS also needs to return T/F with F indicating
a cycle.
Keep track of visited (nodes seen), visiting (nodes being process in the
search), order (final order of the nodes)
E: Runtime: O(V + E)
"""

from collections import deque


class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = self.generate_graph(prerequisites)
        visited = set()
        visiting = set()
        order = deque()
        for i in range(numCourses):
            if i not in visited:
                if not self.dfs(graph, i, visiting, visited, order):
                    return []
        return list(order)

    def generate_graph(self, prerequisites):
        graph = {}
        for pre in prerequisites:
            if pre[1] in graph:
                graph[pre[1]].append(pre[0])
            else:
                graph[pre[1]] = [pre[0]]
        return graph

    def dfs(self, graph, node, visiting, visited, order):
        visited.add(node)
        visiting.add(node)
        if node in graph:
            neighbors = graph[node]
            for neighbor in neighbors:
                if neighbor in visiting:
                    # found a cycle
                    return False
                if neighbor not in visited:
                    if not self.dfs(graph, neighbor, visiting, visited, order):
                        return False
        order.appendleft(node)
        visiting.remove(node)
        return True
