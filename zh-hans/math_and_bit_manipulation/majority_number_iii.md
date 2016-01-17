# Majority Number III

## Question

- lintcode: [(48) Majority Number III](http://www.lintcode.com/en/problem/majority-number-iii/)

```
Given an array of integers and a number k,
the majority number is the number that occurs more than 1/k of the size of the array.

Find it.

Example
Given [3,1,2,3,2,3,3,4,4,4] and k=3, return 3.

Note
There is only one majority number in the array.

Challenge
O(n) time and O(k) extra space
```

## 题解

[Majority Number II](http://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/majority_number_ii.html) 的升级版，有了前两道题的铺垫，此题的思路已十分明了，对 K-1个数进行相互抵消，这里不太可能使用 key1, key2...等变量，用数组使用上不太方便，且增删效率不高，故使用哈希表较为合适，当哈希表的键值数等于 K 时即进行清理，当然更准备地来讲应该是等于 K-1时清理。故此题的逻辑即为：1. 更新哈希表，若遇哈希表 size == K 时则执行删除操作，最后遍历哈希表取真实计数器值，返回最大的 key.

### C++
```c++
class Solution {
public:
    /**
     * @param nums: A list of integers
     * @param k: As described
     * @return: The majority number
     */
    int majorityNumber(vector<int> nums, int k) {
        unordered_map<int, int> map;
        
        for (auto n : nums) {
           if (map.size() < k) map[n]++;
           else {
                if (map.count(n)) map[n]++;
                else {
                    map[n] = 1;
                    vector<int> keys;
                    for (auto &it : map) {
                        it.second--;
                        if (!it.second) keys.push_back(it.first);
                    }
                    for (int i : keys) map.erase(i);
                }
            }   
        }
        
        int mx = 0;
        int ret = 0;
        for (auto &it : map) {
            if (it.second > mx) {
                ret = it.first;
                mx = it.second;
            }
        }
        return ret;
    }
};
```

### Java

```java
public class Solution {
    /**
     * @param nums: A list of integers
     * @param k: As described
     * @return: The majority number
     */
    public int majorityNumber(ArrayList<Integer> nums, int k) {
        HashMap<Integer, Integer> hash = new HashMap<Integer, Integer>();
        if (nums == null || nums.isEmpty()) return -1;

        // update HashMap
        for (int num : nums) {
            if (!hash.containsKey(num)) {
                hash.put(num, 1);
                if (hash.size() >= k) {
                    removeZeroCount(hash);
                }
            } else {
                hash.put(num, hash.get(num) + 1);
            }
        }

        // reset
        for (int key : hash.keySet()) {
            hash.put(key, 0);
        }
        for (int key : nums) {
            if (hash.containsKey(key)) {
                hash.put(key, hash.get(key) + 1);
            }
        }

        // find max
        int maxKey = -1, maxCount = 0;
        for (int key : hash.keySet()) {
            if (hash.get(key) > maxCount) {
                maxKey = key;
                maxCount = hash.get(key);
            }
        }

        return maxKey;
    }

    private void removeZeroCount(HashMap<Integer, Integer> hash) {
        Set<Integer> keySet = hash.keySet();
        for (int key : keySet) {
            hash.put(key, hash.get(key) - 1);
        }

        /* solution 1 */
        Iterator<Map.Entry<Integer, Integer>> it = hash.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry<Integer, Integer> entry = it.next();
            if(entry.getValue() == 0) {
                it.remove();
            }
        }

        /* solution 2 */
        // List<Integer> removeList = new ArrayList<>();
        // for (int key : keySet) {
        //     hash.put(key, hash.get(key) - 1);
        //     if (hash.get(key) == 0) {
        //         removeList.add(key);
        //     }
        // }
        // for (Integer key : removeList) {
        //     hash.remove(key);
        // }

        /* solution3 lambda expression for Java8 */
    }
}
```

### 源码分析

此题的思路不算很难，但是实现起来还是有点难度的，**Java 中删除哈希表时需要考虑线程安全。**

### 复杂度分析

时间复杂度 $$O(n)$$, 使用了哈希表，空间复杂度 $$O(k)$$.

## Reference

- [Majority Number III 参考程序 Java/C++/Python](http://www.jiuzhang.com/solutions/majority-number-iii/)
