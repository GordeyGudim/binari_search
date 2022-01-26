mylist = range(1, 6)
number = int(input())
low = 0
hight = len(mylist)-1
def binary_search(lis,item, lo, hi):
    mid = (lo+hi)//2
    guess = lis[mid]
    if guess == item:
        return mid
    if lo <= hi:
        if guess < item:
            return binary_search(lis, item, lo = mid + 1, hi=hi)
        if guess > item:
            return binary_search(lis, item, lo = lo, hi = mid - 1)
    else:
        return -1
print(binary_search(mylist, number, low, hight))
