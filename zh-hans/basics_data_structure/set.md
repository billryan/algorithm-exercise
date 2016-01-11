# Set

Set 是一种用于保存不重复元素的数据结构。常被用作测试归属性，故其查找的性能十分重要。

## 编程实现

### Python

`Set` 是`python`自带的基本数据结构， 有多种初始化方式。 `Python`的`set`跟`dict`的Implementation方式类似， 可以认为`set`是只有`key`的`dict`.

```python
s = set()
s1 = {1, 2, 3}
s.add('shaunwei')
'shaun' in s  # return true
s.remove('shaunwei')
```


### Java

Set 与 Collection 具有安全一样的接口，通常有`HashSet`, `TreeSet` 或 `LinkedHashSet`三种实现。`HashSet`基于散列函数实现，无序，查询速度最快；`TreeSet`基于红-黑树实现，有序。

```java
Set<String> hash = new HashSet<String>();
hash.add("billryan");
hash.contains("billryan");
```

在不允许重复元素时可当做哈希表来用。
