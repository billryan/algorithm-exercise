# Selection Sort - 选择排序

核心：不断地选择剩余元素中的最小者。

1. 找到数组中最小元素并将其和数组第一个元素交换位置。
2. 在剩下的元素中找到最小元素并将其与数组第二个元素交换，直至整个数组排序。

下图来源为 [File:Selection-Sort-Animation.gif - IB Computer Science](http://wiki.ibcsstudent.org/index.php?title=File:Selection-Sort-Animation.gif)

![Selection Sort](../images/selection_sort.gif)

以上排序过程使用 Python 实现如下所示：

```python
#!/usr/bin/env python


def selectionSort(alist):
    for i in xrange(len(alist)):
        print(alist)
        min_index = i
        for j in xrange(i + 1, len(alist)):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[min_index], alist[i] = alist[i], alist[min_index]
    return alist

unsorted_list = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
print(selectionSort(unsorted_list))
```

性质：

- 比较次数=(N-1)+(N-2)+(N-3)+...+2+1~N^2/2
- 交换次数=N
- 运行时间与输入无关
- 数据移动最少

## Reference

- [选择排序 - 维基百科，自由的百科全书](http://zh.wikipedia.org/wiki/%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F)
- [The Selection Sort — Problem Solving with Algorithms and Data Structures](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html)
