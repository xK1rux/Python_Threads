import multiprocessing
import time
import random

def threads(sapos, dist_percorrida):
    dist_percurso: int = 30
    dist_salto: int = 0
    
    while dist_percorrida < dist_percurso:
        dist_salto = random.randint(1, 5)
        dist_percorrida += dist_salto
        print(f"O sapo #{sapos} saltou {dist_salto} metros e percorreu {dist_percorrida} metros")
        time.sleep(0.5)
    print(f"O sapo #{sapos} chegou ao final do percurso!")
    
def main():
    params = [(0, 0)] * 5
    distancia: int = 0

    for i in range(5):
        params[i] = (i + 1, distancia)

    with multiprocessing.Pool(processes=5) as threads:
        threads.starmap(threads, params)


if __name__ == "__main__":
    main()