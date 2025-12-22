#二分探索

#targetちょうどのものがあればそのindexを,なければ-1を返す
def Binary_search(dat, target):
    left, right=0, len(dat)-1
    while(left<=right):
        mid=(left+right)//2
        if dat[mid]==target:
            return mid
        elif dat[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1


#targetより小さい最大のものを返す
def binary_search(dat, target):
    left=0
    right=len(dat)
    while left<right:
        mid=(left+right)//2
        if dat[mid]>=target:
            right=mid
        else:
            left=mid+1
    return left