https://leetcode.com/problems/fibonacci-number/description/

视频讲解

https://www.bilibili.com/video/BV1eg411w7gn?p=63&vd_source=dead283aa3efb297fb9f9c1d2b8e9fe8

https://programmercarl.com/0509.%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE



动态规划的解题步骤

1、确定状态转移公式,当前的状态是怎么由前面的状态变化而来的及其与
之相关联的辅助的dp数组(dptable)以及下标的含义。这一步往往也是最难
的,这一步想清楚了,整个动态规划的问题基本上可以说就解决了一大半。一
般来说,首先要确定dp数组中元素代表的意义,然后在这个意义之下,确定状
态是如何在dp数组的元素之间如何变化的。

2、初始化dp数组。

3、根据题目条件确定遍历顺序,并实现状态转移公式。
同时在实现的过程中,可以适当的输出dp数组的值,确定自己的代码实现思
路无误。具体怎么做,我们用一个实际的题目来说明。