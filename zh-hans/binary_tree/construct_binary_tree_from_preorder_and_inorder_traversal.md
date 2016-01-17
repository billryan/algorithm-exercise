# Construct Binary Tree from Preorder and Inorder Traversal

## Question

- leetcode: [Construct Binary Tree from Preorder and Inorder Traversal | LeetCode OJ](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
- lintcode: [(73) Construct Binary Tree from Preorder and Inorder Traversal](http://www.lintcode.com/en/problem/construct-binary-tree-from-preorder-and-inorder-traversal/)

```
Given preorder and inorder traversal of a tree, construct the binary tree.

Example
Given in-order [1,2,3] and pre-order [2,1,3], return a tree:
  2
 / \
1   3
Note
You may assume that duplicates do not exist in the tree.
```

## 题解

二叉树的重建，典型题。核心有两点：
1. preorder 先序遍历的第一个节点即为根节点。
2. 确定 inorder 数组中的根节点后其左子树和右子树也是 preorder 的左子树和右子树。

其中第二点是隐含条件，数组中没有重复元素，故可以根据先序遍历中第一个元素（根节点）得到根节点的值，然后在 inorder 中序遍历的数组中搜索得到根节点的索引值，即为左子树，右边为右子树。根据中序遍历中左子树的索引确定先序遍历数组中左子树的起止索引。递归直至处理完所有数组元素。

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
     *@param preorder : A list of integers that preorder traversal of a tree
     *@param inorder : A list of integers that inorder traversal of a tree
     *@return : Root of a tree
     */
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder == null || inorder == null) return null;
        if (preorder.length == 0 || inorder.length == 0) return null;
        if (preorder.length != inorder.length) return null;

        TreeNode root = helper(preorder, 0, preorder.length - 1,
                               inorder, 0, inorder.length - 1);
        return root;
    }

    private TreeNode helper(int[] preorder, int prestart, int preend,
                            int[] inorder, int instart, int inend) {
        // corner cases
        if (prestart > preend || instart > inend) return null;
        // build root TreeNode
        int root_val = preorder[prestart];
        TreeNode root = new TreeNode(root_val);
        // find index of root_val in inorder[]
        int index = findIndex(inorder, instart, inend, root_val);
        // build left subtree
        root.left = helper(preorder, prestart + 1, prestart + index - instart,
               inorder, instart, index - 1);
        // build right subtree
        root.right = helper(preorder, prestart + index - instart + 1, preend,
               inorder, index + 1, inend);
        return root;
    }

    private int findIndex(int[] nums, int start, int end, int target) {
        for (int i = start; i <= end; i++) {
            if (nums[i] == target) return i;
        }
        return -1;
    }
}
```

### 源码分析

由于需要知道左右子树在数组中的索引，故需要引入辅助方法。找根节点这个大家都能很容易地想到，但是最关键的一步——找出左右子树的起止索引，这一点就不那么直接了，老实说想了很久忽略了这个突破点。

### 复杂度分析

`findIndex` 时间复杂度近似 $$O(n)$$, `helper` 递归调用，每次调用都需要找中序遍历数组中的根节点，故总的时间复杂度为 $$O(n^2)$$. 原地生成最终二叉树，空间复杂度为 $$O(1)$$.

## Reference

- [Construct Binary Tree from Preorder and Inorder Traversal 参考程序 Java/C++/Python](http://www.jiuzhang.com/solutions/construct-binary-tree-from-preorder-and-inorder-traversal/)
