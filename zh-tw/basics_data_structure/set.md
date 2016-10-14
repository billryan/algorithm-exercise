# Set

Set 是一種用於保存不重複元素的資料結構。常被用作測試歸屬性，故其查找的性能十分重要。

## 程式實現

### Python

`Set` 是`python`自帶的基本資料結構， 有多種初始化方式。 `Python`的`set`跟`dict`的Implementation方式類似， 可以認爲`set`是只有`key`的`dict`.

```python
s = set()
s1 = {1, 2, 3}
s.add('shaunwei')
'shaun' in s  # return true
s.remove('shaunwei')
```

### C++

STL提供的資料結構有 Set 以及 Multiset ，分別提供不重複與重複元素的版本，自C++11以後，STL提供兩種 Set 的實現方式，一個是基於紅-黑樹的`set`與`multiset`，包含在`<set>`標頭檔之中，有序。另一個則是基於湊雜函數的`unordered_set`及`unordered_multiset`，包含在標頭檔`<unordered_set>`，無序。基本的 Set 使用如下所示

```C++
set<string> s;
s.insert("crossluna");
s.insert("billryan");
auto it = s.find("lucifer");
if(it != s.end()) {
    // "lucifer" found
}
```
另外可以藉由在建構時傳遞自訂的 Functor 、 Hash Function 以達成更彈性的使用，詳細用法及更多的介面請參考 STL 使用文檔。


### Java

Set 與 Collection 具有安全一樣的接口，通常有`HashSet`, `TreeSet` 或 `LinkedHashSet`三種實現。`HashSet`基於湊雜函數實現，無序，查詢速度最快；`TreeSet`基於紅-黑樹實現，有序。

```java
Set<String> hash = new HashSet<String>();
hash.add("billryan");
hash.contains("billryan");
```

在不允許重複元素時可當做哈希表來用。

