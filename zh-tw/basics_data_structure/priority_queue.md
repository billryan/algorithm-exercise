# Priority Queue - 優先隊列

應用程序常常需要處理帶有優先級的業務，優先級最高的業務首先得到服務。因此優先隊列這種資料結構應運而生。優先隊列中的每個元素都有各自的優先級，優先級最高的元素最先得到服務；優先級相同的元素按照其在優先隊列中的順序得到服務，例如作業系統(operating system)中的任務調度。

優先隊列與其說是資料結構，不如說是一種抽象資料型別(Abstract Data Type，ADT)，其介面(interface)至少需要三個基本的方法(method)：
 - 插入一筆優先級別資料 (insert_with_priority)
 - 取出最優先資料 (pull_highest_priority_element)
 - 查看最優先資料 (peak)
若使用C++的STL提供的介面則如下所示

```c++
template <typename T> class priority_queue{
    void push (const T& val);
    void pop ();
    const T& top() const;
};
```

優先隊列可以使用數組或鏈表實現，從時間和空間複雜度來說，往往用堆(heap)來實現。

## Reference

- [優先佇列 - 維基百科，自由的百科全書](http://zh.wikipedia.org/zh/%E5%84%AA%E5%85%88%E4%BD%87%E5%88%97)
- [STL: priority_queue](http://www.cplusplus.com/reference/queue/priority_queue/)
