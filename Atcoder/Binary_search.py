#二分探索
def Binary_search(dat, value):
    left, right=0, len(dat)-1
    while(left<=right):
        mid=(left+right)//2
        if dat[mid]==value:
            return mid
        elif dat[mid]<value:
            left=mid+1
        else:
            right=mid-1
    return -1