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

## 題解1 - Recursive

二元樹的題用遞迴的思想求解自然是最容易的，此題要求爲交換左右子節點，故遞迴交換即可。具體實現可分返回值爲`NULL`或者二元樹節點兩種情況，返回值爲節點的情況理解起來相對不那麼直觀一些。

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
        swap(root->left, root->right);
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

### 源碼分析

分三塊實現，首先是節點爲空的情況，然後交換左右節點，最後遞迴調用，遞迴調用的正確性可通過畫圖理解。

### 複雜度分析

每個節點遍歷一次，時間複雜度爲 $$O(n)$$, 使用了臨時變數，空間複雜度爲 $$O(1)$$.

## 題解2 - Iterative

遞迴的實現非常簡單，那麼非遞迴的如何實現呢？如果將遞迴改寫成 stack 的實現，那麼簡單來講就需要兩個 stack 了，稍顯複雜。其實仔細觀察此題可發現使用 level-order 的遍歷次序也可實現。即從根節點開始進入隊列 queue，交換左右節點，並將非空的左右子節點進入隊列，從隊列中取出節點，交換之，直至隊列爲空。

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

### 源碼分析

交換左右指針後需要判斷子節點是否非空，僅入隊非空子節點。

### 複雜度分析

遍歷每一個節點，時間複雜度爲 $$O(n)$$, 使用了隊列，最多存儲最下一層子節點數目，最多只有總節點數的一半，故最壞情況下 $$O(n)$$.

## Reference

- [0ms C++ Recursive/Iterative Solutions with Explanations - Leetcode Discuss](https://leetcode.com/discuss/42613/0ms-c-recursive-iterative-solutions-with-explanations)
