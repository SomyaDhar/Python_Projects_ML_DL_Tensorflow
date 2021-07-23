import time

def insertion_sort(arr, displayBar, animSpeed): 
   
    for j in range(1, len(arr)): 
        key = arr[j] 
        k = j-1
        while k >=0 and key < arr[k] : 
                arr[k+1] = arr[k] 
                displayBar(arr, ['blue' if a == j or a ==k else 'red' for a in range(len(arr))])
            
                k -= 1
                
                time.sleep(animSpeed)    

        print(key)
        arr[k+1] = key 
        displayBar(arr, ['green' if a == j or a ==k+1 else 'blue' for a in range(len(arr))])
        time.sleep(animSpeed) 

        
    displayBar(arr, ['green' for a in range(len(arr))])