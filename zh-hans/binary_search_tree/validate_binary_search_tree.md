# Validate Binary Search Tree

**TAGS:** TAG_Divide_and_Conquer TAG_Recursion TAG_Binary_Search_Tree TAG_Binary_Tree TAG_Medium

## Question

- leetcode: [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- lintcode: [Validate Binary Search Tree](http://www.lintcode.com/en/problem/validate-binary-search-tree/)

### Problem Statement

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

  * The left subtree of a node contains only nodes with keys **less than** the node's key.
  * The right subtree of a node contains only nodes with keys **greater than** the node's key.
  * Both the left and right subtrees must also be binary search trees.
  * A single node tree is a BST

**Example**

An example:

    
      2
     / \
    1   4
       / \
      3   5
    

The above binary tree is serialized as `{2,1,4,#,#,3,5}` (in level order).

## 题解1 - recursion

按照题中对二叉搜索树所给的定义递归判断，我们从递归的两个步骤出发分析：
1. 基本条件/终止条件 - 返回值需斟酌。
2. 递归步/条件递归 - 能使原始问题收敛。

终止条件好确定——当前节点为空，或者不符合二叉搜索树的定义，返回值分别是什么呢？先别急，分析下递归步试试先。递归步的核心步骤为比较当前节点的`key`和左右子节点的`key`大小，和定义不符则返回`false`, 否则递归处理。从这里可以看出在节点为空时应返回`true`, 由上层的其他条件判断。但需要注意的是这里不仅要考虑根节点与当前的左右子节点，**还需要考虑左子树中父节点的最小值和右子树中父节点的最大值。**否则程序在`[10,5,15,#,#,6,20]` 这种 case 误判。

由于不仅需要考虑当前父节点，还需要考虑父节点的父节点... 故递归时需要引入上界和下界值。画图分析可知对于左子树我们需要比较父节点中最小值，对于右子树则是父节点中的最大值。又由于满足二叉搜索树的定义时，左子结点的值一定小于根节点，右子节点的值一定大于根节点，故无需比较所有父节点的值，使用递推即可得上界与下界，这里的实现非常巧妙。

### C++ - long long

```c++
/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */
class Solution {
public:
    /**
     * @param root: The root of binary tree.
     * @return: True if the binary tree is BST, or false
     */
    bool isValidBST(TreeNode *root) {
        if (root == NULL) return true;

        return helper(root, LLONG_MIN, LLONG_MAX);
    }

    bool helper(TreeNode *root, long long lower, long long upper) {
        if (root == NULL) return true;

        if (root->val <= lower || root->val >= upper) return false;
        bool isLeftValidBST = helper(root->left, lower, root->val);
        bool isRightValidBST = helper(root->right, root->val, upper);

        return isLeftValidBST && isRightValidBST;
    }
};
```

### C++ - without long long

```c++
/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */
class Solution {
public:
    /**
     * @param root: The root of binary tree.
     * @return: True if the binary tree is BST, or false
     */
    bool isValidBST(TreeNode *root) {
        if (root == NULL) return true;

        return helper(root, INT_MIN, INT_MAX);
    }

    bool helper(TreeNode *root, int lower, int upper) {
        if (root == NULL) return true;

        if (root->val <= lower || root->val >= upper) {
            bool right_max = root->val == INT_MAX && root->right == NULL;
            bool left_min = root->val == INT_MIN && root->left == NULL;
            if (!(right_max || left_min)) {
                return false;
            }
        }
        bool isLeftValidBST = helper(root->left, lower, root->val);
        bool isRightValidBST = helper(root->right, root->val, upper);

        return isLeftValidBST && isRightValidBST;
    }
};
```

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
     * @return: True if the binary tree is BST, or false
     */
    public boolean isValidBST(TreeNode root) {
        if (root == null) return true;

        return helper(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean helper(TreeNode root, long lower, long upper) {
        if (root == null) return true;
        // System.out.println("root.val = " + root.val + ", lower = " + lower + ", upper = " + upper);
        // left node value < root node value < right node value
        if (root.val >= upper || root.val <= lower) return false;
        boolean isLeftValidBST = helper(root.left, lower, root.val);
        boolean isRightValidBST = helper(root.right, root.val, upper);

        return isLeftValidBST && isRightValidBST;
    }
}
```

### 源码分析

为避免节点中出现整型的最大最小值，引入 long 型进行比较。有些 BST 的定义允许左子结点的值与根节点相同，此时需要更改比较条件为`root.val > upper`. C++ 中 long 可能与 int 范围相同，故使用 long long. 如果不使用比 int 型更大的类型，那么就需要在相等时多加一些判断。

### 复杂度分析

递归遍历所有节点，时间复杂度为 $$O(n)$$, 使用了部分额外空间，空间复杂度为 $$O(1)$$.

## 题解2 - iteration

联想到二叉树的中序遍历。

### Java

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
    public boolean isValidBST(TreeNode root) {
        Deque<TreeNode> st = new ArrayDeque<>();
        long pre = Long.MIN_VALUE;
        // inorder traverse
        while (root != null || !st.isEmpty()) {
            if (root != null) {
                st.push(root);
                root = root.left;
            }
            else {
                root = st.pop();
                if (root.val > pre)
                    pre = root.val;
                else
                    return false;
                root = root.right;
            }
        }
        return true;
    }
}
```

## Reference

- [LeetCode: Validate Binary Search Tree 解题报告 - Yu's Garden - 博客园](http://www.cnblogs.com/yuzhangcmu/p/4177047.html) - 提供了4种不同的方法，思路可以参考。
