# coding: utf-8

"""
    优化算法实现：爬山，模拟退火，(遗传算法)
    目标：求数组a[]中的最大值
"""
import random
import math
import time

# 生成数组a[]
def generate_data(n, l, h):
    a = []
    for i in xrange(n):
        a.append(random.randint(l, h))
    return a

# 暴力穷举
def brute_force(a):
    max = a[0]
    for i in xrange(len(a)):
        if a[i] > max:
            max = a[i]
    return max

# 爬山法:可以选择不同初始点，获得不同的局部最优解，进而获得更靠谱的全局近似最优解
def hill_climbing(a):
    init = random.choice([i for i in xrange(len(a))])
    max_l, max_r = a[init], a[init]
    l, r = init, init
    print '(初始点下标, 值): (', init, ',', a[init], ')'
    print '向左搜寻最大值:',
    while l >= 0:
        if a[l] > max_l:
            max_l = a[l]
            print '(', init-l, ',', a[l], ') ---> ',
        if l>0 and max_l > a[l-1]:
            break
        l -= 1
    print '向左搜寻%d个点，得到局部最优解%d' % (init-l, max_l)

    print '向右搜寻最大值:',
    while r < len(a):
        if a[r] > max_r:
            max_r = a[r]
            print '(', r-init, ',', a[r], ') ---> ',
        if r < len(a)-1 and max_r > a[r+1]:
            break
        r += 1
    print '向右搜寻%d个点，得到局部最优解%d' % (r-init, max_r)
    result = max([max_l, max_r])
    print '综合左右两边，得到', result
    return result

# 模拟退火算法
def SimulatedAnnealing(a):
    T = 100000000000000000000 # 初始温度
    T1 = 1    # 终止温度,即循环终止条件
    k = 0.5   # 降温系数

    init = random.choice([i for i in xrange(len(a))])
    max_l, max_r = a[init], a[init]
    l, r = init, init
    T_l, T_r = T, T
    print '(初始点下标, 值): (', init, ',', a[init], ')'

    print '向左搜寻最大值:',
    while T_l > T1 and l >= 0:
        dE = a[l] - max_l
        # 产生新解
        if dE >= 0:
            max_t = a[l]
        elif math.e**(dE/T_l) > random.random():
            max_t = a[l]
        # 接受新解
        if max_t > max_l:
            max_l = max_t
        print '(%d, %d) ---> ' % (init-l, max_l),
        T_l *= k  # 降火
        l -= 1
    print '向左搜寻%d个点，得到局部最优解%d' % (init-l, max_l)

    print '向右搜寻最大值:',
    while T_r > T1 and r < len(a):
        dE = a[r] - max_r
        # 产生新解
        if dE >= 0:
            max_t = a[r]
        elif math.e**(dE/T_r) > random.random():
            max_t = a[r]
        # 接受新解
        if max_t > max_r:
            max_r = max_t
        print '(%d, %d) ---> ' % (r-init, max_r),
        T_r *= k  # 降火
        r += 1
    print '向右搜寻%d个点，得到局部最优解%d' % (r-init, max_r)

    result = max([max_l, max_r])
    print '综合左右两边，得到', result
    return result

if __name__ == '__main__':
    a = generate_data(100000, 1, 1000000)
    print len(a), a
    print '\n=========暴力法========='
    b1 = time.time()
    print brute_force(a)
    e1 = time.time()
    print '暴力穷举法用时', (e1-b1)
    print '\n=========爬山法========='
    b2 = time.time()
    hill_climbing(a)
    e2 = time.time()
    print '爬山法用时', (e2-b2)
    print '\n=======模拟退火法========='
    b3 = time.time()
    SimulatedAnnealing(a)
    e3 = time.time()
    print '模拟退火法用时', (e3-b3)
    print '=================='
