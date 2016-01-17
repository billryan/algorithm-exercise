# Route Between Two Nodes in Graph

## Question

- lintcode: [(176) Route Between Two Nodes in Graph](http://www.lintcode.com/en/problem/route-between-two-nodes-in-graph/)
- [Find if there is a path between two vertices in a directed graph - GeeksforGeeks](http://www.geeksforgeeks.org/find-if-there-is-a-path-between-two-vertices-in-a-given-graph/)

### Problem Statement

Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.

#### Example

Given graph:

    A----->B----->C
     \     |
      \    |
       \   |
        \  v
         ->D----->E

for `s = B` and `t = E`, return `true`

for `s = D` and `t = C`, return `false`

## 题解1 - DFS

检测图中两点是否通路，图搜索的简单问题，DFS 或者 BFS 均可，注意检查是否有环即可。这里使用哈希表记录节点是否被处理较为方便。深搜时以起点出发，递归处理其邻居节点，**需要注意的是处理邻居节点的循环时不是直接 return, 而只在找到路径为真时才返回 true, 否则会过早返回 false 而忽略后续可能满足条件的路径。**

### Java

```java
/**
 * Definition for Directed graph.
 * class DirectedGraphNode {
 *     int label;
 *     ArrayList<DirectedGraphNode> neighbors;
 *     DirectedGraphNode(int x) {
 *         label = x;
 *         neighbors = new ArrayList<DirectedGraphNode>();
 *     }
 * }
 */
public class Solution {
   /**
     * @param graph: A list of Directed graph node
     * @param s: the starting Directed graph node
     * @param t: the terminal Directed graph node
     * @return: a boolean value
     */
    public boolean hasRoute(ArrayList<DirectedGraphNode> graph,
                            DirectedGraphNode s, DirectedGraphNode t) {

        Set<DirectedGraphNode> visited = new HashSet<DirectedGraphNode>();
        return dfs(graph, s, t, visited);
    }

    public boolean dfs(ArrayList<DirectedGraphNode> graph,
                       DirectedGraphNode s, DirectedGraphNode t,
                       Set<DirectedGraphNode> visited) {

        if (s == t) {
            return true;
        } else {
            // corner cases
            if (s == null || t == null) return false;
            // flag visited node, avoid cylic
            visited.add(s);
            // compare unvisited neighbor nodes recursively
            if (s.neighbors.size() > 0) {
                for (DirectedGraphNode node : s.neighbors) {
                    if (visited.contains(node)) continue;
                    if (dfs(graph, node, t, visited)) return true;
                }
            }
        }

        return false;
    }
}
```

### 源码分析

根据构造函数的实现，Java 中判断是否有邻居节点时使用`.size`，而不是`null`. 注意深搜前检测是否被处理过。行
```java
if (dfs(graph, node, t, visited)) return true;
```
中注意不是直接 return, 只在为 true 时返回。

### 复杂度分析

遍历所有点及边，时间复杂度为 $$O(V+E)$$.

## 题解2 - BFS

除了深搜处理邻居节点，我们也可以采用 BFS 结合队列处理，优点是不会爆栈，缺点是空间复杂度稍高和实现复杂点。

### Java

```java
/**
 * Definition for Directed graph.
 * class DirectedGraphNode {
 *     int label;
 *     ArrayList<DirectedGraphNode> neighbors;
 *     DirectedGraphNode(int x) {
 *         label = x;
 *         neighbors = new ArrayList<DirectedGraphNode>();
 *     }
 * }
 */
public class Solution {
   /**
     * @param graph: A list of Directed graph node
     * @param s: the starting Directed graph node
     * @param t: the terminal Directed graph node
     * @return: a boolean value
     */
    public boolean hasRoute(ArrayList<DirectedGraphNode> graph,
                            DirectedGraphNode s, DirectedGraphNode t) {

        if (graph == null || s == null || t == null) return false;

        Queue<DirectedGraphNode> q = new LinkedList<DirectedGraphNode>();
        Set<DirectedGraphNode> visited = new HashSet<DirectedGraphNode>();
        q.offer(s);
        while (!q.isEmpty()) {
            int qLen = q.size();
            for (int i = 0; i < qLen; i++) {
                DirectedGraphNode node = q.poll();
                visited.add(node);
                if (node == t) return true;
                // push neighbors into queue
                if (node.neighbors.size() > 0) {
                    for (DirectedGraphNode n : node.neighbors) {
                        // avoid cylic
                        if (visited.contains(n)) continue;
                        q.offer(n);
                    }
                }
            }
        }

        return false;
    }
}
```

### 源码分析

同题解一。

### 复杂度分析

时间复杂度同题解一，也是 $$O(V+E)$$, 空间复杂度最坏情况下为两层多叉树，为 $$O(V+E)$$.
