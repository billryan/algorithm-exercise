# Binary Tree Level Order Traversal II

## Question

- leetcode: [Binary Tree Level Order Traversal II | LeetCode OJ](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)
- lintcode: [(70) Binary Tree Level Order Traversal II](http://www.lintcode.com/en/problem/binary-tree-level-order-traversal-ii/)

```
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

Example
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7


return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
```

## 题解

此题在普通的 BFS 基础上增加了逆序输出，简单的实现可以使用辅助栈或者最后对结果逆序。

### Java - Stack

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
     * @return: buttom-up level order a list of lists of integer
     */
    public ArrayList<ArrayList<Integer>> levelOrderBottom(TreeNode root) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if (root == null) return result;

        Stack<ArrayList<Integer>> s = new Stack<ArrayList<Integer>>();
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        while (!q.isEmpty()) {
            int qLen = q.size();
            ArrayList<Integer> aList = new ArrayList<Integer>();
            for (int i = 0; i < qLen; i++) {
                TreeNode node = q.poll();
                aList.add(node.val);
                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);
            }
            s.push(aList);
        }

        while (!s.empty()) {
            result.add(s.pop());
        }
        return result;
    }
}
```

### Java - Reverse

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
     * @return: buttom-up level order a list of lists of integer
     */
    public ArrayList<ArrayList<Integer>> levelOrderBottom(TreeNode root) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if (root == null) return result;

        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        while (!q.isEmpty()) {
            int qLen = q.size();
            ArrayList<Integer> aList = new ArrayList<Integer>();
            for (int i = 0; i < qLen; i++) {
                TreeNode node = q.poll();
                aList.add(node.val);
                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);
            }
            result.add(aList);
        }

        Collections.reverse(result);
        return result;
    }
}
```

### 源码分析

Java 中 Queue 是接口，通常可用 LinkedList 实例化。

### 复杂度分析

时间复杂度为 $$O(n)$$, 使用了队列或者辅助栈作为辅助空间，空间复杂度为 $$O(n)$$.
