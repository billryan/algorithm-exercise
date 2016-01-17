# Balanced Binary Tree

## Question

- leetcode: [Balanced Binary Tree | LeetCode OJ](https://leetcode.com/problems/balanced-binary-tree/)
- lintcode: [(93) Balanced Binary Tree](http://www.lintcode.com/en/problem/balanced-binary-tree/)

### Problem Statement

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

#### Example

Given binary tree A=`{3,9,20,#,#,15,7}`, B=`{3,#,20,15,7}`

```
A)  3            B)    3 
   / \                  \
  9  20                 20
    /  \                / \
   15   7              15  7
```

The binary tree A is a height-balanced binary tree, but B is not.

## 题解1 - 递归

根据题意，平衡树的定义是两子树的深度差最大不超过1，显然使用递归进行分析较为方便。既然使用递归，那么接下来就需要分析递归调用的终止条件。和之前的 [Maximum Depth of Binary Tree | Algorithm](http://algorithm.yuanbin.me/zh-hans/binary_tree/maximum_depth_of_binary_tree.html) 类似，`NULL == root`必然是其中一个终止条件，返回`0`；根据题意还需的另一终止条件应为「左右子树高度差大于1」，但对应此终止条件的返回值是多少？——`INT_MAX` or `INT_MIN`？想想都不合适，为何不在传入参数中传入`bool`指针或者`bool`引用咧？并以此变量作为最终返回值，此法看似可行，先来看看鄙人最开始想到的这种方法。

### C++ Recursion with extra bool variable

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
     * @return: True if this Binary tree is Balanced, or false.
     */
    bool isBalanced(TreeNode *root) {
        if (NULL == root) {
            return true;
        }

        bool result = true;
        maxDepth(root, result);

        return result;
    }

private:
    int maxDepth(TreeNode *root, bool &isBalanced) {
        if (NULL == root) {
            return 0;
        }

        int leftDepth = maxDepth(root->left, isBalanced);
        int rightDepth = maxDepth(root->right, isBalanced);
        if (abs(leftDepth - rightDepth) > 1) {
            isBalanced = false;
            // speed up the recursion process
            return INT_MAX;
        }

        return max(leftDepth, rightDepth) + 1;
    }
};
```

#### 源码解析

如果在某一次子树高度差大于1时，返回`INT_MAX`以减少不必要的计算过程，加速整个递归调用的过程。

初看起来上述代码好像还不错的样子，但是在看了九章的实现后，瞬间觉得自己弱爆了... 首先可以确定`abs(leftDepth - rightDepth) > 1`肯定是需要特殊处理的，如果返回`-1`呢？咋一看似乎在下一步返回`max(leftDepth, rightDepth) + 1`时会出错，再进一步想想，我们能否不让`max...`这一句执行呢？如果返回了`-1`，其接盘侠必然是`leftDepth`或者`rightDepth`中的一个，因此我们只需要在判断子树高度差大于1的同时也判断下左右子树深度是否为`-1`即可都返回`-1`，不得不说这种处理方法要精妙的多，赞！

### C++

```c++
/**
 * forked from http://www.jiuzhang.com/solutions/balanced-binary-tree/
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
     * @return: True if this Binary tree is Balanced, or false.
     */
    bool isBalanced(TreeNode *root) {
        return (-1 != maxDepth(root));
    }

private:
    int maxDepth(TreeNode *root) {
        if (NULL == root) {
            return 0;
        }

        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        if (leftDepth == -1 || rightDepth == -1 || \
            abs(leftDepth - rightDepth) > 1) {
            return -1;
        }

        return max(leftDepth, rightDepth) + 1;
    }
};
```

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
    public boolean isBalanced(TreeNode root) {
        return maxDepth(root) != -1;
    }
    
    private int maxDepth(TreeNode root) {
        if (root == null) return 0;
        
        int leftDepth = maxDepth(root.left);
        int rightDepth = maxDepth(root.right);
        if (leftDepth == -1 || rightDepth == -1 ||
            Math.abs(leftDepth - rightDepth) > 1) {
            
            return -1;
        }
        
        return 1 + Math.max(leftDepth, rightDepth);
    }
}
```

### 源码分析

抓住两个核心：子树的高度以及高度之差，返回值应该包含这两种信息。

### 复杂度分析

遍历所有节点各一次，时间复杂度为 $$O(n)$$, 使用了部分辅助变量，空间复杂度 $$O(1)$$.
