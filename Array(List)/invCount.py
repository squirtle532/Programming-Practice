def invCount(arr):
    inv_count = 0
    n = len(arr)
    for i in range(n):
         for j in range(i+1,n):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count
if __name__ == "__main__":
    arr = [4, 3, 2, 1]
    print(invCount(arr))
