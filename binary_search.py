mylist = range(1, 6)
number = int(input())
low = 0
hight = len(mylist)-1
def binari_search(lis,item, lo, hi):
    mid = (lo+hi)//2
    guess = lis[mid]
    if guess == item:
        return mid
    if guess < item:
        return binari_search(lis, item, lo = mid + 1, hi=hi)
    if guess < item:
        return binari_search(lis, item, lo = lo, hi = mid - 1)
print(binari_search(mylist, number, low, hight))
