# Check if a singly linked list is palindrome

## Source

- [Function to check if a singly linked list is palindrome - GeeksforGeeks](http://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/)

```
Given a singly linked list of characters, write a function that
returns true if the given list is palindrome, else false.
```

- tags: palindrome, linked_list

## 题解1 - 使用辅助栈

根据栈的特性(FILO)，可以首先遍历链表并入栈(最后访问栈时则反过来了)，随后再次遍历链表并比较当前节点和栈顶元素，若比较结果完全相同则为回文。 又根据回文的特性，实际上还可以只遍历链表前半部分节点，再用栈中的元素和后半部分元素进行比较，分链表节点个数为奇数或者偶数考虑即可。由于链表长度未知，因此可以考虑使用快慢指针求得。

### Java

```java
/**
 * Definition for singly-linked list.
 */
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

public class Solution {
	public static boolean isPalindrome(ListNode head) {
		ListNode fast = head;
		ListNode slow = head;
		Stack<Integer> stack = new Stack<Integer>();

		// push node before mid
		while (fast != null && fast.next != null) {
			stack.push(slow.val);
			slow = slow.next;
			fast = fast.next.next;
		}

		// skip mid node for odd size
		if (fast != null) {
			slow = slow.next;
		}

		while (slow != null) {
			int top = stack.pop();
			// compare top with slow.val
			if (top != slow.val) {
				return false;
			}
			slow = slow.next;
		}

		return true;
	}

	public static void main (String[] args) {
		int len = 9;
		ListNode head = new ListNode(0);
		ListNode node = head;
		for (int i = 1; i < 9; i++) {
			int temp = (i >= len / 2) ? (len - i - 1) : i;
			node.next = new ListNode(temp);
			node = node.next;
		}

		System.out.println(isPalindrome(head));
	}
}
```

### 源码分析

注意区分好链表中个数为奇数还是偶数就好了，举几个简单例子辅助分析。

### 复杂度分析

使用了栈作为辅助空间，空间复杂度为 $$O(\frac{1}{2}n)$$, 分别遍历链表的前半部分和后半部分，时间复杂度为 $$O(n)$$.

## 题解2 - 原地翻转

题解 1 的解法使用了辅助空间，在可以改变原来的链表的基础上，可使用原地翻转，思路为翻转前半部分，然后迭代比较。具体可分为以下四个步骤。

1. 找中点。
2. 翻转链表的后半部分。
3. 逐个比较前后部分节点值。
4. 链表复原，翻转后半部分链表。

### Java

```java
/**
 * Definition for singly-linked list.
 */
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

public class Solution {
	public static boolean isPalindrome(ListNode head) {
		ListNode fast = head;
		ListNode slow = head;
		// push node before mid
		while (fast != null && fast.next != null) {
			slow = slow.next;
			fast = fast.next.next;
		}
		// skip mid node for odd number
		if (fast != null) {
			slow = slow.next;
		}

		ListNode rightHead = reverse(slow);
		ListNode rCurr = rightHead;
		ListNode lCurr = head;
		while (rCurr != null) {
			if (rCurr.val != lCurr.val) {
				return false;
			}
			lCurr = lCurr.next;
			rCurr = rCurr.next;
		}
		// recover list
		rightHead = reverse(rightHead);

		return true;
	}

	public static ListNode reverse (ListNode head) {
		ListNode prev = null;
		ListNode curr = head;
		while (curr != null) {
			ListNode temp = curr.next;
			curr.next = prev;
			prev = curr;
			curr = temp;
		}

		return prev;
	}

	public static void main (String[] args) {
		int len = 9;
		ListNode head = new ListNode(0);
		ListNode node = head;
		for (int i = 1; i < 9; i++) {
			int temp = (i >= len / 2) ? (len - i - 1) : i;
			node.next = new ListNode(temp);
			node = node.next;
		}

		System.out.println(isPalindrome(head));
	}
}
```

### 源码分析

连续翻转两次右半部分链表即可复原原链表，将一些功能模块如翻转等尽量模块化。

### 复杂度分析

遍历链表若干次，时间复杂度近似为 $$O(n)$$, 使用了几个临时遍历，空间复杂度为 $$O(1)$$.

## 题解3 - 递归

递归需要两个重要条件，递归步的建立和递归终止条件。对于回文比较，理所当然应该递归比较第 i 个节点和第 n-i 个节点，那么问题来了，如何构建这个递归步？大致可以猜想出来递归的传入参数应该包含两个节点，用以指代第 i 个节点和第 n-i 个节点。返回参数应该包含布尔值(用以提前返回不是回文的情况)和左半部分节点的下一个节点(用以和右半部分的节点进行比较)。由于需要返回两个值，在 Java 中需要使用自定义类进行封装，C/C++ 中则可以使用指针改变在**递归调用后**进行比较时节点的值。

### Java

```java
/**
 * Definition for singly-linked list.
 */
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

public class Solution {
	private class Result {
		ListNode node;
		boolean isp;
		Result(ListNode aNode, boolean ret) {
		       isp = ret;
		       node = aNode;
	       	}
	}

	public Result helper(ListNode left, ListNode right) {
		Result result = new Result(left, true);

		if (right == null) return result;

		result = helper(left, right.next);
		boolean isp = (right.val == result.node.val);
		if (!isp) {
			result.isp = false;
		}
		result.node = result.node.next;

		return result;
	}

	public boolean isPalindrome(ListNode head) {
		Result ret = helper(head, head);
		return ret.isp;
	}

	public static void main (String[] args) {
		int len = 9;
		ListNode head = new ListNode(0);
		ListNode node = head;
		for (int i = 1; i < 9; i++) {
			int temp = (i >= len / 2) ? (len - i - 1) : i;
			node.next = new ListNode(temp);
			node = node.next;
		}

		Solution ret = new Solution();
		System.out.println(ret.isPalindrome(head));
	}
}
```

### 源码分析

核心代码为返回 Result 复合数据类型部分，返回 result 后在返回最终结果之前需要执行`result.node = result.node.next`, 左半部分节点往后递推，用以返回给上层回调用。

### 复杂度分析

递归调用 n 层，时间复杂度近似为 $$O(n)$$, 使用了几个临时变量，空间复杂度为 $$O(1)$$.

## Reference

- [Function to check if a singly linked list is palindrome - GeeksforGeeks](http://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/)
- [回文判断 | The-Art-Of-Programming-By-July/01.04.md](https://github.com/julycoding/The-Art-Of-Programming-By-July/blob/master/ebook/zh/01.04.md)
- [ctci/QuestionB.java at master · gaylemcd/ctci](https://github.com/gaylemcd/ctci/blob/master/java/Chapter%202/Question2_7/QuestionB.java)
