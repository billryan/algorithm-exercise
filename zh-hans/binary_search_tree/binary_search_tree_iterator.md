# Binary Search Tree Iterator

## Question

- lintcode: [(86) Binary Search Tree Iterator](http://www.lintcode.com/en/problem/binary-search-tree-iterator/) <i class="fa fa-star"></i><i class="fa fa-star"></i>

```
Design an iterator over a binary search tree with the following rules:

- Elements are visited in ascending order (i.e. an in-order traversal)
- next() and hasNext() queries run in O(1) time in average.

Example
For the following binary search tree, in-order traversal by using iterator is [1, 6, 10, 11, 12]

		   10
		 /    \
		1      11
		 \       \
		 	6       12

Challenge
Extra memory usage O(h), h is the height of the tree.

Super Star: Extra memory usage O(1)
```

## 题解 - 中序遍历

仍然考的是中序遍历，但是是非递归实现。其实这道题等价于写一个二叉树中序遍历的迭代器。需要内置一个栈，一开始先存储到最左叶子节点的路径。在遍历的过程中，只要当前节点存在右子树，则进入右子树，存储从此处开始到当前子树里最左叶子节点的路径。

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
 * Example of iterate a tree:
 * BSTIterator iterator = BSTIterator(root);
 * while (iterator.hasNext()) {
 *    TreeNode * node = iterator.next();
 *    do something for node
 */
    class BSTIterator {
    private:
        stack<TreeNode*> stack_;
        TreeNode* cur_ = NULL;
        
    public:
        //@param root: The root of binary tree.
        BSTIterator(TreeNode *root) {
            // write your code here
            cur_ = root;
        }
    
        //@return: True if there has next node, or false
        bool hasNext() {
            // write your code here
            return (cur_ || !stack_.empty());
        }
        
        //@return: return next node
        TreeNode* next() {
            // write your code here
            while (cur_) {
                stack_.push(cur_);
                cur_ = cur_->left;
            }
            cur_ = stack_.top();
            stack_.pop();
            TreeNode* node = cur_;
            cur_ = cur_->right;
            
            return node;
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
 * Example of iterate a tree:
 * Solution iterator = new Solution(root);
 * while (iterator.hasNext()) {
 *    TreeNode node = iterator.next();
 *    do something for node
 * } 
 */
public class Solution {
    private Stack<TreeNode> stack = new Stack<>();
    private TreeNode curt;
    
    // @param root: The root of binary tree.
    public Solution(TreeNode root) {
        curt = root;
    }

    //@return: True if there has next node, or false
    public boolean hasNext() {
        return (curt != null || !stack.isEmpty()); //important to judge curt != null
    }
    
    //@return: return next node
    public TreeNode next() {
        while (curt != null) {
            stack.push(curt);
            curt = curt.left;
        }
        
        curt = stack.pop();
        TreeNode node = curt;
        curt = curt.right;
        
        return node;
    }
}
```

### 源码分析

1. 这里容易出错的是 `hasNext()` 函数中的判断语句，不能漏掉 `curt != null`。
2. 如果是 leetcode 上的原题，由于接口不同，则不需要维护 current 指针。
