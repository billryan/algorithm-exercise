# Minimum Absolute Difference in BST

Tags: Binary Search Tree, Easy

## Question

- leetcode: [Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

### Problem Statement

Given a binary search tree with non-negative values, find the minimum
[absolute difference](https://en.wikipedia.org/wiki/Absolute_difference)
between values of any two nodes.

**Example:**
    
    
    
    **Input:**
    
       1
        \
         3
        /
       2
    
    **Output:**
    1
    
    **Explanation:**
    The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

**Note:** There are at least two nodes in this BST.

## 题解

题意为找任意两个节点间绝对值差的最小值，根据二叉搜索树的特性，中序遍历即得有序数组，找出相邻两数的最小差值即为解。

### Java - Recursive

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    private int min = Integer.MAX_VALUE;
    private TreeNode prev = null;

    public int getMinimumDifference(TreeNode root) {
        if (root == null) return min;

        getMinimumDifference(root.left);
        if (prev != null) {
            min = Math.min(min, root.val - prev.val);
        }
        prev = root;
        getMinimumDifference(root.right);
        return min;
    }
}
```

### Java - Iterative

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int getMinimumDifference(TreeNode root) {
        int min = Integer.MAX_VALUE;
        TreeNode prev = null;
        Deque<TreeNode> stack = new ArrayDeque<TreeNode>();

        while (root != null || (!stack.isEmpty())) {
            if (root != null) {
                stack.push(root);
                root = root.left;
            } else {
                root = stack.pop();
                if (prev != null) {
                    min = Math.min(min, root.val - prev.val);
                }
                prev = root;
                root = root.right;
            }
        }

        return min;
    }
}
```

### 源码分析

递归的解法中需要特别注意 min 和 prev 的设定，作为参数传入均不太妥当。由于二叉搜索树的特性，求得最小差值时无需判断绝对值。

### 复杂度分析

递归实现用了隐式栈，迭代实现用了显式栈，最坏情况下栈的大小均为节点总数，平均情况下为树的高度。故平均情况下空间复杂度为 $$O(\log n)$$, 每个节点被访问一次，时间复杂度为 $$O(n)$$.

## Reference

- [Two Solutions, in-order traversal and a more general way using TreeSet](https://discuss.leetcode.com/topic/80823/two-solutions-in-order-traversal-and-a-more-general-way-using-treeset/8)