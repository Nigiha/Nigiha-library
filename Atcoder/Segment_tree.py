#セグメント木(0-index)
#===セグメント木を生成===
def seg_tree(n):#nはデータの数
    unit=0#問題によって変える
    x=1
    while x<n:#データの数を2^aの形にする
        x*=2
    n=x

    size=x*2
    dat=[unit]*size

#===i番目の要素を更新をxに更新===
def update(i, x):
    i+=n-1
    dat[i]=x
    while i>0:
        i=(i-1//2)
        dat[i]=min(dat[i*2+1], dat[i*2-2])
    
#===(a, b]の最小値を求める===
def result(a, b):
    return result_sub(a, b, 0, 0, n)
def result_sub(a, b, k, r, l):
    if r<=a or b<=l:
        return unit
    