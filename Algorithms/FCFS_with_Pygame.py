import pygame
import time
import math
import random

# User input
n = int(input("Number of processes: "))
processes = []
for i in range(n):
    pid = input(f"Process ID {i+1} (e.g., P1): ")
    arrival = int(input("Arrival time: "))
    burst = int(input("Burst time: "))
    processes.append({"pid": pid, "arrival": arrival, "burst": burst})

processes.sort(key=lambda x: x["arrival"])

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 1200, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" Neon CPU Command - FCFS Scheduling")

# Colors and fonts
BG_COLOR = (15, 15, 26)
NEON_BLUE = (0, 255, 255)
NEON_PURPLE = (209, 127, 255)
NEON_GREEN = (127, 255, 159)
NEON_ORANGE = (255, 170, 85)
TEXT_COLOR = (204, 204, 204)
WHITE = (255, 255, 255)
FONT = pygame.font.SysFont('consolas', 20)
BIG_FONT = pygame.font.SysFont('consolas', 28, bold=True)
COLORS = [NEON_BLUE, NEON_PURPLE, NEON_GREEN, NEON_ORANGE]
clock = pygame.time.Clock()

# Globals
gantt_chart = []
time_now = 0
cpu_center = (WIDTH // 2, 220)
process_radius = 30

def draw_background():
    WIN.fill(BG_COLOR)
    for _ in range(100):
        x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        pygame.draw.circle(WIN, (20, 20, 40), (x, y), 1)

def draw_cpu():
    pygame.draw.circle(WIN, NEON_BLUE, cpu_center, 60, 2)
    for i in range(8):
        angle = i * math.pi / 4
        x = cpu_center[0] + 70 * math.cos(angle)
        y = cpu_center[1] + 70 * math.sin(angle)
        pygame.draw.circle(WIN, NEON_BLUE, (int(x), int(y)), 3)
    label = BIG_FONT.render("CPU CORE", True, WHITE)
    WIN.blit(label, (cpu_center[0] - 70, cpu_center[1] - 15))

def draw_process(pos, color, pid):
    pygame.draw.circle(WIN, color, pos, process_radius)
    text = FONT.render(pid, True, WHITE)
    WIN.blit(text, (pos[0] - 15, pos[1] - 10))

def draw_gantt_chart():
    x = 60
    y = 550
    for item in gantt_chart:
        duration = item["end"] - item["start"]
        width = duration * 35
        rect = pygame.Rect(x, y, width, 40)
        pygame.draw.rect(WIN, item["color"], rect, border_radius=8)
        pid_text = FONT.render(item["pid"], True, TEXT_COLOR)
        WIN.blit(pid_text, (x + width // 2 - 10, y + 10))
        start_text = FONT.render(str(item["start"]), True, TEXT_COLOR)
        WIN.blit(start_text, (x, y + 45))
        x += width
    if gantt_chart:
        end_text = FONT.render(str(gantt_chart[-1]["end"]), True, TEXT_COLOR)
        WIN.blit(end_text, (x, y + 45))

def move_to_cpu(process, color):
    x = -50
    y = cpu_center[1]
    while x < cpu_center[0] - 40:
        draw_background()
        draw_cpu()
        draw_gantt_chart()
        draw_process((x, y), color, process["pid"])
        draw_status(f"Approaching {process['pid']} to CPU", 24)
        pygame.display.update()
        x += 7
        clock.tick(60)

def execute_process(process, color, current_time):
    draw_background()
    draw_cpu()
    draw_gantt_chart()
    draw_process(cpu_center, color, process["pid"])
    start_time = time.time()
    while time.time() - start_time < process["burst"]:
        draw_background()
        draw_cpu()
        draw_process(cpu_center, color, process["pid"])
        draw_gantt_chart()
        draw_status(f"Executing {process['pid']} - Remaining: {process['burst'] - int(time.time() - start_time)}s", 24)
        pygame.display.update()
        clock.tick(30)

def draw_status(text, size):
    font = pygame.font.SysFont('consolas', size, bold=True)
    render = font.render(text, True, WHITE)
    WIN.blit(render, (WIDTH // 2 - render.get_width() // 2, 30))

# Main loop
def main():
    global time_now
    current = 0
    running = True

    while running:
        draw_background()
        draw_cpu()
        draw_gantt_chart()
        draw_status(" Neon CPU Command Console - FCFS Scheduling", 26)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if current < len(processes):
            p = processes[current]
            if time_now < p["arrival"]:
                time_now += 1
                time.sleep(1)
                continue

            move_to_cpu(p, COLORS[current % len(COLORS)])
            execute_process(p, COLORS[current % len(COLORS)], time_now)

            gantt_chart.append({
                "pid": p["pid"],
                "start": time_now,
                "end": time_now + p["burst"],
                "color": COLORS[current % len(COLORS)]
            })

            time_now += p["burst"]
            current += 1
        else:
            draw_status(" All processes completed", 26)
            pygame.display.update()
            time.sleep(3)
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()
