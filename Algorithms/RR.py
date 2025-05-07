NumberOfProcess = int(input("Enter your process number :: "))

p = 1
process = []
burst_dict = {}
while p <= NumberOfProcess:
    Entry_Time = int(input(f"Enter the entry of process P{p} :: "))
    Process_Time = int(input(f"Enter process time for P{p} :: "))
    process.append([f"P{p}", Entry_Time, Process_Time])
    burst_dict[f"P{p}"] = Process_Time  
    p += 1

process = sorted(process, key=lambda x: x[1])  

Time_Slice = 2
ready_queue = []
current_time = 0
done = {}
remaining_time = {p[0]: p[2] for p in process}
arrival_dict = {p[0]: p[1] for p in process}
execution_order = []

while len(done) < NumberOfProcess:
    for p in process:
        if p[1] <= current_time and p[0] not in ready_queue and p[0] not in done:
            ready_queue.append(p[0])
    
    if not ready_queue:
        current_time += 1
        continue

    current_process = ready_queue.pop(0)
    execution_order.append(current_process)

    if remaining_time[current_process] <= Time_Slice:
        current_time += remaining_time[current_process]
        remaining_time[current_process] = 0
        done[current_process] = current_time  
    else:
        current_time += Time_Slice
        remaining_time[current_process] -= Time_Slice
        for p in process:
            if p[1] <= current_time and p[0] not in ready_queue and p[0] not in done and p[0] != current_process:
                ready_queue.append(p[0])
        ready_queue.append(current_process)

print("\nFinal Results:")
print("Process | Arrival | Burst | Finish | Turnaround ")
total_tat = 0
total_wt = 0

for p in process:
    name = p[0]
    arrival = p[1]
    burst = burst_dict[name]
    finish = done[name]
    tat = finish - arrival

    print(f"{name:7} | {arrival:7} | {burst:5} | {finish:6} | {tat:10}")

print("\nGantt:")
print(" -> ".join(execution_order))
