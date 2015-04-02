# Selection Sort - 选择排序

核心：不断地选择剩余元素中的最小者。

1. 找到数组中最小元素并将其和数组第一个元素交换位置
2. 在剩下的元素中找到最小元素并将其与数组第二个元素交换，直至整个数组排序

实现：

```
public class Selection
{
    public static void sort(Comparable[] a)
    {
        int N = a.length();
        for (int i = 0; i < N; i++)
        {
            int min = i;
            for (int j = i+1; j < N; j++)
            {
                if (less(a[j], a[min]))
                {
                    min = j;
                }
            }
            exch(a, i, min);
        }
    }
}
```

性质：

- 比较次数=(N-1)+(N-2)+(N-3)+...+2+1~N^2/2
- 交换次数=N
- 运行时间与输入无关
- 数据移动最少

## Reference

[选择排序 - 维基百科，自由的百科全书](http://zh.wikipedia.org/wiki/%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F)
