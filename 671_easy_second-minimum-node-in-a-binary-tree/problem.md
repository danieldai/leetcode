https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/


要利用这个树的特性，从上到下遍历树，如果遇到和根节点值不一样的节点就可以结束遍历对应的子树，这个节点是潜在的答案。
取各个子树潜在答案的最小值