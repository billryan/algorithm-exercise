# Insertion Sort - 插入排序

核心：通過構建有序序列，對於未排序序列，從後向前掃描(對於單向鏈表則只能從前往後遍歷)，找到相應位置並插入。實現上通常使用in-place排序(需用到O(1)的額外空間)

1. 從第一個元素開始，該元素可認為已排序
2. 取下一個元素，對已排序陣列從後往前掃描
3. 若從排序陣列中取出的元素大於新元素，則移至下一位置
4. 重複步驟3，直至找到已排序元素小於或等於新元素的位置
5. 插入新元素至該位置
6. 重複2~5

性質：

- 交換操作和陣列中導致的數量相同
- 比較次數>=倒置數量，<=倒置的數量加上陣列的大小減一
- 每次交換都改變了兩個順序顛倒的元素的位置，即減少了一對倒置，倒置數量為0時即完成排序。
- 每次交換對應著一次比較，且1到N-1之間的每個i都可能需要一次額外的記錄(a[i]未到達陣列左端時)
- 最壞情況下需要~$$N^2/2$$次比較和$$~N^2/2$$次交換，最好情況下需要$$N-1$$次比較和0次交換。
- 平均情況下需要~$$N^2/4$$次比較和~$$N^2/4$$次交換

![Insertion Sort](../../shared-files/images/insertion_sort.gif)


## Implementation

### Python

```python
#!/usr/bin/env python


def insertionSort(alist):
    for i, item_i in enumerate(alist):
        print alist
        index = i
        while index > 0 and alist[index - 1] > item_i:
            alist[index] = alist[index - 1]
            index -= 1

        alist[index] = item_i

    return alist

unsorted_list = [6, 5, 3, 1, 8, 7, 2, 4]
print(insertionSort(unsorted_list))
```

### Java

```java
public class Sort {
	public static void main(String[] args) {
		int unsortedArray[] = new int[]{6, 5, 3, 1, 8, 7, 2, 4};
		insertionSort(unsortedArray);
		System.out.println("After sort: ");
		for (int item : unsortedArray) {
			System.out.print(item + " ");
		}
	}

	public static void insertionSort(int[] array) {
		int len = array.length;
		for (int i = 0; i < len; i++) {
			int index = i, array_i = array[i];
			while (index > 0 && array[index - 1] > array_i) {
				array[index] = array[index - 1];
				index -= 1;
			}
			array[index] = array_i;

			/* print sort process */
			for (int item : array) {
				System.out.print(item + " ");
			}
			System.out.println();
		}
	}
}
```

實現(C++)：

```
template<typename T>
void insertion_sort(T arr[], int len) {
    int i, j;
    T temp;
    for (int i = 1; i < len; i++) {
        temp = arr[i];
        for (int j = i - 1; j >= 0 && arr[j] > temp; j--) {
            a[j + 1] = a[j];
        }
        arr[j + 1] = temp;
    }
}
```

## 希爾排序 Shell sort

核心：基於插入排序，使陣列中任意間隔為h的元素都是有序的，即將全部元素分為h個區域使用插入排序。其實現可類似於插入排序但使用不同增量。更高效的原因是它權衡了子陣列的規模和有序性。

實現(C++):

```
template<typename T>
void shell_sort(T arr[], int len) {
	int gap, i, j;
	T temp;
	for (gap = len >> 1; gap > 0; gap >>= 1)
		for (i = gap; i < len; i++) {
			temp = arr[i];
			for (j = i - gap; j >= 0 && arr[j] > temp; j -= gap)
				arr[j + gap] = arr[j];
			arr[j + gap] = temp;
		}
}
```

希爾排序只描述了分為多個h做插入排序，並沒有規定h的值，事實上有很多研究就是在探討不同的h值對於複雜度的影響，在英文版的wiki百科的[希爾排序](https://en.wikipedia.org/wiki/Shellsort)條目中，給出了多種不同的h序列及分析，事實上可以看到Sedgewick給出的序列已經可以達到最差$$\Theta(N^{4/3})$$的複雜度。在實際應用上，若不是排序非常大的序列，這個複雜度已經可以接受，另外希爾排序的實現簡單，尤其是在硬體上，因此可以用應用在嵌入式系統之中。

## Reference

- [插入排序 - 維基百科，自由的百科全書](http://zh.wikipedia.org/wiki/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F)
- [希爾排序 - 維基百科，自由的百科全書](http://zh.wikipedia.org/wiki/%E5%B8%8C%E5%B0%94%E6%8E%92%E5%BA%8F)
- [The Insertion Sort — Problem Solving with Algorithms and Data Structures](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html)
