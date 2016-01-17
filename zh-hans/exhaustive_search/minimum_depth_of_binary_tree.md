# Minimum Depth of Binary Tree

## Question

- leetcode: [Minimum Depth of Binary Tree | LeetCode OJ](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
- lintcode: [(155) Minimum Depth of Binary Tree](http://www.lintcode.com/en/problem/minimum-depth-of-binary-tree/)

```
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node.

Example
Given a binary tree as follow:

        1

     /     \

   2       3

          /    \

        4      5
The minimum depth is 2
```

## 题解

注意审题，题中的最小深度指的是从根节点到**最近的叶子节点（因为题中的最小深度是the number of nodes，故该叶子节点不能是空节点）**，所以需要单独处理叶子节点为空的情况。此题使用 DFS 递归实现比较简单。

### Java

```java
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: An integer.
     */
    public int minDepth(TreeNode root) {
        if (root == null) return 0;

        int leftDepth = minDepth(root.left);
        int rightDepth = minDepth(root.right);

        // current node is not leaf node
        if (root.left == null) {
            return 1 + rightDepth;
        } else if (root.right == null) {
            return 1 + leftDepth;
        }

        return 1 + Math.min(leftDepth, rightDepth);
    }
}
```

### 源码分析

建立好递归模型即可，左右子节点为空时需要单独处理下。

### 复杂度分析

每个节点遍历一次，时间复杂度 $$O(n)$$. 不计栈空间的话空间复杂度 $$O(1)$$.
