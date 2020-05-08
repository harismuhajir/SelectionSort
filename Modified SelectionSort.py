def modifiedSelection(listData):
    print("Data awal:",listData)
    i = 0
    j = len(listData)-1
    while i < j:
        print("Iterasi ke-{}:".format(i+1))
        min,max = listData[i],listData[i]
        swap_min,swap_max = i,i
        for k in range(i,j+1):
            if listData[k] > max:
                max = listData[k]
                swap_max = k
            elif listData[k] < min:
                min = listData[k]
                swap_min = k
        listData[i],listData[swap_min] = listData[swap_min],listData[i]
        print("Minimal:",listData)
        if listData[swap_min] == max:
            listData[j],listData[swap_min] = listData[swap_min],listData[j]
        else:
            listData[j], listData[swap_max] = listData[swap_max], listData[j]
        i += 1
        j -= 1
        print("Maksimal:",listData)
    print("Data urut:",listData)

a= [6,8,1,2,9,7,3,5,4]
modifiedSelection(a)