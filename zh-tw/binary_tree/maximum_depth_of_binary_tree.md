# Maximum Depth of Binary Tree

## Question

- leetcode: [Maximum Depth of Binary Tree | LeetCode OJ](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- lintcode: [(97) Maximum Depth of Binary Tree](http://www.lintcode.com/en/problem/maximum-depth-of-binary-tree/)

### Problem Statement

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.

#### Example

Given a binary tree as follow:



      1
     / \
    2   3
       / \
      4   5


The maximum depth is `3`.

## 題解 - 遞迴

樹遍歷的題目最方便的寫法自然是遞迴，不過遞迴調用的層數過多可能會導致 Stack 空間 overflow，因此需要適當考慮遞迴調用的層數。我們首先來看看使用遞迴如何解這道題，要求二叉樹的最大深度，直觀上來講使用深度優先搜索判斷左右子樹的深度孰大孰小即可，從根節點往下一層樹的深度即自增1，遇到`NULL`時即返回0。

由於對每個節點都會使用一次`maxDepth`，故時間複雜度爲 $$O(n)$$, 樹的深度最大爲 $$n$$, 最小爲 $$\log_2 n$$, 故空間複雜度介於 $$O(\log n)$$ 和 $$O(n)$$ 之間。

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
     * @param root: The root of binary tree.
     * @return: An integer
     */
    int maxDepth(TreeNode *root) {
        if (NULL == root) {
            return 0;
        }

        int left_depth = maxDepth(root->left);
        int right_depth = maxDepth(root->right);

        return max(left_depth, right_depth) + 1;
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
     * @return: An integer.
     */
    public int maxDepth(TreeNode root) {
        // write your code here
        if (root == null) {
            return 0;
        }
        return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }
}
```

## 題解 - 迭代(顯式使用 Stack)

使用遞迴可能會導致棧空間溢出，這裏使用顯式棧空間(使用堆內存)來代替之前的隱式 Stack 空間。從上節遞迴版的程式碼(先處理左子樹，後處理右子樹，最後返回其中的較大值)來看，是可以使用類似後序遍歷的迭代思想去實現的。

首先使用後序遍歷的模板，在每次迭代循環結束處比較棧當前的大小和當前最大值`max_depth`進行比較。

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
     * @param root: The root of binary tree.
     * @return: An integer
     */
    int maxDepth(TreeNode *root) {
        if (NULL == root) {
            return 0;
        }

        TreeNode *curr = NULL, *prev = NULL;
        stack<TreeNode *> s;
        s.push(root);

        int max_depth = 0;

        while(!s.empty()) {
            curr = s.top();
            if (!prev || prev->left == curr || prev->right == curr) {
                if (curr->left) {
                    s.push(curr->left);
                } else if (curr->right){
                    s.push(curr->right);
                }
            } else if (curr->left == prev) {
                if (curr->right) {
                    s.push(curr->right);
                }
            } else {
                s.pop();
            }

            prev = curr;

            if (s.size() > max_depth) {
                max_depth = s.size();
            }
        }

        return max_depth;
    }
};
```

## 題解3 - 迭代(隊列)

在使用了遞迴/後序遍歷求解樹最大深度之後，我們還可以直接從問題出發進行分析，樹的最大深度即爲廣度優先搜索中的層數，故可以直接使用廣度優先搜索求出最大深度。

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
     * @param root: The root of binary tree.
     * @return: An integer
     */
    int maxDepth(TreeNode *root) {
        if (NULL == root) {
            return 0;
        }

        queue<TreeNode *> q;
        q.push(root);

        int max_depth = 0;
        while(!q.empty()) {
            int size = q.size();
            for (int i = 0; i != size; ++i) {
                TreeNode *node = q.front();
                q.pop();

                if (node->left) {
                    q.push(node->left);
                }
                if (node->right) {
                    q.push(node->right);
                }
            }

            ++max_depth;
        }

        return max_depth;
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
     * @return: An integer.
     */
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int depth = 0;
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        while (!q.isEmpty()) {
            depth++;
            int qLen = q.size();
            for (int i = 0; i < qLen; i++) {
                TreeNode node = q.poll();
                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);
            }
        }

        return depth;
    }
}
```

### 源碼分析

廣度優先中隊列的使用中，`qLen` 需要在for 循環遍歷之前獲得，因爲它是一個變量。

### 複雜度分析

最壞情況下空間複雜度爲 $$O(n)$$, 遍歷每一個節點，時間複雜度爲 $$O(n)$$,
