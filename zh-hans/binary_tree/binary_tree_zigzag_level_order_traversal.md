# Binary Tree Zigzag Level Order Traversal

## Question

- leetcode: [Binary Tree Zigzag Level Order Traversal | LeetCode OJ](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)
- lintcode: [(71) Binary Tree Zigzag Level Order Traversal](http://www.lintcode.com/en/problem/binary-tree-zigzag-level-order-traversal/)

```
Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

Example
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7


return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]
```

## 题解1 - 队列

二叉树的广度优先遍历使用队列非常容易实现，这道题要求的是蛇形遍历，我们可以发现奇数行的遍历仍然可以按照广度优先遍历的方式实现，而对于偶数行，只要翻转一下就好了。

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
     * @return: A list of lists of integer include
     *          the zigzag level order traversal of its nodes' values
     */
    public ArrayList<ArrayList<Integer>> zigzagLevelOrder(TreeNode root) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if (root == null) return result;

        boolean odd = true;
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        while (!q.isEmpty()) {
            // level traversal
            int qLen = q.size();
            ArrayList<Integer> level = new ArrayList<Integer>();
            for (int i = 0; i < qLen; i++) {
                TreeNode node = q.poll();
                level.add(node.val);
                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);
            }
            // add level order reverse for even
            if (odd) {
                result.add(level);
            } else {
                Collections.reverse(level);
                result.add(level);
            }
            // flip odd and even
            odd = !odd;
        }

        return result;
    }
}
```

### 源码分析

区分奇数偶数行使用额外变量。

### 复杂度分析

需要 reverse 的节点数目近似为 n/2, 故时间复杂度 $$O(n)$$. 最下层节点数目最多 n/2, 故reverse 操作的空间复杂度可近似为 $$O(n/2)$$.

总的时间复杂度为 $$O(n)$$, 空间复杂度也为 $$O(n)$$.

## Reference

- [Binary Tree Zigzag Level Order Traversal 参考程序 Java/C++/Python](http://www.jiuzhang.com/solutions/binary-tree-zigzag-level-order-traversal/)
- [Printing a Binary Tree in Zig Zag Level-Order | LeetCode](http://articles.leetcode.com/2010/09/printing-binary-tree-in-zig-zag-level_18.html)
