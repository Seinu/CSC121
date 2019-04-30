average = lambda l:sum(l) / len(l)

list1 = [2, 1, 5, 9, 8]
list1_avg = average(list1)
print("list1 average:", format(list1_avg,".2f"))
list2 = [17, 5, 2, 4]
list2_avg = average(list2)
print("list2 average:", format(list2_avg,".2f"))