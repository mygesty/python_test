# coding:utf-8

class Sort(object):
    def __init__(self, alist):
        self.alist = alist

    def bubble(self):
        alist = self.alist
        length = len(alist)
        for i in range(length-1):
            for j in range(length-i-1):
                if alist[j] > alist[j+1]:
                    alist[j], alist[j+1] = alist[j+1], alist[j]
        return alist

    def select(self):
        alist = self.alist
        length = len(alist)
        for i in range(length):
            min = i
            for j in range(i+1, length):
                if alist[min] > alist[j]:
                    min = j
            alist[i], alist[min] = alist[min], alist[i]
        return alist


    def insert(self):
        alist = self.alist
        length = len(alist)
        for i in range(1, length):
            for j in range(0, i):
                if alist[i] < alist[i-1]:
                    alist[i], alist[i-1] = alist[i-1], alist[i]
                    i -= 1
                else:
                    break
        return alist

    def shell(self):
        alist = self.alist
        length = len(alist)
        grep = length // 2
        while(grep >= 1):
            for i in range(grep, length):
                if alist[i] < alist[i-grep]:
                    alist[i], alist[i-grep] = alist[i-grep], alist[i]
            grep = int(grep / 2)
        return alist

    def quick(self, first, last):
        alist = self.alist
        if first >= last:
            return

        middle = alist[first]
        low = first
        high = last
        while low < high:
            while low < high and middle < alist[high]:
                high -= 1
            alist[low] = alist[high]
            while low < high and middle > alist[low]:
                low += 1
            alist[high] = alist[low]
        alist[low] = middle

        self.quick(first, low-1)
        self.quick(low+1, last)

    def merge(self, first, last):
        alist = self.alist[first:last]
        length = len(alist)
        if length <= 1:
            return alist
        min = length // 2
        left = self.merge(first, min+first)
        right = self.merge(min+first, last)

        left_pointer = 0
        right_pointer = 0
        result = []
        while left_pointer < len(left) and right_pointer < len(right):
            if left[left_pointer] < right[right_pointer]:
                result.append(left[left_pointer])
                left_pointer += 1
            else:
                result.append(right[right_pointer])
                right_pointer += 1
        result += left[left_pointer:]
        result += right[right_pointer:]
        return result
