# Insert Node in a Binary Search Tree

## Question

- lintcode: [(85) Insert Node in a Binary Search Tree](http://www.lintcode.com/en/problem/insert-node-in-a-binary-search-tree/)

```
Given a binary search tree and a new tree node, insert the node into the tree. You should keep the tree still be a valid binary search tree.

Example
Given binary search tree as follow:

     2

  /    \

1        4

         /

       3

after Insert node 6, the tree should be:

     2

  /    \

1        4

         /   \

       3        6

Challenge
Do it without recursion
```

## 題解 - 遞迴

二元樹的題使用遞迴自然是最好理解的，程式碼也簡潔易懂，缺點就是遞迴調用時stack空間容易溢出，故實際實現中一般使用迭代替代遞迴，性能更佳嘛。不過迭代的缺點就是程式碼量稍(很)大，邏輯也可能不是那麼好懂。

既然確定使用遞迴，那麼接下來就應該考慮具體的實現問題了。在遞迴的具體實現中，主要考慮如下兩點：
1. 基本條件/終止條件 - 返回值需斟酌。
2. 遞迴步/條件遞迴 - 能使原始問題收斂。

首先來找找遞迴步，根據二叉查找樹的定義，若插入節點的值若大於當前節點的值，則繼續與當前節點的右子樹的值進行比較；反之則繼續與當前節點的左子樹的值進行比較。題目的要求是返回最終二元搜尋樹的根節點，從以上遞迴步的描述中似乎還難以對應到實際程式碼，這時不妨分析下終止條件。

有了遞迴步，終止條件也就水到渠成了，若當前節點爲空時，即返回結果。問題是——返回什麼結果？當前節點爲空時，說明應該將「插入節點」插入到上一個遍歷節點的左子節點或右子節點。對應到程序程式碼中即爲`root->right = node`或者`root->left = node`. 也就是說遞迴步使用`root->right/left = func(...)`即可。

### C++ Recursion

```c++
/**
 * forked from http://www.jiuzhang.com/solutions/insert-node-in-binary-search-tree/
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
     * @param root: The root of the binary search tree.
     * @param node: insert this node into the binary search tree
     * @return: The root of the new binary search tree.
     */
    TreeNode* insertNode(TreeNode* root, TreeNode* node) {
        if (NULL == root) {
            return node;
        }

        if (node->val <= root->val) {
            root->left = insertNode(root->left, node);
        } else {
            root->right = insertNode(root->right, node);
        }

        return root;
    }
};
```

### Java Recursion
```java
public class Solution {
    /**
     * @param root: The root of the binary search tree.
     * @param node: insert this node into the binary search tree
     * @return: The root of the new binary search tree.
     */
    public TreeNode insertNode(TreeNode root, TreeNode node) {
        if (root == null) {
            return node;
        }
        if (root.val > node.val) {
            root.left = insertNode(root.left, node);
        } else {
            root.right = insertNode(root.right, node);
        }
        return root;
    }
}
```

## 題解 - 迭代

看過了以上遞迴版的題解，對於這個題來說，將遞迴轉化爲迭代的思路也是非常清晰易懂的。迭代比較當前節點的值和插入節點的值，到了二元樹的最後一層時選擇是鏈接至左子結點還是右子節點。

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
 * }
 */
class Solution {
public:
    /**
     * @param root: The root of the binary search tree.
     * @param node: insert this node into the binary search tree
     * @return: The root of the new binary search tree.
     */
    TreeNode* insertNode(TreeNode* root, TreeNode* node) {
        if (NULL == root) {
            return node;
        }

        TreeNode* tempNode = root;
        while (NULL != tempNode) {
            if (node->val <= tempNode->val) {
                if (NULL == tempNode->left) {
                    tempNode->left = node;
                    return root;
                }
                tempNode = tempNode->left;
            } else {
                if (NULL == tempNode->right) {
                    tempNode->right = node;
                    return root;
                }
                tempNode = tempNode->right;
            }
        }

        return root;
    }
};
```

### Java Iterative
```java
public class Solution {
    /**
     * @param root: The root of the binary search tree.
     * @param node: insert this node into the binary search tree
     * @return: The root of the new binary search tree.
     */
    public TreeNode insertNode(TreeNode root, TreeNode node) {
        // write your code here
        if (root == null) return node;
        if (node == null) return root;
        
        TreeNode rootcopy = root;
        while (root != null) {
            if (root.val <= node.val && root.right == null) {
                root.right = node;
                break;
            }
            else if (root.val > node.val && root.left == null) {
                root.left = node;
                break;
            }
            else if(root.val <= node.val) root = root.right;
            else root = root.left;
        }
        return rootcopy;
    }
}
```


### 源碼分析

在`NULL == tempNode->right`或者`NULL == tempNode->left`時需要在鏈接完`node`後立即返回`root`，避免死循環。