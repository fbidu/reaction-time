"""
Here be awesome code!
"""
import sys
import random
from statistics import mean, median
from time import sleep, time


def benchmark():
    time_a = time()
    print("🌟🌟🌟🌟🌟🌟")
    _ = input()
    time_b = time()
    return time_b - time_a


if __name__ == "__main__":
    try:
        delay = float(sys.argv[1])
    except (IndexError, ValueError):
        delay = 0

    print(f"Desconsiderando delay de sistema de {delay}s")
    print("Quando aparecer estrelas na tela, aperte enter")
    times = []

    for _ in range(10):
        sleep(random.random() * random.randint(1, 3))
        timer = benchmark() - delay
        times.append(timer)

    print(f"Média = {mean(times)}")
    print(f"Mediana = {median(times)}")
