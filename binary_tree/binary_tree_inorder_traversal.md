# Binary Tree Inorder Traversal

Question: [(67) Binary Tree Inorder Traversal](http://www.lintcode.com/en/problem/binary-tree-inorder-traversal/)

```
Given a binary tree, return the inorder traversal of its nodes' values.

Example
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3


return [1,3,2].

Challenge
Can you do it without recursion?
```

## Iteration - 迭代版

题解：

使用辅助栈，空间复杂度 $$O(n)$$, 时间复杂度 $$O(n)$$.

中序遍历没有前序遍历好写，其中之一就在于入栈出栈的顺序和限制规则。我们采用「左根右」的访问顺序可知主要有如下三步构成。

1. 首先需要一直对左子树迭代并将非空节点入栈
2. 节点指针为空后不再入栈
3. 当前节点为空时进行出栈操作，并访问栈顶节点
4. 将当前指针p用其右子节点替代

步骤2,3,4对应「左根右」的遍历结构，只是此时的步骤2取的左值为空。

**C++**
```
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
    /**
     * @param root: The root of binary tree.
     * @return: Inorder in vector which contains node values.
     */
public:
    vector<int> inorderTraversal(TreeNode *root) {
        vector<int> result;
        const TreeNode *node = root;
        stack<const TreeNode *> s;

        while (!s.empty() || node != NULL) {
            if (node != NULL) {
                // iterate through the left
                s.push(node);
                node = node->left;
            } else {
                // visit current TreeNode
                node = s.top();
                s.pop();
                result.push_back(node->val);
                // node->left is NULL, iterate for node->right
                node = node->right;
            }
        }

        return result;
    }
};
```

## Recursion - 递归版

题解：

递归版最好理解，递归调用时注意返回值和递归左右子树的顺序即可。

**C++**
```
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
    /**
     * @param root: The root of binary tree.
     * @return: Inorder in vector which contains node values.
     */
public:
    vector<int> inorderTraversal(TreeNode *root) {
        vector<int> result;

        traverse(root, result);

        return result;
    }

private:
    void traverse(TreeNode *root, vector<int> &ret) {
        if (root == NULL) {
            return;
        }

        traverse(root->left, ret);
        ret.push_back(root->val);
        traverse(root->right, ret);
    }
};
```
