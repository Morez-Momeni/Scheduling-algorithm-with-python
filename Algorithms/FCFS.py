NumberOfProcess = int(input("Enter your process number :: "))

p = 1
process = []
while p <= NumberOfProcess:
    Entry_Time = int(input("Enter the entry of process :: "))
    Process_Time = int(input("Enter process time :: "))
    process.append([f"P{p}", Entry_Time, Process_Time])
    p+=1

process = sorted(process, key= lambda x : x[1])
print(process)
print("--------------------------------------------")


current_time = 0
done = []

while len(done) < NumberOfProcess :
    for i in process :
        if i[1] <= current_time:
            done.append(i)
            current_time+=i[2]
            process.remove(i)
            break
    else:
        current_time+=1
print(done)
        