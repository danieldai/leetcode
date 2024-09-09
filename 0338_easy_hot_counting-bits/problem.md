https://leetcode.com/problems/counting-bits/description/

视频讲解

https://www.bilibili.com/video/BV1eg411w7gn?p=50&vd_source=dead283aa3efb297fb9f9c1d2b8e9fe8


热度
LeetCode热题HOT 100》专题

X=X&(X-1),清除最低位的1。

设 函数 f(X) 为 数字到比特位个数的函数
```
f(X) = f(X&(X-1)) + 1
```

比如:假设X=21,二进制表示为00010101
```
21 & 20 =
0001 0101 &
0001 0100 =
0001 0100 = 20

20 & 19 =
0001 0100 &
0001 0011 =
0001 0000 = 16

16 & 15 =
0001 0000 &
00001111 = 0
```

利用奇偶性

    // 如果一个数是奇数，那么它的1的个数为 n-1 的 1的个数加1
    // 如果一个数是偶数，那么它的1的个数为 为 n/2 的 1的个数相同