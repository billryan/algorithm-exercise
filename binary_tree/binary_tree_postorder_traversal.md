# Binary Tree Postorder Traversal

Question: [(68) Binary Tree Postorder Traversal](http://www.lintcode.com/en/problem/binary-tree-postorder-traversal/)

```
Given a binary tree, return the postorder traversal of its nodes' values.

Example
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3


return [3,2,1].

Challenge
Can you do it without recursion?
```

### 题解 - 递归

首先使用递归便于理解。

#### C++ Recursion

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
    /**
     * @param root: The root of binary tree.
     * @return: Postorder in vector which contains node values.
     */
public:
    vector<int> postorderTraversal(TreeNode *root) {
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
        traverse(root->right, ret);
        ret.push_back(root->val);
    }
};
```

### 题解 - 迭代

使用递归写后序遍历那是相当的简单，我们来个不使用递归的迭代版。整体思路仍然为「左右根」，由于是最后才将元素取出。因此需要区分左右的访问记录。

#### C++ Iteration

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
    /**
     * @param root: The root of binary tree.
     * @return: Postorder in vector which contains node values.
     */
public:
    vector<int> postorderTraversal(TreeNode *root) {
        vector<int> result;
        const TreeNode *prevNode = NULL;
        const TreeNode *currNode = root;
        stack<const TreeNode *> s;

        if (root == NULL) {
            return result;
        }

        s.push(root);
        while (!s.empty()) {
            currNode = s.top();
            if (prevNode == NULL || prevNode->left == currNode || prevNode->right == currNode) {
                // traverse down the tree (left first)
                if (currNode->left) {
                    s.push(currNode->left);
                } else if (currNode->right) {
                    s.push(currNode->right);
                }
            } else if (currNode->left == prevNode) {
                // traverse up the tree from the left to right
                // the left node has been visited
                if (currNode->right) {
                    s.push(currNode->right);
                }
            } else {
                // traverse up the tree from the right
                // visit current node
                result.push_back(currNode->val);
                s.pop();
            }

            prevNode = currNode;
        }

        return result;
    }
};
```

#### 源码解析

使用`prevNode`记录之前的访问节点，`currNode`记录目前正在访问/操作的节点。每次进入while循环时给`currNode`赋值，结束时`prevNode = currNode`.

**将递归写成迭代的难点在于如何在迭代中体现递归本质及边界条件的确立。**
