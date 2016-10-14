# Map - 關聯容器

Map 是一種關聯數組的資料結構，也常被稱爲字典(dictionary)或鍵值對(key-value pair)。

## 程式實現

### Python

在 Python 中 `dict`(Map) 是一種基本的資料結構。

```python
# map 在 python 中是一個keyword
hash_map = {} # or dict()
hash_map['shaun'] = 98
hash_map['wei'] = 99
exist = 'wei' in hash_map  # check existence
point = hash_map['shaun']  # get value by key
point = hash_map.pop('shaun') # remove by key, return value
keys = hash_map.keys()  # return key list
# iterate dictionary(map)
for key, value in hash_map.items():
    # do something with k, v
    pass
```

### C++

與 Set 類似，STL提供了 Map 與 Multimap 兩種，提供同一鍵(key)對應單個或多個值(value)，自C++11以後，一樣提供兩種實現方式，基於紅-黑樹的`map`與`multimap`，包含在`<map>`標頭檔之中，鍵有序。另一個則是基於湊雜函數的`unordered_map`及`unordered_multimap`包含在標頭檔`<unordered_map>`，鍵無序。基本的 Map 使用如下所示

```C++
map<string, int> mp;
mp ["billryan"] = 69;
mp ["crossluna"] = 159;
auto it = mp.find("billryan"); 
if(it != mp.end()) {
    // "billryan" found
    cout << mp["billryan"]; // output: 69
}
```
另外可以藉由在建構時傳遞自訂的 Functor 、 Hash Function 以達成更彈性的使用，詳細用法及更多的介面請參考 STL 使用文檔。

### Java

Java 的實現中 Map 是一種將物件與物件相關聯的設計。常用的實現有`HashMap`和`TreeMap`, `HashMap`被用來快速訪問，而`TreeMap`則保證『鍵』始終有序。Map 可以返回鍵的 Set, 值的 Collection, 鍵值對的 Set.

```java
Map<String, Integer> map = new HashMap<String, Integer>();
map.put("bill", 98);
map.put("ryan", 99);
boolean exist = map.containsKey("ryan"); // check key exists in map
int point = map.get("bill"); // get value by key
int point = map.remove("bill") // remove by key, return value
Set<String> set = map.keySet();
// iterate Map
for (Map.Entry<String, Integer> entry : map.entrySet()) {
    String key = entry.getKey();
    int value = entry.getValue();
    // do some thing
}
```