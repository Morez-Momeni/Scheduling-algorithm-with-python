import matplotlib.pyplot as plt
import random


def FCFS():
    NumberOfProcess = int(input("Enter your process number :: "))

    p = 1
    process = []
    while p <= NumberOfProcess:
        Entry_Time = int(input(f"Enter entry time for P{p} :: "))
        Process_Time = int(input(f"Enter process time for P{p} :: "))
        if Process_Time == 0:
            continue
        process.append([f"P{p}", Entry_Time, Process_Time])
        p += 1

    process = sorted(process, key=lambda x: x[1])
    print(process)
    print("--------------------------------------------")

    current_time = 0
    done = []
    execution_blocks = []

    while len(done) < NumberOfProcess:
        for i in process:
            if i[1] <= current_time:
                start_time = current_time
                current_time += i[2]
                execution_blocks.append((i[0], start_time, i[2]))  
                done.append(i)
                process.remove(i)
                break
        else:
            current_time += 1

    fig, ax = plt.subplots(figsize=(12, 2))
    colors = {}
    y = 0

    for block in execution_blocks:
        name, start, duration = block
        if name not in colors:
            colors[name] = "#" + ''.join(random.choices("89ABCDEF", k=6))
        ax.barh(y, duration, left=start, height=0.6, color=colors[name], edgecolor='black')
        ax.text(start + duration / 2, y, name, va='center', ha='center', fontsize=9, color='black')

    ax.set_yticks([])
    ax.set_xticks(range(current_time + 1))
    ax.set_xlim(0, current_time)
    ax.set_xlabel("Time")
    ax.set_title("Gantt Chart - FCFS")
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
def SJF():
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



    fig, ax = plt.subplots(figsize=(12, 2))
    colors = {}

    y = 0  

    for process in gant:
        name, start, end = process
        duration = end - start


        if name not in colors:
            colors[name] = "#" + ''.join([random.choice("89ABCDEF") for _ in range(6)])

        ax.barh(y, duration, left=start, height=0.6, color=colors[name], edgecolor='black')


        ax.text(start + duration / 2, y, name, va='center', ha='center', color='black', fontsize=10)

    ax.set_yticks([])  
    ax.set_xticks(range(gant[-1][2] + 1)) 
    ax.set_xlim(0, gant[-1][2])
    ax.set_xlabel("Time")
    ax.set_title("Gantt Chart - SJF (Shortest Job First - Non-Preemptive)")
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
def RR():
    NumberOfProcess = int(input("Enter your process number :: "))

    p = 1
    process = []
    burst_dict = {}
    while p <= NumberOfProcess:
        Entry_Time = int(input(f"Enter the entry of process P{p} :: "))
        Process_Time = int(input(f"Enter process time for P{p} :: "))
        if Process_Time == 0:
            continue
        process.append([f"P{p}", Entry_Time, Process_Time])
        burst_dict[f"P{p}"] = Process_Time  
        p += 1

    process = sorted(process, key=lambda x: x[1])  

    gantt_chart = []
    Time_Slice = 2
    current_time = 0
    ready_queue = []
    remaining_time = {p[0]: p[2] for p in process}
    arrival_dict = {p[0]: p[1] for p in process}
    done = {}
    execution_blocks = []

    while len(done) < NumberOfProcess:
        for p in process:
            if p[1] <= current_time and p[0] not in ready_queue and p[0] not in done:
                ready_queue.append(p[0])
    
        if not ready_queue:
            current_time += 1
            continue

        current_process = ready_queue.pop(0)

        start_time = current_time
        if remaining_time[current_process] <= Time_Slice:
            current_time += remaining_time[current_process]
            execution_time = remaining_time[current_process]
            remaining_time[current_process] = 0
            done[current_process] = current_time
        else:
            current_time += Time_Slice
            execution_time = Time_Slice
            remaining_time[current_process] -= Time_Slice
            for p in process:
                if p[1] <= current_time and p[0] not in ready_queue and p[0] not in done and p[0] != current_process:
                    ready_queue.append(p[0])
            ready_queue.append(current_process)

        execution_blocks.append((current_process, start_time, execution_time))

    fig, ax = plt.subplots(figsize=(12, 2))
    colors = {}
    y = 0

    for block in execution_blocks:
        name, start, duration = block
        if name not in colors:
            colors[name] = "#" + ''.join(random.choices("89ABCDEF", k=6))
        ax.barh(y, duration, left=start, height=0.6, color=colors[name], edgecolor='black')
        ax.text(start + duration / 2, y, name, va='center', ha='center', fontsize=9, color='black')

    ax.set_yticks([])
    ax.set_xticks(range(current_time + 1))
    ax.set_xlim(0, current_time)
    ax.set_xlabel("Time")
    ax.set_title("Gantt Chart - Round Robin")
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
def SRT():
    NumberOfProcess = int(input("Enter your process number ? :: "))
    x = 1 
    a = []
    Current_Time = 0 

    while x <= NumberOfProcess:
        Process_Time = int(input(f"zaman pardazesh X{x} :: "))
        if Process_Time == 0:
            continue
        Entery_Time = int(input(f"zaman vorod X{x} :: "))
        remaining_time = Process_Time
        Process = [f"P{x}", Entery_Time, Process_Time, remaining_time]
        a.append(Process)
        x += 1

    a.sort(key=lambda a: a[1])

    z = 1
    done = []
    timeline = []

    while z <= len(a):
        in_order = []
        for i in a:
            if i[1] <= Current_Time and i not in done:
                in_order.append(i)
        if in_order:
            Next_Process = min(in_order, key=lambda x: x[3])
            timeline.append(Next_Process[0])
            Next_Process[3] -= 1
            Current_Time += 1
            if Next_Process[3] == 0:
                done.append(Next_Process)
                z += 1
        else:

            Current_Time += 1

    print(done)

    fig, ax = plt.subplots(figsize=(12, 2))
    colors = {}
    y = 0
    start_time = 0

    for i in range(len(timeline)):
        if i == 0 or timeline[i] != timeline[i - 1]:
            start_time = i
        if i == len(timeline) - 1 or timeline[i] != timeline[i + 1]:
            duration = i - start_time + 1
            proc_name = timeline[i]

        
            if proc_name not in colors:
                colors[proc_name] = "#" + ''.join([random.choice("89ABCDEF") for _ in range(6)])

            ax.barh(y, duration, left=start_time, height=0.6, color=colors[proc_name], edgecolor='black')
            ax.text(start_time + duration / 2, y, proc_name, va='center', ha='center', color='black', fontsize=10)

    ax.set_yticks([])
    ax.set_xticks(range(len(timeline)+1))
    ax.set_xlim(0, len(timeline))
    ax.set_xlabel("Time")
    ax.set_title("Gantt Chart - SRT (Shortest Remaining Time First)")
    plt.tight_layout()
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.show()

while True:
    print("CPU Scheduling Menu")
    print("1)FCFS\n2)SJF\n3)RR\n4)SRT\n5)Exit")
    menu_num = int(input("Enter your number :: "))

    if menu_num == 1:
        FCFS()
    elif menu_num == 2:
        SJF()
    elif menu_num == 3:
        RR()
    elif menu_num == 4:
        SRT()
    elif menu_num == 5:
        break
    else:
        print("Please select from 1 to 4 !!!")
        continue
