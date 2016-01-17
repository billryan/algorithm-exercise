# Two Lists Sum Advanced <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>

## Question

- CC150 - [Add two numbers represented by linked lists | Set 2 - GeeksforGeeks](http://www.geeksforgeeks.org/sum-of-two-linked-lists/)

```
Given two numbers represented by two linked lists, write a function that returns sum list.
The sum list is linked list representation of addition of two input numbers.

Example

Input:
  First  List: 5->6->3  // represents number 563
  Second List: 8->4->2  // represents number 842
Output
  Resultant list: 1->4->0->5  // represents number 1405

Challenge

Not allowed to modify the lists.
Not allowed to use explicit extra space.
```

## 题解1 - 反转链表

在题 [Two Lists Sum | Data Structure and Algorithm](http://algorithm.yuanbin.me/zh-hans/linked_list/two_lists_sum.html) 的基础上改了下数位的表示方式，前者低位在前，高位在后，这个题的高位在前，低位在后。很自然地可以联想到先将链表反转，而后再使用 Two Lists Sum 的解法。

## Reference

- [Add two numbers represented by linked lists | Set 2 - GeeksforGeeks](http://www.geeksforgeeks.org/sum-of-two-linked-lists/)
