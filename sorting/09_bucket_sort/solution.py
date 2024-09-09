import math


def bucket_sort(arr):
    if not arr:
        return []
    
    # 1. 找到数组中的最大值和最小值
    min_val = min(arr)
    max_val = max(arr)
    
    # 2. 确定桶的数量，通常选择桶数为数组长度的平方根
    bucket_count = int(math.sqrt(arr))
    buckets = [[] for _ in range(bucket_count)]
    
    # 3. 将数组中的元素分配到相应的桶中
    for num in arr:
        # 计算元素的桶索引
        bucket_index = (num - min_val) * (bucket_count - 1) // (max_val - min_val)
        buckets[bucket_index].append(num)
    
    # 4. 对每个桶内的元素进行排序
    sorted_buckets = []
    for bucket in buckets:
        # 使用插入排序或其他排序算法对桶内元素进行排序
        sorted_buckets.extend(sorted(bucket))
    
    return sorted_buckets

# 示例用法
if __name__ == "__main__":
    # 示例数组
    arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.68, 0.80]
    
    print("排序前的数组:")
    print(arr)
    
    sorted_arr = bucket_sort(arr)
    
    print("排序后的数组:")
    print(sorted_arr)
