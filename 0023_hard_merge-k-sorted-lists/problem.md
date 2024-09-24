https://leetcode.com/problems/merge-k-sorted-lists/description/


可以把问题分解为合并两个排序的链表

过去3个月
字节跳动
11
谷歌Google
3
Meta
亚马逊
2
腾讯
2
微软Microsoft
领英 Linkedln
IXL
2
优步
Uber
2
爱彼迎Airbnb
2
过去6个月
推特Twitter
6个月前
美团



You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []