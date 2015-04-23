# Binary Tree Preorder Traversal - 前序遍历


## Source

- lintcode: [(66) Binary Tree Preorder Traversal](http://www.lintcode.com/en/problem/binary-tree-preorder-traversal/)


```
Given a binary tree, return the preorder traversal of its nodes' values.

Note
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3


return [1,2,3].

Example
Challenge
Can you do it without recursion?
```

### 题解 - 递归

**面试时不推荐递归这种做法。**

递归版很好理解，首先判断当前节点(根节点)是否为`null`，是则返回空vector，否则先返回当前节点的值，然后对当前节点的左节点递归，最后对当前节点的右节点递归。递归时对结果的处理方式不同可进一步细分为遍历和分治两种方法。

#### C++ Traverse - 递归遍历

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
     * @return: Preorder in vector which contains node values.
     */
    vector<int> preorderTraversal(TreeNode *root) {
        vector<int> val_vec;
        traverse(root, val_vec);

        return val_vec;
    }

private:
    void traverse(TreeNode *root, vector<int> &ret) {
        if (root == NULL) {
            return;
        }

        ret.push_back(root->val);
        traverse(root->left, ret);
        traverse(root->right, ret);
    }
};
```

#### 源码分析

使用了辅助递归函数`traverse`，传值时注意应使用`vector`的引用。

### 题解 - 分治

使用分治的方法和递归类似，但是不同的是递归是将结果作为参数传入递归函数中，而分治则是先将结果保留，随后再合并到最终结果中。

#### C++ Divide and Conquer

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
     * @return: Preorder in vector which contains node values.
     */
    vector<int> preorderTraversal(TreeNode *root) {
        vector<int> val_vec;

        // NULL or leaf(叶子节点)
        if (root == NULL) {
            return val_vec;
        }

        // Divide (分)
        vector<int> left = preorderTraversal(root->left);
        vector<int> right = preorderTraversal(root->right);

        // Conquer (治)
        val_vec.push_back(root->val);
        val_vec.insert(val_vec.end(), left.begin(), left.end());
        val_vec.insert(val_vec.end(), right.begin(), right.end());

        return val_vec;
    }
};
```

#### 源码分析

由于是使用vector, 将新的vector插入另一vector不能再使用push_back, 而应该使用insert。

### 题解 - 迭代

迭代时需要利用栈来保存遍历到的节点，首先进行出栈抛出当前节点，保存当前节点的值，随后将右、左节点分别入栈，迭代到其为叶子节点(NULL)为止。

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
public:
    /**
     * @param root: The root of binary tree.
     * @return: Preorder in vector which contains node values.
     */
    vector<int> preorderTraversal(TreeNode *root) {
        vector<int> val_vec;
        stack<const TreeNode *> s;

        if (root == NULL) {
            return val_vec;
        }

        s.push(root);
        while (!s.empty()) {
            const TreeNode *node = s.top();
            s.pop();

            val_vec.push_back(node->val);

            if (node->right != NULL) {
                s.push(node->right);
            }
            if (node->left != NULL) {
                s.push(node->left);
            }
        }

        return val_vec;
    }
};
```

#### 源码分析

1. 对root进行异常处理
2. 将root压入栈
3. 循环终止条件为栈s为空，所有元素均已处理完
4. 访问当前栈顶元素(首先取出栈顶元素，随后pop掉栈顶元素)并存入最终结果
5. 将右、左节点分别压入栈内，以便取元素时为先左后右。
6. 返回最终结果

其中步骤4,5,6为迭代的核心，对应前序遍历「根左右」。

所以说到底，**使用迭代，只不过是另外一种形式的递归。**使用递归的思想去理解遍历问题会容易理解许多。
