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

## 題解

這題在普通的 BFS 基礎上增加了逆序輸出，簡單的實現可以使用 Stack 或者最後對結果逆序。

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

### 源碼分析

Java 中 Queue 是接口，通常可用 LinkedList 實例化。

### 複雜度分析

時間複雜度爲 $$O(n)$$, 使用了 Queue 或者 Stack 作爲輔助空間，空間複雜度爲 $$O(n)$$.
