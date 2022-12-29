def binary_search(arr,value):
    start=0
    end=len(arr)-1
    mid=(end+start)//2
    while (arr[mid] != value):
        if arr[mid]< value:
            start = mid+1
        else:
            end=mid-1
        mid=(start+end)//2
        print(start,mid,end)
    if arr[mid] == value :
        return mid #it shows the index value
    else:
        return " not found"               

print(binary_search([1,2,3,4,5,6,7,8,9],9))        