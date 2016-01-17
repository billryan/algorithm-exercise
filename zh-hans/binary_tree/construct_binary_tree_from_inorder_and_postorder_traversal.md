# Construct Binary Tree from Inorder and Postorder Traversal

## Question

- lintcode: [(72) Construct Binary Tree from Inorder and Postorder Traversal](http://www.lintcode.com/en/problem/construct-binary-tree-from-inorder-and-postorder-traversal/)

```
Given inorder and postorder traversal of a tree, construct the binary tree.

Example
Given inorder [1,2,3] and postorder [1,3,2], return a tree:
  2
   / \
   1   3
   Note
   You may assume that duplicates do not exist in the tree.
```

## 题解

和题 [Construct Binary Tree from Preorder and Inorder Traversal](http://algorithm.yuanbin.me/zh-hans/binary_tree/construct_binary_tree_from_preorder_and_inorder_traversal.html) 几乎一致，关键在于找到中序遍历中的根节点和左右子树，递归解决。

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
     *@param inorder : A list of integers that inorder traversal of a tree
     *@param postorder : A list of integers that postorder traversal of a tree
     *@return : Root of a tree
     */
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if (inorder == null || postorder == null) return null;
        if (inorder.length == 0 || postorder.length == 0) return null;
        if (inorder.length != postorder.length) return null;

        TreeNode root = helper(inorder, 0, inorder.length - 1,
               postorder, 0, postorder.length - 1);
        return root;
    }

    private TreeNode helper(int[] inorder, int instart, int inend,
                            int[] postorder, int poststart, int postend) {
        // corner cases
        if (instart > inend || poststart > postend) return null;

        // build root TreeNode
        int root_val = postorder[postend];
        TreeNode root = new TreeNode(root_val);
        // find index of root_val in inorder[]
        int index = findIndex(inorder, instart, inend, root_val);
        // build left subtree
        root.left = helper(inorder, instart, index - 1,
                           postorder, poststart, poststart + index - instart - 1);
        // build right subtree
        root.right = helper(inorder, index + 1, inend,
                           postorder, poststart + index - instart, postend - 1);
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

找根节点的方法作为私有方法，辅助函数需要注意索引范围。

### 复杂度分析

找根节点近似 $$O(n)$$, 递归遍历整个数组，嵌套找根节点的方法，故总的时间复杂度为 $$O(n^2)$$.
