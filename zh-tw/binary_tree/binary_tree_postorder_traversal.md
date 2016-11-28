# Binary Tree Postorder Traversal

## Question

- leetcode: [Binary Tree Postorder Traversal | LeetCode OJ](https://leetcode.com/problems/binary-tree-postorder-traversal/)
- lintcode: [(68) Binary Tree Postorder Traversal](http://www.lintcode.com/en/problem/binary-tree-postorder-traversal/)

### Problem Statement

Given a binary tree, return the _postorder_ traversal of its nodes' values.

#### Example

Given binary tree `{1,#,2,3}`,



       1
        \
         2
        /
       3


return `[3,2,1]`.

#### Challenge

Can you do it without recursion?


## 題解1 - 遞迴

首先使用遞迴便於理解。

### Python - Divide and Conquer

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        if root is None:
            return []
        else:
            return self.postorderTraversal(root.left) +\
                   self.postorderTraversal(root.right) + [root.val]
```

### C++ - Traversal

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

### Java - Divide and Conquer

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
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        if (root != null) {
            List<Integer> left = postorderTraversal(root.left);
            result.addAll(left);
            List<Integer> right = postorderTraversal(root.right);
            result.addAll(right);
            result.add(root.val);
        }

        return result;
    }
}
```

### 源碼分析

遞迴版的太簡單了，沒啥好說的，注意入 Stack 順序。

### 複雜度分析

時間複雜度近似爲 $$O(n)$$.

## 題解2 - 迭代

使用遞迴寫後序遍歷那是相當的簡單，我們來個不使用遞迴的迭代版。整體思路仍然爲「左右根」，那麼怎麼才能知道什麼時候該訪問根節點呢？問題即轉化爲如何保證左右子節點一定先被訪問到？由於入Stack之後左右節點已無法區分，因此需要區分左右子節點是否被訪問過(加入到最終返回結果中)。除了有左右節點的情況，根節點也可能沒有任何子節點，此時也可直接將其值加入到最終返回結果中。

### Python

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        result = []
        if root is None:
            return result
        s = []
        # previously traversed node
        prev = None
        s.append(root)
        while s:
            curr = s[-1]
            noChild = curr.left is None and curr.right is None
            childVisited = (prev is not None) and \
                           (curr.left == prev or curr.right == prev)
            if noChild or childVisited:
                result.append(curr.val)
                s.pop()
                prev = curr
            else:
                if curr.right is not None:
                    s.append(curr.right)
                if curr.left is not None:
                    s.append(curr.left)

        return result
```

### C++

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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> result;
        if (root == NULL) return result;

        TreeNode *prev = NULL;
        stack<TreeNode *> s;
        s.push(root);
        while (!s.empty()) {
            TreeNode *curr = s.top();
            bool noChild = false;
            if (curr->left == NULL && curr->right == NULL) {
                noChild = true;
            }
            bool childVisited = false;
            if (prev != NULL && (curr->left == prev || curr->right == prev)) {
                childVisited = true;
            }

            // traverse
            if (noChild || childVisited) {
                result.push_back(curr->val);
                s.pop();
                prev = curr;
            } else {
                if (curr->right != NULL) s.push(curr->right);
                if (curr->left != NULL) s.push(curr->left);
            }
        }

        return result;
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
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        if (root == null) return result;

        Deque<TreeNode> stack = new ArrayDeque<TreeNode>();
        stack.push(root);
        TreeNode prev = null;
        while (!stack.isEmpty()) {
            TreeNode curr = stack.peek();
            boolean noChild = (curr.left == null && curr.right == null);
            boolean childVisited = false;
            if (prev != null && (curr.left == prev || curr.right == prev)) {
                childVisited = true;
            }

            if (noChild || childVisited) {
                result.add(curr.val);
                stack.pop();
                prev = curr;
            } else {
                if (curr.right != null) stack.push(curr.right);
                if (curr.left != null) stack.push(curr.left);
            }
        }

        return result;
    }
}
```

### 源碼分析

遍歷順序爲『左右根』，判斷根節點是否應該從Stack中剔除有兩種條件，一爲無子節點，二爲子節點已遍歷過。判斷子節點是否遍歷過需要排除`prev == null` 的情況，因爲 prev 初始化爲 null.

**將遞迴寫成迭代的難點在於如何在迭代中體現遞迴本質及邊界條件的確立，可使用簡單示例和紙上畫出Stack調用圖輔助分析。**

### 複雜度分析

最壞情況下Stack內存儲所有節點，空間複雜度近似爲 $$O(n)$$, 每個節點遍歷兩次或以上，時間複雜度近似爲 $$O(n)$$.

## 題解3 - 反轉先序遍歷

要想得到『左右根』的後序遍歷結果，我們發現只需將『根右左』的結果轉置即可，而先序遍歷通常爲『根左右』，故改變『左右』的順序即可，所以如此一來後序遍歷的非遞迴實現起來就非常簡單了。

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
    /**
     * @param root: The root of binary tree.
     * @return: Postorder in vector which contains node values.
     */
public:
    vector<int> postorderTraversal(TreeNode *root) {
        vector<int> result;
        if (root == NULL) return result;

        stack<TreeNode*> s;
        s.push(root);
        while (!s.empty()) {
            TreeNode *node = s.top();
            s.pop();
            result.push_back(node->val);
            // root, right, left => left, right, root
            if (node->left != NULL) s.push(node->left);
            if (node->right != NULL) s.push(node->right);
        }
        // reverse
        std::reverse(result.begin(), result.end());
        return result;
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
     * @return: Postorder in ArrayList which contains node values.
     */
    public ArrayList<Integer> postorderTraversal(TreeNode root) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        if (root == null) return result;

        Deque<TreeNode> stack = new ArrayDeque<TreeNode>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            result.add(node.val);
            if (node.left != null) stack.push(node.left);
            if (node.right != null) stack.push(node.right);
        }
        Collections.reverse(result);

        return result;
    }
}
```

### 源碼分析

注意入Stack的順序和最後轉置即可。

### 複雜度分析

同先序遍歷。

## Reference

- [[leetcode]Binary Tree Postorder Traversal @ Python - 南郭子綦](http://www.cnblogs.com/zuoyuan/p/3720846.html) - 解釋清晰
- [更簡單的非遞迴遍歷二叉樹的方法](http://zisong.me/post/suan-fa/geng-jian-dan-de-bian-li-er-cha-shu-de-fang-fa) - 比較新穎和簡潔的實現
