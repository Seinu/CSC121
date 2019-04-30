start_num = int(input("Enter starting number: "))
end_num = int(input("Enter ending number: "))
total = sum(i for i in range(start_num, end_num+1) if(i % 2 == 1))
print("Total of odd numbers in that range:", total)
