# Find the Connected Component in the Undirected Graph

## Question

- lintcode: [(431) Find the Connected Component in the Undirected Graph](http://www.lintcode.com/en/problem/find-the-connected-component-in-the-undirected-graph/)

### Problem Statement

Find the number connected component in the undirected graph. Each node in the
graph contains a label and a list of its neighbors. (a connected component (or
just component) of an undirected graph is a subgraph in which any two vertices
are connected to each other by paths, and which is connected to no additional
vertices in the supergraph.)

#### Example

Given graph:



    A------B  C
     \     |  |
      \    |  |
       \   |  |
        \  |  |
          D   E


Return `{A,B,D}, {C,E}`. Since there are two connected component which is
`{A,B,D}, {C,E}`

## 题解1 - DFS

深搜加哈希表（因为有环，必须记录节点是否被访问过）

### Java

```java
/**
 * Definition for Undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     ArrayList<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * }
 */
public class Solution {
    /**
     * @param nodes a array of Undirected graph node
     * @return a connected set of a Undirected graph
     */
    public List<List<Integer>> connectedSet(ArrayList<UndirectedGraphNode> nodes) {
        if (nodes == null || nodes.size() == 0) return null;

        List<List<Integer>> result = new ArrayList<List<Integer>>();
        Set<UndirectedGraphNode> visited = new HashSet<UndirectedGraphNode>();
        for (UndirectedGraphNode node : nodes) {
            if (visited.contains(node)) continue;
            List<Integer> temp = new ArrayList<Integer>();
            dfs(node, visited, temp);
            Collections.sort(temp);
            result.add(temp);
        }

        return result;
    }

    private void dfs(UndirectedGraphNode node,
                     Set<UndirectedGraphNode> visited,
                     List<Integer> result) {

        // add node into result
        result.add(node.label);
        visited.add(node);
        // node is not connected, exclude by for iteration
        // if (node.neighbors.size() == 0 ) return;
        for (UndirectedGraphNode neighbor : node.neighbors) {
            if (visited.contains(neighbor)) continue;
            dfs(neighbor, visited, result);
        }
    }
}
```

### 源码分析

注意题目的输出要求，需要为 Integer 和有序。添加 node 至 result 和 visited 时放一起，且只在 dfs 入口，避免漏解和重解。

### 复杂度分析

遍历所有节点和边一次，时间复杂度 $$O(V+E)$$, 记录节点是否被访问，空间复杂度 $$O(V)$$.

## 题解2 - BFS

深搜容易爆栈，采用 BFS 较为安全。BFS 中记录已经访问的节点在入队前判断，可有效防止不重不漏。

### Java

```java
/**
 * Definition for Undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     ArrayList<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * }
 */
public class Solution {
    /**
     * @param nodes a array of Undirected graph node
     * @return a connected set of a Undirected graph
     */
    public List<List<Integer>> connectedSet(ArrayList<UndirectedGraphNode> nodes) {
        if (nodes == null || nodes.size() == 0) return null;

        List<List<Integer>> result = new ArrayList<List<Integer>>();
        // log visited node before push into queue
        Set<UndirectedGraphNode> visited = new HashSet<UndirectedGraphNode>();
        for (UndirectedGraphNode node : nodes) {
            if (visited.contains(node)) continue;
            List<Integer> row = bfs(node, visited);
            result.add(row);
        }

        return result;
    }

    private List<Integer> bfs(UndirectedGraphNode node,
                              Set<UndirectedGraphNode> visited) {

        List<Integer> row = new ArrayList<Integer>();
        Queue<UndirectedGraphNode> q = new LinkedList<UndirectedGraphNode>();
        q.offer(node);
        visited.add(node);

        while (!q.isEmpty()) {
            UndirectedGraphNode qNode = q.poll();
            row.add(qNode.label);
            for (UndirectedGraphNode neighbor : qNode.neighbors) {
                if (visited.contains(neighbor)) continue;
                q.offer(neighbor);
                visited.add(neighbor);
            }
        }

        Collections.sort(row);
        return row;
    }
}
```

### 源码分析

略

### 复杂度分析

同题解一。

## Reference

- [Find the Connected Component in the Undirected Graph 参考程序 Java/C++/Python](http://www.jiuzhang.com/solutions/find-the-connected-component-in-the-undirected-graph/)
