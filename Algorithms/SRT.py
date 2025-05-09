import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random


NumberOfProcess = int(input("Enter your process number ? :: "))
x = 1 
a = []
Current_Time = 0 

while x <= NumberOfProcess:
    Process_Time = int(input("zaman pardazesh :: "))
    if Process_Time == 0:
        continue
    Entery_Time = int(input("zaman vorod :: "))
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
        timeline.append("Current_time increased")
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
