# Read an integer that denotes the length of the list which is returned as the output of the algorithm
length_of_circular_linked_list = int(input())
# Read space-separated integers that denote the elements of the list which is returned as the output of the algorithm
circular_linked_list = list(map(int,input().strip().split(" ")))
# Write your code here
if len(circular_linked_list)%3 !=0:
    while(len(circular_linked_list)%3 !=0):
        circular_linked_list.append(-1)
temp = []
index=-1
for i in range(len(circular_linked_list)//3):
    x = []
    for i in range(3):
        index+=1
        if circular_linked_list[index] == -1:
            continue
        x.append(circular_linked_list[index])
    for j in x:
        if j not in temp:
            temp.append(j)

print(len(temp))
print(*temp,sep=" ")
