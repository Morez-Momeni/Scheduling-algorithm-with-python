NumberOfProcess = int(input("Enter your process number ? :: "))
x = 1 
a = []
Current_Time = 0 

while x <= NumberOfProcess :
    Process_Time = int(input("zaman pardazesh :: "))
    if Process_Time == 0:
        continue
    Entery_Time = int(input("zaman vorod :: "))
    Process = [f"P{x}",Entery_Time,Process_Time]
    a.append(Process)
    x+=1

a.sort(key= lambda a: a[1])
print(a)

z = 1
done = []
gant = []
while z <= len(a):
    in_order = []
    for i in a :
        if i[1] <= Current_Time and i not in done:
            in_order.append(i)
    if in_order:
        Next_Process = min(in_order , key= lambda x : x[2])
        done.append(Next_Process)
        Start_Time = Current_Time
        Current_Time += Next_Process[2]
        End_Time = Current_Time
        gant.append([Next_Process[0],Start_Time,End_Time])
        z+=1
    else:
        Current_Time+=1

print(done)
print(gant)
for g in gant:
    print(f"{g[0]} | Start: {g[1]} ------> End: {g[2]} ")   



