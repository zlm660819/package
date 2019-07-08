# -*- coding: utf-8 -*-

def binary_search(list_obj, key):
    l = 0
    h = len(list_obj) - 1
    time = 0
    while l < h:
        time += 1
        mid = int((l + h) / 2)
        if key < list_obj[mid]:
            h = mid - 1
        elif key > list_obj[mid]:
            l = mid + 1
        else:
            print("times: %s" % time)
            return mid
    print("times: %s" % time)
    return False
 

def interpolation_search(list_obj, key):
    l = 0
    h = len(list_obj) - 1
    time = 0
    while l < h:
        time += 1
    # 计算mid值是插值算法的核心代码
        mid = l + int((h - l) * (key - list_obj[l])/(list_obj[h] - list_obj[l]))
        print("mid=%s, l=%s, h=%s" % (mid, l, h))
        if key < list_obj[mid]:
            h = mid - 1
        elif key > list_obj[mid]:
            l = mid + 1
        else:
            print("times: %s" % time)
            return mid
    print("times: %s" % time)
    return False
 
def fibonacci_search(list_obj, key):
    F = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
        233, 377, 610, 987, 1597, 2584, 4181, 6765,
        10946, 17711, 28657, 46368]
    l = 0
    h = len(list_obj) - 1
    # 为了使得查找表满足斐波那契特性，在表的最后添加几个同样的值
    # 这个值是原查找表的最后那个元素的值
    # 添加的个数由F[k]-1-h决定
    k = 0
    while h > F[k]-1:
        k += 1
        print(k)
    i = h
    while F[k]-1 > i:
        list_obj.append(list_obj[h])
        i += 1
    print(list_obj)
    time = 0
    while l <= h:
        time += 1
        if k < 2:
            mid = l
        else:
            mid = l + F[k-1]-1
        print("l=%s, mid=%s, h=%s" % (l, mid, h))
        if key < list_obj[mid]:
            h = mid - 1
            k -= 1
        elif key > list_obj[mid]:
            l = mid + 1
            k -= 2
        else:
            if mid <= h:
                print("times: %s" % time)
                return mid
            else:
                print("times: %s" % time)
                return h
   print("times: %s" % time)
   return False
 

if __name__ == '__main__':
    list_obj = [1, 2, 5, 8, 10, 15, 19, 23, 25, 28, 30]
    result = binary_search(list_obj, 19)
    print(result)
