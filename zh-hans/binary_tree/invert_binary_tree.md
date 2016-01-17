# Invert Binary Tree

## Question

- leetcode: [Invert Binary Tree | LeetCode OJ](https://leetcode.com/problems/invert-binary-tree/)
- lintcode: [(175) Invert Binary Tree](http://www.lintcode.com/en/problem/invert-binary-tree/)

```
Invert a binary tree.

Example
  1         1
 / \       / \
2   3  => 3   2
   /       \
  4         4
Challenge
Do it in recursion is acceptable, can you do it without recursion?
```

## 题解1 - Recursive

二叉树的题用递归的思想求解自然是最容易的，此题要求为交换左右子节点，故递归交换之即可。具体实现可分返回值为空或者二叉树节点两种情况，返回值为节点的情况理解起来相对不那么直观一些。

### C++ - return void

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
 * };
 */
class Solution {
public:
    /**
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    void invertBinaryTree(TreeNode *root) {
        if (root == NULL) return;

        TreeNode *temp = root->left;
        root->left = root->right;
        root->right = temp;

        invertBinaryTree(root->left);
        invertBinaryTree(root->right);
    }
};
```

### C++ - return TreeNode *

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == NULL) return NULL;

        TreeNode *temp = root->left;
        root->left = invertTree(root->right);
        root->right = invertTree(temp);

        return root;
    }
};
```

### 源码分析

分三块实现，首先是节点为空的情况，然后使用临时变量交换左右节点，最后递归调用，递归调用的正确性可通过画图理解。

### 复杂度分析

每个节点遍历一次，时间复杂度为 $$O(n)$$, 使用了临时变量，空间复杂度为 $$O(1)$$.

## 题解2 - Iterative

递归的实现非常简单，那么非递归的如何实现呢？如果将递归改写成栈的实现，那么简单来讲就需要两个栈了，稍显复杂。其实仔细观察此题可发现使用 level-order 的遍历次序也可实现。即从根节点开始入队，交换左右节点，并将非空的左右子节点入队，从队列中取出节点，交换之，直至队列为空。

### C++

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
 * };
 */
class Solution {
public:
    /**
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    void invertBinaryTree(TreeNode *root) {
        if (root == NULL) return;

        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            // pop out the front node
            TreeNode *node = q.front();
            q.pop();
            // swap between left and right pointer
            swap(node->left, node->right);
            // push non-NULL node
            if (node->left != NULL) q.push(node->left);
            if (node->right != NULL) q.push(node->right);
        }
    }
};
```

### 源码分析

交换左右指针后需要判断子节点是否非空，仅入队非空子节点。

### 复杂度分析

遍历每一个节点，时间复杂度为 $$O(n)$$, 使用了队列，最多存储最下一层子节点数目，最多只有总节点数的一半，故最坏情况下 $$O(n)$$.

## Reference

- [0ms C++ Recursive/Iterative Solutions with Explanations - Leetcode Discuss](https://leetcode.com/discuss/42613/0ms-c-recursive-iterative-solutions-with-explanations)
