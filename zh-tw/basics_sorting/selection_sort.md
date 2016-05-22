# Selection Sort - 選擇排序

核心：不斷地選擇剩餘元素中的最小者。

1. 找到陣列中最小元素並將其和陣列第一個元素交換位置。
2. 在剩下的元素中找到最小元素並將其與陣列第二個元素交換，直至整個陣列排序。

性質：

- 比較次數=(N-1)+(N-2)+(N-3)+...+2+1~N^2/2
- 交換次數=N
- 運行時間與輸入無關
- 數據移動最少

下圖來源為 [File:Selection-Sort-Animation.gif - IB Computer Science](http://wiki.ibcsstudent.org/index.php?title=File:Selection-Sort-Animation.gif)

![Selection Sort](../../shared-files/images/selection_sort.gif)

## Implementation

### Python

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

### Java

```java
public class Sort {
	public static void main(String[] args) {
		int unsortedArray[] = new int[]{8, 5, 2, 6, 9, 3, 1, 4, 0, 7};
		selectionSort(unsortedArray);
		System.out.println("After sort: ");
		for (int item : unsortedArray) {
			System.out.print(item + " ");
		}
	}

	public static void selectionSort(int[] array) {
		int len = array.length;
		for (int i = 0; i < len; i++) {
			for (int item : array) {
				System.out.print(item + " ");
			}
			System.out.println();
			int min_index = i;
			for (int j = i + 1; j < len; j++) {
				if (array[j] < array[min_index]) {
					min_index = j;
				}
			}
			int temp = array[min_index];
			array[min_index] = array[i];
			array[i] = temp;
		}
	}
}
```

###C++

```C++
void selectionSort(vector<int> & arr){
    int min_idx = 0;
    for(int i = 0; i < arr.size(); i++){
        min_idx = i;
        for(int j = i + 1; j < arr.size(); j++){
            if (arr[j] < arr[min_idx])
                min_idx = j;
        }
        std::swap(arr[i], arr[min_idx]);
    }
}
```

## Reference

- [選擇排序 - 維基百科，自由的百科全書](http://zh.wikipedia.org/wiki/%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F)
- [The Selection Sort — Problem Solving with Algorithms and Data Structures](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html)
