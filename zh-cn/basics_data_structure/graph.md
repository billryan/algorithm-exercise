# Graph - 图

图的表示通常使用**邻接矩阵和邻接表**，前者易实现但是对于稀疏矩阵会浪费较多空间，后者使用链表的方式存储信息但是对于图搜索时间复杂度较高。

## 编程实现

### 邻接矩阵

设顶点个数为 V, 那么邻接矩阵可以使用 V × V 的二维数组来表示。
`g[i][j]`表示顶点`i`和顶点`j`的关系，对于无向图可以使用0/1表示是否有连接，对于带权图则需要使用`INF`来区分。有重边时保存边数或者权值最大/小的边即可。

#### Python
```python
g = [[0 for _ in range(V)] for _ in range(V)]
```

#### Java
```java
/* Java Definition */
int[][] g = new int[V][V];
```


### 邻接表

邻接表通过表示从顶点`i`出发到其他所有可能能到的边。

### 有向图

#### Python

```python
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
```

#### Java

```java
/* Java Definition */
class DirectedGraphNode {
    int label;
    ArrayList<DirectedGraphNode> neighbors;
    DirectedGraphNode(int x) {
        label = x;
        neighbors = new ArrayList<DirectedGraphNode>();
    }
}
```

### 无向图同上，只不过在建图时双向同时加。

#### Python

```python
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
```


#### Java

```java
class UndirectedGraphNode {
    int label;
    ArrayList<UndirectedGraphNode> neighbors;
    UndirectedGraphNode(int x) {
        this.label = x;
        this.neighbors = new ArrayList<UndirectedGraphNode>();
    }
}
```
