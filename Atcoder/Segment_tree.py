#セグメント木(0-index) 最小値
n=100
unit=0#問題によって変える
#===セグメント木を生成===
def seg_tree(n):#nはデータの数
    x=1
    while x<n:#データの数を2^aの形にする
        x*=2
    n=x

    size=x*2
    dat=[unit]*size

    return dat

dat=seg_tree(n)

#===i番目の要素を更新をxに更新===
def update(i, x, dat):
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
    elif a<r and l<b:
        return dat[k]
    else:
        vl=result_sub(a, b, k*2+1, l, (l+r)//2)
        vr=result_sub(a, b, k*2+2, (l+r)//2, r)
        return(min(vl, vr))