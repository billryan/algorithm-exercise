# Graph - 圖

圖的表示通常使用**鄰接矩陣和鄰接表**，前者易實現但是對於稀疏矩陣會浪費較多空間，後者使用鏈表的方式存儲資訊但是對於圖搜索時間複雜度較高。

## 程式實現

### 鄰接矩陣 (Adjacency Matrix)

設頂點個數爲 V, 那麼鄰接矩陣可以使用 V × V 的二維陣列來表示。
`g[i][j]`表示頂點`i`和頂點`j`的關係，對於無向圖(undirected graph)可以使用0/1表示是否有連接，對於帶有權重的圖則需要使用`INF`來區分。有重邊時保存邊數或者權值最大/小的邊即可。

#### Python
```python
g = [[0 for _ in range(V)] for _ in range(V)]
```

#### Java
```java
/* Java Definition */
int[][] g = new int[V][V];
```

#### C++
```C++
vector<vector<int>> g (V, vector<int>(V, 0));
```


### 鄰接表 (Adjacency List)

鄰接表通過表示從頂點`i`出發到其他所有可能能到的邊。

### 有向圖

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

#### C++

```C++
struct DirectedGraphNode {
    int label;
    vector<DirectedGraphNode*> neighbors;

    DirectedGraphNode(int x): label(x) { }
};
```

### 無向圖同上，只不過在建圖時雙向同時加。

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

#### C++

```C++
struct UndirectedGraphNode {
    int label;
    vector<UndirectedGraphNode*> neighbors;

    UndirectedGraphNode(int x): label(x) { }
};
```