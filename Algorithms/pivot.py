def pivot(list, pivot):
    list.append(pivot) # dodanie pivotu do listy
    for powtorzenie in range(len(list)-1): # powtorz tyle razy ile jest elementow w liscie
        # elementy mniejsze maja byc przenoszone na prawa strone
        for i in range(len(list)-1):
            if list[i] < pivot:
                el = list[i]
                list.remove(el)
                list.append(el)
    # odwroc kolejnosc (mniejsze maja byc na lewej stronie)
    list.reverse()
    return list


l = [6, 7, 3, 1, 9, 9, 5, 1, 2]
l2 = [1,2,3,4,5,6,7,8,9]
l3= [9,8,7,6,5,4,3,2,1]


print(pivot(l,6))
print(pivot(l2,10))
print(pivot(l3,3))



