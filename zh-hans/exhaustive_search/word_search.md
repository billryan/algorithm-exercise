# Word Search

## Question

- leetcode: [Word Search | LeetCode OJ](https://leetcode.com/problems/word-search/)
- lintcode: [(123) Word Search](http://www.lintcode.com/en/problem/word-search/)

### Problem Statement

Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

#### Example

Given board =

```
[
  "ABCE",
  "SFCS",
  "ADEE"
]
```

- word = `"ABCCED"`, -&gt; returns `true`,
- word = `"SEE"`, -&gt; returns `true`,
- word = `"ABCB"`, -&gt; returns `false`.

## 题解

典型的 DFS 实现，这里有上下左右四个方向，往四个方向递归之前需要记录坐标处是否被访问过，并且在不满足条件时要重置该标记变量。该题的一大难点是如何处理起始点和字符串的第一个字符不等的情况，我最开始尝试在一个 DFS 中解决，发现很难 bug-free, 而且程序逻辑支离破碎。后来看了下其他题解发现简单粗暴的方法就是双重循环嵌套 DFS...

### Java

```java
public class Solution {
    /**
     * @param board: A list of lists of character
     * @param word: A string
     * @return: A boolean
     */
    public boolean exist(char[][] board, String word) {
        if (board == null || board.length == 0 || board[0].length == 0) return false;
        if (word == null || word.length() == 0) return false;

        boolean[][] visited = new boolean[board.length][board[0].length];
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (dfs(board, word, visited, i, j, 0)) {
                    return true;
                }
            }
        }

        return false;
    }

    public boolean dfs(char[][] board, String word,
                               boolean[][] visited,
                               int row, int col,
                               int wi) {
        // out of index
        if (row < 0 || row > board.length - 1 ||
            col < 0 || col > board[0].length - 1) {
            return false;
        }

        if (!visited[row][col] && board[row][col] == word.charAt(wi)) {
            // return instantly
            if (wi == word.length() - 1) return true;
            // traverse unvisited row and col
            visited[row][col] = true;
            boolean down = dfs(board, word, visited, row + 1, col, wi + 1);
            boolean right = dfs(board, word, visited, row, col + 1, wi + 1);
            boolean up = dfs(board, word, visited, row - 1, col, wi + 1);
            boolean left = dfs(board, word, visited, row, col - 1, wi + 1);
            // reset with false if none of above is true
            visited[row][col] = up || down || left || right;
            return up || down || left || right;
        }

        return false;
    }
}
```

### 源码分析

注意处理好边界退出条件及`visited`在上下左右四个方向均为`false`时需要重置。判断字符串字符和`board`中字符是否相等前需要去掉已访问坐标。如果不引入`visited`二维矩阵，也可以使用特殊字符替换的方法，这样的话空间复杂度就大大降低了，细节见下面参考链接。

### 复杂度分析

DFS 最坏情况下遍历所有坐标点，二重 for 循环最坏情况下也全部执行完，故时间复杂度最差情况下为 $$O(m^2n^2)$$, 使用了`visited`矩阵，空间复杂度为 $$O(mn)$$, 当然这个可以优化到 $$O(1)$$.(原地更改原 board 数组字符内容)。

## Reference

- [LeetCode – Word Search (Java)](http://www.programcreek.com/2014/06/leetcode-word-search-java/)
