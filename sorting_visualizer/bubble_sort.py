import time

def bubble_sort(arr, displayBar, animSpeed):
    for _ in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                displayBar(arr, ['blue' if a == j or a ==j+1 else 'red' for a in range(len(arr))])
                time.sleep(animSpeed)
    displayBar(arr, ['blue' for a in range(len(arr))])
        
        
                