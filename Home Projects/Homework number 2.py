#
# mainFile.py
#
# Created by Radu Gabriel Albastroiu
#

# if the relationships are reflexive
def reflexive(adiacent, A):
    for i in range(len(A)):
        bool = False
        for ele in adiacent[i]:
            if ele == A[i]:
                bool = True
                break
        if(bool == False):
            return False
    return True

# if the relationships are simetrical (graph without orientation)
def simetrical(adiacent, A):
    for i in range(len(A)):
        for ele in adiacent[i]:
            if A[i] != ele:
                if not A[i] in adiacent[A.index(ele)]:
                    return False
    return True       

# if the relationships have the transitive property
# A->B and B->C => A->C
# i is A
# ele si B
# second_ele is C
def transitive(adiacent, A):
    for i in range(len(A)):
        for ele in adiacent[i]:
            if ele != A[i]:
                for second_ele in adiacent[A.index(ele)]:
                    if second_ele != A[i] and second_ele != ele:
                        if not second_ele in adiacent[i]:    
                            return False
    return True
                
# echivalent clases(number of conex components in a graph)
def echiv_clases(adiacent, A):
    viz_list = []
    for i in range(len(A)):
        viz_list.append(0)
    
    # id reprezent the number of components
    id = 0
    for ele in A:
        if not viz_list[A.index(ele)]:
            id += 1
            dfs(adiacent, A, viz_list, ele, id)
    
    return viz_list
  
# normal depth first search
def dfs(adiacent, A, viz_list, ele, id):
    # in viz list I put the number of the echivalent class
    viz_list[A.index(ele)] = id

    for next in adiacent[A.index(ele)]:
        if not viz_list[A.index(next)]:
            dfs(adiacent, A, viz_list, next, id)



# data
A = []
relationship_links = []
i = 0

# input reading
for input_line in open('date.txt'):
    if i:
        relationship_links.append(input_line.split())
    else:
        A = input_line.split()
        i += 1

# sort the relationships between elements
relationship_links.sort()

# creating an adiacent list
adiacent_list = []
for ele in A:
    alist = []
    for rel in relationship_links:
        if rel[0] == ele:
            alist.append(rel[1])
        if rel[1] == ele and rel[0] != rel[1]:
            alist.append(rel[0])
     
    # remove duplicates
    alist_without_duplicates = []
    for ele in alist:
        if ele not in alist_without_duplicates:
            alist_without_duplicates.append(ele)
    # sort the list for every node
    alist_without_duplicates.sort()
    # add the list created for one node
    adiacent_list.append(alist_without_duplicates)


# functions calls and printing the results
bool_reflexive = reflexive(adiacent_list, A)
if bool_reflexive:
    print(" The operation has the reflexive property")
else:
    print(" The operation has not the reflexive proeperty")

bool_simetrical = simetrical(adiacent_list, A)
if bool_simetrical:
    print(" The operation has the simetrical property")
else:
    print(" The operation has not the simetrical proeperty")

bool_transitive = transitive(adiacent_list, A)
if bool_transitive:
    print(" The operation has the transitive property")
else:
    print(" The operation has not the transitive property")

bool_echiv = False

# check if the operation is equivalent
if bool_reflexive and bool_simetrical and bool_transitive:
    bool_echiv = True

echiv_clases_list = []
if bool_echiv:
    echiv_clases_list = echiv_clases(adiacent_list, A)

MAX = 0
if len(echiv_clases_list):
    MAX = max(echiv_clases_list)

# print the clases of equivalence
if MAX:
    print(" There are " + str(MAX) + " clases of equivalence")
    for i in range(MAX):
        alist = []
        j = 0
        for ele in echiv_clases_list:
            if ele == i + 1:
                alist.append(A[j])
            j += 1
        print(" - Class of equivalence nr " + str(i+1) + ": ", alist)
    
