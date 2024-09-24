https://leetcode.com/problems/binary-tree-postorder-traversal/description/

讲解

https://www.bilibili.com/video/BV1eg411w7gn?p=27&vd_source=dead283aa3efb297fb9f9c1d2b8e9fe8

https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%80%92%E5%BD%92%E9%81%8D%E5%8E%86.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE


1. 递归的方式
2. 使用栈来迭代的方式，迭代是先把左节点都入栈，然后检查栈顶的元素是否有右子节点，或者右子节点是否被访问过，右子节点被放过过后才访问当前节点，否则把右子节点也入栈

