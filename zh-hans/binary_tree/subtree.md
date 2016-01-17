# Subtree

## Question

- lintcode: [(245) Subtree](http://www.lintcode.com/en/problem/subtree/#)

```
You have two every large binary trees: T1,
with millions of nodes, and T2, with hundreds of nodes.
Create an algorithm to decide if T2 is a subtree of T1.

Example
T2 is a subtree of T1 in the following case:
       1                3
      / \              /
T1 = 2   3      T2 =  4
        /
       4
T2 isn't a subtree of T1 in the following case:
       1               3
      / \               \
T1 = 2   3       T2 =    4
        /
       4
Note
A tree T2 is a subtree of T1 if there exists a node n in T1 such that
the subtree of n is identical to T2.
That is, if you cut off the tree at node n,
the two trees would be identical.
```

## 题解

判断 T2是否是 T1的子树，首先应该在 T1中找到 T2的根节点，找到根节点后两棵子树必须完全相同。所以整个思路分为两步走：找根节点，判断两棵树是否全等。咋看起来极其简单，但实际实现中还是比较精妙的，尤其是递归的先后顺序及条件与条件或的处理。

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
     * @param T1, T2: The roots of binary tree.
     * @return: True if T2 is a subtree of T1, or false.
     */
    public boolean isSubtree(TreeNode T1, TreeNode T2) {
        if (T2 == null) return true;
        if (T1 == null) return false;
        return identical(T1, T2) || isSubtree(T1.left, T2) || isSubtree(T1.right, T2);
    }

    private boolean identical(TreeNode T1, TreeNode T2) {
        if (T1 == null && T2 == null) return true;
        if (T1 == null || T2 == null) return false;
        if (T1.val != T2.val) return false;
        return identical(T1.left, T2.left) && identical(T1.right, T2.right);
    }
}
```

### 源码分析

这道题的异常处理相对 trick 一点，需要理解 null 对子树的含义。另外需要先调用`identical`再递归调用`isSubtree`判断左右子树的情况。方法`identical`中调用`.val`前需要判断是否为 null, 而后递归调用判断左右子树是否 identical。

### 复杂度分析

identical 的调用，时间复杂度近似 $$O(n)$$, 查根节点的时间复杂度随机，平均为 $$O(m)$$, 故总的时间复杂度可近似为 $$O(mn)$$.

## Reference

- [LintCode: Subtree](http://cherylintcode.blogspot.com/2015/06/subtree.html)
