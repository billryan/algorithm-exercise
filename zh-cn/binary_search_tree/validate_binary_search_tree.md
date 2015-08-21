# Validate Binary Search Tree

## Source

- lintcode: [(95) Validate Binary Search Tree](http://www.lintcode.com/en/problem/validate-binary-search-tree/)

```
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example
An example:

   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".
```

## 题解1 - 递归(比较左右子节点的`key`)

按照题中对二叉搜索树所给的定义递归判断，我们从递归的两个步骤出发分析：
1. 基本条件/终止条件 - 返回值需斟酌。
2. 递归步/条件递归 - 能使原始问题收敛。

终止条件好确定——当前节点为空，或者不符合二叉搜索树的定义，返回值分别是什么呢？先别急，分析下递归步试试先。递归步的核心步骤为比较当前节点的`key`和左右子节点的`key`大小，和定义不符则返回`false`, 否则递归处理。从这里可以看出在节点为空时应返回`true`, 由上层的其他条件判断。

### C++ Recursion(naive implementation)

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
        if (NULL == root) {
            return true;
        }

        if (NULL == root->left) {
            if ((NULL != root->right) && (root->val >= root->right->val)) {
                return false;
            } else {
                return isValidBST(root->right);
            }
        }

        if (NULL == root->right) {
            if ((NULL != root->left) && (root->val <= root->left->val)) {
                return false;
            } else {
                return isValidBST(root->left);
            }
        }

        if ((root->val > root->left->val) && (root->val < root->right->val)) {
            return isValidBST(root->left) && isValidBST(root->right);
        } else {
            return false;
        }
    }
};
```

### 源码分析

这种递归方法虽然非常直观，但是需要处理节点指针值为空的边界条件，否则在进行取值操作时会产生运行时错误，这些边界处理使得代码看起来十分不雅观。那么有没有什么优雅的方式处理这种情况呢？还真有，下面就来介绍一种不错的思路。

## 题解2 - 递归(引入极值简化代码)

对于如何处理复杂边界条件，目前我所知的有两种有效的方法：
1. 引入`dummy node`，这个对于链表头不确定时特别有效。
2. 引入`INT_MAX`, `INT_MIN`等最大/最小值，对于比较类问题很有效(需要考虑到本身值就为最值，这种情况一般极少见)。

显然，对于这个问题，`dummy node`是不太适用，我们来探讨下取最值的可能性。从以上代码可知边界处理的关键在于需要判断`root->left`和`root-right`是否为`NULL`, `key`的比较则相对固定，分别为`root->left->val`和`root->right->val`, 由此我们自然可以联想到可以使用`left_val`和`right_val`对左右子树的`key`进行「包装」，在子节点与根节点的`key`进行比较之前对`left_val`和`right_val`赋值即可（这一思想在 lintcode: [(65) Median of two Sorted Arrays](http://www.lintcode.com/en/problem/median-of-two-sorted-arrays/) 和 lintcode: [(93) Balanced Binary Tree](http://www.lintcode.com/en/problem/balanced-binary-tree/) 中也有使用）。

### C++ Recursion(wrapper for root->*->val)

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
        if (NULL == root) {
            return true;
        }

        // wrap key root->left->val, LONG_MIN for true
        long int left_val = (NULL == root->left ? LONG_MIN : root->left->val);
        // wrap key root->right->val, LONG_MAX for true
        long int right_val = (NULL == root->right ? LONG_MAX : root->right->val);

        if ((root->val > left_val) && (root->val < right_val)) {
            return isValidBST(root->left) && isValidBST(root->right);
        } else {
            return false;
        }
    }
};
```

### 源码分析

根据题解部分的分析，我们使用`left_val`「包装」比较`key`时要用到的`root->left->val`, 当`root->left`为空时我们置`left_val`为最小值，保证返回结果为`true`——也就是不影响原来的结果；对`right_val`的分析也是同理可得。由于我们使用了`left_val`对原来的子节点值进行了「包装」，故在比较`key`大小时使用`root->val > left_val`是有一丁点bug的，因为有可能出现`root->val == LONG_MIN`，这种极端测试用例面试中自己心里有数就好了。

后记：使用了「包装」的方法虽然简化了代码明晰了思路，但是在测试用例中如果出现较多的空节点时，朴素版的代码运行效率会高一些。嗯，不要仅仅只为了代码的优雅而忽略了运行时的效率！

## 题解3 - 迭代(使用栈改写递推)

看过了上述递归版的思路，客官要不要来一碗迭代版的清酒？理论上来讲，任何递归版的程序都可以用迭代实现，当然「理论上来讲」一般也就意味着这玩意儿我们远远地看着她就好，可远观而不可亵玩焉... 不卖关子了，我们挑一个简单的递归版程序来试试，嗯，就是上题包装过的递归程序。

函数的每一次递归调用都相当于是一次入栈操作，返回结果则相当于是一次出栈操作。顺着这个思路我们使用一个栈来压入当前节点的左右子节点，入栈前比较其是否符合定义。

### C++ Iteration(using stack)

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
        if (NULL == root) {
            return true;
        }

        stack<TreeNode *> s;
        s.push(root);
        while (!s.empty()) {
            TreeNode *node = s.top();
            s.pop();

            // wrap the value of node->left->val
            long int left_val = (NULL == node->left ? LONG_MIN : node->left->val);
            // wrap the value of node->right->val
            long int right_val = (NULL == node->right ? LONG_MAX : node->right->val);

            if ((node->val > left_val) && (node->val < right_val)) {
                if (NULL != node->right) {
                    s.push(node->right);
                }
                if (NULL != node->left) {
                    s.push(node->left);
                }
            } else {
                return false;
            }
        }

        return true;
    }
};
```

## 题解4 - 迭代(使用栈)

从题解3的迭代程序来看这道题似乎可以很方便地直接使用栈解决之。我们来看看迭代的直接思路，压入当前节点的非空子节点的同时判断其是否符合题目所给定义，直至栈为空——所有节点均已处理完。

### C++ Iteration

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
        if (NULL == root) {
            return true;
        }

        stack<TreeNode *> s;
        s.push(root);
        while (!s.empty()) {
            TreeNode *node = s.top();
            s.pop();
            
            // compare the right node
            if (NULL != node->right) {
                if (node->val < node->right->val) {
                    s.push(node->right);
                } else {
                    return false;
                }
            } // end if (NULL...)

            // compare the left node
            if (NULL != node->left) {
                if (node->val > node->left->val) {
                    s.push(node->left);
                } else {
                    return false;
                }
            } // end if (NULL...)
        }

        return true;
    }
};
```

## Reference

- [LeetCode: Validate Binary Search Tree 解题报告 - Yu's Garden - 博客园](http://www.cnblogs.com/yuzhangcmu/p/4177047.html) - 提供了4种不同的方法，思路可以参考。
