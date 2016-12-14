#
# mainFile.py
#
# Created by Radu Gabriel Albastroiu
#

import itertools

n = int(input(" Number N: "))

# print the number from input
print()
print(" N from input is: " + str(n))

# creates partitions for n
list_partitions = []
# numberk represent the number of elements in the partition
for numberk in reversed(range(1, n)):
    partition = []
    # creating one partition
    for iter in range(1,numberk + 1):
        partition.append(iter)

    Sum = (numberk * (numberk + 1)) / 2

    if Sum > n: 
        continue
    elif Sum == n:
        list_partitions.append(partition)
    else:
        # if the partition is 1 2 3 and sum 10 than make the partition 1 2 7
        partition[numberk - 1] += int(n - Sum)
        list_partitions.append(partition.copy())
        # start represent the position in list to start changing the list
        for start in reversed(range(0, numberk - 1)):
            # iter goes from start to end of list
            for iter in range(start,numberk - 1):
                
                # for each position in range start-end of list creates a new list 
                # EX: 1 2 7 -> 1 3 6 -> 1 4 5 than start gets 0 and 1 4 5 -> 2 3 5
                while partition[iter] + 2 < partition[iter + 1]:
                    partition[iter] += 1
                    partition[iter + 1] -= 1
                    list_partitions.append(partition.copy())

# print partitions
print()
print(" Partitions are :")
for alist in list_partitions:
    print(" - " + str(alist))

# nth palindrom number
nr = 0
count = 0
while True:
    nr += 1
    # from nr to nr string
    nr_list = [str(i) for i in str(nr)]
    
    # from nr to reversed nr string
    nr_list_reversed = [str(i) for i in reversed(str(nr))]
    
    # compare
    if nr_list == nr_list_reversed:
        count += 1
        if count == n:
            print()  
            print(" Nth palindrom number is : " + str(nr))
            break

# all subsequences of sum N
# using the list of partitions for each partition I generate all the permutations
# I do this using itertools
print()
print( " All subsequences of sum N are : ")
list_subsecv = []
for alist in list_partitions:
    # itertools.permutations(alist) = all permutation for a list
    list_subsecv.append(list(itertools.permutations(alist)))

# printing the subsequences
for i in list_subsecv:
    for j in i:
        print(j)
