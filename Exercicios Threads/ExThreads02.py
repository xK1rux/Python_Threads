import multiprocessing
import time
import random

def threads(id, valor):
    soma: int = 0

    for i in range(5):
        soma += valor[i]
        time.sleep(0.2)
    print(f"O resultado da soma da Thread #{id} é: {soma}")


def main():
    params = [(0, 0)]*3

    for i in range(3):
        valores = [0]*5
        for j in range(5):
            valores[j] = random.randint(1, 100)
        params[i] = (i + 1, valores)

    with multiprocessing.Pool(processes=3) as threads:
        threads.starmap(threads, params)


if __name__ == "__main__":
    main()