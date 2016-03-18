# coding: utf-8

"""
    Author: AC
    Date:   16-3-18 下午4:37
    Description:    找出任意多个int型整数的中位数
"""
import random


# 随机生成count个[l, h]的int型数字
def generate_nums(count, l, h):
    _nums = []
    for i in xrange(count):
        temp = random.randint(l, h)
        # print i+1, temp
        _nums.append(temp)
    return _nums


# 将数字分区，分区存储
def split_nums(_nums, _parts, l, h):
    _splits = {}  # 记录每层中的数字
    ranges = []  # 记录层的边界数字
    ave_count = (h-l) / _parts
    for i in xrange(_parts+1):
        _range = l+i*ave_count
        if i < _parts:
            ranges.append(_range)
        else:
            ranges.append(max([_range, h]))

    for num in _nums:
        for i in xrange(len(ranges)-1):
            if ranges[i] <= num <= ranges[i+1]:
                if i not in _splits:
                    _splits[i] = [num]
                else:
                    _splits[i].append(num)
                break
    return _splits


# 统计获得中位数
def get_result(_splits, _counts):
    ave_pos = (_counts+1) / 2   # 中位数大概位置
    count = 0  # 记录浏览过的分区中数字的总数目
    area = 0  # 记录中文数所在分区的标号
    print '中位数(中间位置)的下标为%d' % ave_pos
    for i in _splits:
        if count < ave_pos:
            count += len(_splits[i])
            area = i
            print '前%d个分区的数字总数目为%d' % (i, count)
        else:
            print '前%d个分区数字总数目%d超过中间位置%d' % (i-1, count, ave_pos)
            break
    result_pos = ave_pos - (count - len(_splits[area]))
    print '中位数是第%d个分区的第%d个数' % (i-1, result_pos)
    data = sorted(_splits[area])
    print '升序排序第%d个分区:' % (i-1), _splits[area], '--->', data
    _result = data[result_pos-1]
    return _result

if __name__ == '__main__':
    counts = 100000  # 总数目
    parts = 1000  # 初始分区数目
    low = -10000  # 随机整数最小值
    high = 10000  # 随机整数最大值
    nums = generate_nums(counts, low, high)
    print '生成%d个[%d, %d]范围的随机整数:' % (counts, low, high), nums

    splits = split_nums(nums, parts, low, high)
    print '\n将随机生成的整数划分到%d个分区中:' % parts, splits

    print '\n计算中位数:'
    result = get_result(splits, counts)
    print '中位数:', result


