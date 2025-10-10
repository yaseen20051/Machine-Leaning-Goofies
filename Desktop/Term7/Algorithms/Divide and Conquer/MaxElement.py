

def maxElement(arr,left,right):
    if(left == right):
        return arr[left]
    mid = (left + right) // 2
    maxleft = maxElement(arr,left,mid)
    maxRight = maxElement(arr,mid+1,right)
    max = maxleft if maxleft>maxRight else maxRight
    return max


if __name__ == "__main__" :
        print(maxElement([1,2,20,10,21,6,7],0,6))