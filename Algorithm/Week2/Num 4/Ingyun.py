def solution(food_times, k): 
    from heapq import heapify, heappop, heappush
    heap=[]
    for i, v in enumerate(food_times):
        heappush(heap, [v,i])
    
    remain_len = len(food_times)
    already_food = 0
    while heap:
        popv, popi = heappop(heap)
        t = (popv-already_food)*remain_len
        
        if k >= t:
            k = k-t
            already_food = popv
            remain_len -= 1
        else :
            k = k%remain_len
            heappush(heap, [popv, popi])
            mylist = sorted(heap, key=lambda x: x[1])
            return mylist[k][1]+1
    else :
        return -1