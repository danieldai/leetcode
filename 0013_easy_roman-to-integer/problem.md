https://leetcode.com/problems/roman-to-integer/

微软

说明：

有个隐含的条件，罗马数字 有 III, IV, 但是不会出现 IIV这样的情况

这样就可以从右向左遍历罗马数字的字符串，如果出现左边的字符比右边字符小，那就减去对应的数字，其它情况都是加上对应的数字