# Convert Sorted List to Binary Search Tree

## Question

- leetcode - [Convert Sorted List to Binary Search Tree | LeetCode OJ](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)
- lintcode - [(106) Convert Sorted List to Binary Search Tree](http://www.lintcode.com/en/problem/convert-sorted-list-to-binary-search-tree/)

```
Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.
```

## 题解 - 折半取中

题 [Convert Sorted Array to Binary Search Tree | Data Structure and Algorithm](http://algorithm.yuanbin.me/zh-hans/binary_search_tree/convert_sorted_array_to_binary_search_tree.html) 的升级版，不过这里把「有序数组」换成了「有序链表」。我们可以参考上题的题解思路，思考如何才能在链表中找到「中间节点」。对于本题的单向链表来说，要想知道中间位置的节点，则必须需要知道链表的长度，因此我们就自然联想到了可以通过遍历链表来求得其长度。求得长度我们就知道了链表中间位置节点的索引了，进而根据头节点和当前节点则可将链表分为左右两半形成递归模型。到这里还只能算是解决了问题的一半，这道题另一比较麻烦的地方在于边界条件的取舍，很难第一次就 AC, 下面结合代码做进一步的分析。

### C++

```c++
/**
 * Definition of ListNode
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 *     ListNode(int val) {
 *         this->val = val;
 *         this->next = NULL;
 *     }
 * }
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
     * @param head: The first node of linked list.
     * @return: a tree node
     */
    TreeNode *sortedListToBST(ListNode *head) {
        if (NULL == head) {
            return NULL;
        }

        // get the size of List
        ListNode *node = head;
        int len = 0;
        while (NULL != node) {
            node = node->next;
            ++len;
        }

        return buildBSTHelper(head, len);
    }

private:
    TreeNode *buildBSTHelper(ListNode *head, int length) {
        if (NULL == head || length <= 0) {
            return NULL;
        }

        // get the middle ListNode as root TreeNode
        ListNode *lnode = head;
        int count = 0;
        while (count < length / 2) {
            lnode = lnode->next;
            ++count;
        }

        TreeNode *root = new TreeNode(lnode->val);
        root->left = buildBSTHelper(head, length / 2);
        root->right = buildBSTHelper(lnode->next, length - 1 - length / 2);

        return root;
    }
};
```

### 源码分析

1. 异常处理。
2. 获取链表长度。
3. `buildBSTHelper`输入参数为表头节点地址以及相应的链表长度，递归获取根节点、左节点和右节点。

其中`buildBSTHelper`的边界处理很有技巧，首先是递推的终止条件，头节点为`NULL`时显然应该返回`NULL`. 但`length`的终止条件又如何确定？拿不定主意时就用几个简单例子来试试，比如`1`, `1->2`, `1->2->3`.

先来分析下给`buildBSTHelper`传入的`length`的含义——从表头节点`head`开始往后递推长度为`length`的链表。故`length`为0时表示不访问链表中的任一节点，也就是说应该返回`NULL`.

再来分析链表的中间位置如何确定，我们引入计数器`count`来表示**目前需要遍历`count`个链表节点数目**才能得到中间位置的节点。看看四种不同链表长度下的表现。

1. 链表长度为1时，中间位置即为自身，计数器的值为0.
2. 链表长度为2时，中间位置可选第一个节点，也可选第二个节点，相应的计数器值为0或1.
3. 链表长度为3时，中间位置为第二个节点，相应的计数器应为1，表示从表头节点往后递推一个节点。
4. 链表长度为4时，... 计数器的值为1或者2.

从以上四种情况我们可以推断出`count`的值可取为`length / 2`或者`length / 2 + 1`, 简单起见我们先取`length / 2`试试，对应的边界条件即为`count < length / 2`, `count`初始值为0. 经过`count`次迭代后，目前`lnode`即为所需的链表中间节点，取出其值初始化为`TreeNode`的根节点。

确定根节点后还需要做的事情就是左子树和右子树中链表头和链表长度的取舍。首先来看看左子树根节点的确定，**`count`的含义为到达中间节点前遍历过的链表节点数目，那么从另一方面来说它就是前半部分链表的长度！**故将此长度`length / 2`作为得到左子树根节点所需的链表长度参数。除掉链表前半部分节点和中间位置节点这两部分外，剩下的链表长度即为`length - 1 - length / 2`.

> **Warning** `length - 1 - length / 2 != length / 2 - 1`

有没有觉得可以进一步化简为`length / 2 - 1`? 我首先也是这么做的，后来发现一直遇到`TERMSIG= 11`错误信息，这种错误一般是指针乱指或者指针未初始化就去访问。但自己仔细检查后发现并没有这种错误，于是乎在本地做单元测试，发现原来是死循环造成了栈空间溢出(猜的)！也就是说边界条件有问题！可自己的分析明明是没啥问题的啊...

在这种情况下我默默地打开了九章的参考代码，发现他们竟然没有用`length / 2 - 1`，而是`length - 1 - length / 2`. 立马意识到这两者可能并不相等。用错误数据试了下，长度为1或者3时两者即不相等。知道对于整型数来说，`1 / 2`为0，但是却没能活学活用，血泪的教训。:-( 一个美好的下午就没了。

在测试出错的时候，还是要相信测试数据的力量，而不是凭自己以前认为对的方式去解决问题。

### 复杂度分析

首先遍历链表得到链表长度，复杂度为 $$O(n)$$. 递归遍历链表时，每个链表节点被访问一次，故时间复杂度为 $$O(n)$$, 两者加起来总的时间复杂度仍为 $$O(n)$$.

### 进一步简化代码
```c++
class Solution {
public:
    TreeNode *sortedListToBST(ListNode *head) {
        int length = 0;
        ListNode *curr = head;
        while (curr != NULL) {
            curr = curr->next;
            ++length;
        }
        return helper(head, length);
    }
private:
    TreeNode *helper(ListNode *&pos, int length) {
        if (length <= 0) {
            return NULL;
        }
        
        TreeNode *left = helper(pos, length / 2);
        TreeNode *root = new TreeNode(pos->val); // the sequence cannot be changed!
                                                 // this is important difference of the solution above
        pos = pos->next;
        root->left = left;
        root->right = helper(pos, length - length / 2 - 1);
        return root;
    }
};
```

### 源码分析
1. 可以进一步简化 helper 函数代码，注意参数的接口设计。
2. 即是把传入的链表指针向前递进 n 步，并返回经过的链表节点转化成的二分查找树的根节点。
3. 注意注释中的那两句实现，`new root` 和 `new left` 不可调换顺序。这才是精简的要点。但是这种方法不如上面的分治法容易理解。


### O(nlogn) 的实现，避免 length 边界
```java
/**
 * Definition for ListNode.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int val) {
 *         this.val = val;
 *         this.next = null;
 *     }
 * }
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
     * @param head: The first node of linked list.
     * @return: a tree node
     */
    public TreeNode sortedListToBST(ListNode head) {
        if (head == null) {
            return null;
        }
        return helper(head);
    } 

    private TreeNode helper(ListNode head) {
        if (head == null) {
            return null;
        }
        if (head.next == null) {
            return new TreeNode(head.val);
        }

        ListNode pre = null;
        ListNode slow = head, fast = head;

        while (fast != null && fast.next != null) {
            pre = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        pre.next = null;

        TreeNode root = new TreeNode(slow.val);
        TreeNode L = helper(head);
        TreeNode R = helper(slow.next);
        root.left = L;
        root.right = R;

        return root;
    } 
}
```
### 源码分析
1. 如果想避免上述 length 边界搞错的问题，可以使用分治法遍历树求中点的方法。
2. 但这种时间复杂度是 $$O(nlogn)$$，性能上还是比 $$O(n)$$ 差一点。

## Reference

- [Convert Sorted List to Binary Search Tree | 九章算法](http://www.jiuzhang.com/solutions/convert-sorted-list-to-binary-search-tree/)
