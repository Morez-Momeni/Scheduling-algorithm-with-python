NumbersOfProcess = int(input("Enter the number of process :: "))


process = []
i = 1

while i <= NumbersOfProcess :
    PriorityOfProcess = int(input("Enter priority of process :: "))
    Zaman_vorod = int(input("Enter entry of process :: "))
    Zaman_pardazesh = int(input("Enter execution time of process :: "))
    process.append([f"P{i}",Zaman_vorod,PriorityOfProcess,Zaman_pardazesh])
    i+=1
process = sorted(process , key= lambda x : x[2])
print(process)

current_time = 0

z = 1
done = []

while z <= len(process):
    ready = []  

    for p in process:
        if p[1] <= current_time and p not in done :
            ready.append(p)
    if ready :
        next_process = min(ready , key =lambda x : x[2])
        done.append(next_process)
        current_time += next_process[3]
        z+=1
    else:
        current_time+=1
    
print(done)
