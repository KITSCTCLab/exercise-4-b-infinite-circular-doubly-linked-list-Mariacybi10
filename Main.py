# Read an integer that denotes the length of the list which is returned as the output of the algorithm
length_of_circular_linked_list = int(input())
# Read space-separated integers that denote the elements of the list which is returned as the output of the algorithm
circular_linked_list = list(map(int,input().strip().split(" ")))
# Write your code here
output=[]

for x in circular_linked_list:
    if x not in output:
        output.append(x)
        
print(len(output))

for x in output:
    print(x,end=" ")
