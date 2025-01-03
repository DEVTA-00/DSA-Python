def secondLargest(a , n):
    largest = a[0]
    slargest = -1
    for i in range(n):
        if a[i] > largest:
            slargest = largest
            largest = a[i]
            
        elif a[i] < largest and a[i] > slargest:
            slargest = a[i]
            
    return slargest

def secondSma