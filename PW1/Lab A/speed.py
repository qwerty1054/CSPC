import time
from decay import simulate, simulate_loop

def main():
    N0 = 200000
    lam = 0.05

    t0 = time.perf_counter()
    simulate_loop(N0, lam)
    t_loop = time.perf_counter() - t0

    t0 = time.perf_counter()
    simulate(N0, lam)
    t_numpy = time.perf_counter() - t0

    speedup = t_loop / t_numpy

    print(f"Pure Python loop time: {t_loop:.4f} s")
    print(f"NumPy vectorized time: {t_numpy:.4f} s")
    print(f"NumPy is {speedup:.2f}x faster than Python loop")

if __name__ == "__main__":
    main()