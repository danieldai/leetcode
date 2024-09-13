https://leetcode.com/problems/implement-queue-using-stacks/description/

讲解

https://programmercarl.com/0232.%E7%94%A8%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97.html


需要熟悉编程语言使用哪个数据结构作为栈，栈的对应操作都使用那些函数方法

```java
import java.util.Stack;

Stack<Integer> inStack = new Stack<>();
inStack.push(1)
inStack.pop()
inStack.peek()
inStack.empty()
```

python中可以使用list或者deque作为stack来使用。

```python
from collections import deque

# 创建一个空栈
stack = deque()

# 压入元素
stack.append(10)
stack.append(20)
stack.append(30)

# 弹出元素
top_element = stack.pop()  # 返回30

# 检查栈顶元素（不弹出）
top_element = stack[-1]  # 返回20

# 扩展栈
stack.extend([40, 50])

# 清空栈
stack.clear()


stack = []  # 创建一个空栈

# 压入元素
stack.append(10)
stack.append(20)
stack.append(30)

# 弹出元素
top_element = stack.pop()  # 返回30

```

在 C++ 中，和 Java 中的 java.util.Stack 对应的数据结构是 std::stack，它是 C++ 标准库中的一个模板类，提供了后进先出 (LIFO) 的栈操作。

std::stack 常用操作：
push()：向栈顶压入元素。
pop()：从栈顶弹出元素（注意：pop() 只弹出元素，不返回它）。
top()：返回栈顶元素的引用，但不弹出。
empty()：检查栈是否为空。
size()：返回栈中的元素个数。

```cpp
#include <iostream>
#include <stack>

int main() {
    std::stack<int> stack;

    // 压入元素
    stack.push(10);
    stack.push(20);
    stack.push(30);

    // 获取栈顶元素
    std::cout << "Top element: " << stack.top() << std::endl; // 输出 30

    // 弹出栈顶元素
    stack.pop();
    std::cout << "Top element after pop: " << stack.top() << std::endl; // 输出 20

    // 检查栈是否为空
    if (!stack.empty()) {
        std::cout << "Stack is not empty" << std::endl;
    }

    // 获取栈的大小
    std::cout << "Stack size: " << stack.size() << std::endl; // 输出 2

    return 0;
}

```

视频讲解

https://www.bilibili.com/video/BV1eg411w7gn?p=21&vd_source=dead283aa3efb297fb9f9c1d2b8e9fe8


热度
美团
