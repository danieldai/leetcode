

def heapify(arr, n, i):
    # 初始化最大值为根节点
    largest = i
    left = 2 * i + 1  # 左子节点
    right = 2 * i + 2  # 右子节点

    # 如果左子节点存在且大于根节点，则更新最大值为左子节点
    if left < n and arr[i] < arr[left]:
        largest = left

    # 如果右子节点存在且大于当前最大值，则更新最大值为右子节点
    if right < n and arr[largest] < arr[right]:
        largest = right

    # 如果最大值不是根节点，则交换根节点与最大值对应的节点
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # 递归地调整受影响的子树
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # 构建最大堆
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 一个一个地从堆顶取出最大值，并放在数组末尾
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换当前堆顶元素和堆的最后一个元素
        heapify(arr, i, 0)  # 对剩余的堆进行调整

