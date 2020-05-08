def selectionSort(listData,order,mode):
    print("Data awal=",listData)
    num = 1
    if order == "asc":
        if mode == "min":
            for outIter in range(len(listData) - 1):
                selectData = outIter
                for inIter in range(outIter + 1, len(listData)):
                    if listData[inIter] < listData[selectData]:
                        selectData = inIter
                listData[outIter], listData[selectData] = listData[selectData], listData[outIter]
                print("Iterasi ke-{}: {}".format(outIter + 1, listData))
        elif mode == "max":
            for outIter in range(len(listData) - 1, 0, -1):
                selectData = outIter
                for inIter in range(outIter):
                    if listData[inIter] > listData[selectData]:
                        selectData = inIter
                listData[outIter], listData[selectData] = listData[selectData], listData[outIter]
                print("Iterasi ke-{}: {}".format(num, listData))
                num += 1
    elif order == "desc":
        if mode == "min":
            for outIter in range(len(listData) - 1, 0, -1):
                selectData = outIter
                for inIter in range(outIter):
                    if listData[inIter] < listData[selectData]:
                        selectData = inIter
                listData[outIter], listData[selectData] = listData[selectData], listData[outIter]
                print("Iterasi ke-{}: {}".format(num, listData))
                num += 1
        elif mode == "max":
            for outIter in range(len(listData) - 1):
                selectData = outIter
                for inIter in range(outIter + 1, len(listData)):
                    if listData[inIter] > listData[selectData]:
                        selectData = inIter
                listData[outIter], listData[selectData] = listData[selectData], listData[outIter]
                print("Iterasi ke-{}: {}".format(outIter + 1, listData))
    print("Data urut:", listData)

a= [6,8,1,2,9,7,3,5,4]
selectionSort(a,"asc","min")
# selectionSort(a,"asc","max")
# selectionSort(a,"desc","min")
# selectionSort(a,"desc","max")