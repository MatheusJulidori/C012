import threading
import time

#Entrada dos valores de contagem regressiva para os usuários
cont1 = int(input("Entre com o tempo para o usuário 1: "))
cont2 = int(input("Entre com o tempo para o usuário 2: "))
cont3 = int(input("Entre com o tempo para o usuário 3: "))
def countdown(name, n):
    print(f"{name}: Iniciando contagem regressiva de {n} segundos.")
    while n > 0:
        print(f"{name}: {n} segundos restantes.")
        n -= 1
        time.sleep(1)
    print(f"{name}: Contagem regressiva concluída!")

# Lista de contagens regressivas a serem executadas
countdowns = [
    ("Contagem 1", cont1),
    ("Contagem 2", cont2),
    ("Contagem 3", cont3),
]

# Inicia as threads para cada contagem regressiva
threads = []
for name, n in countdowns:
    thread = threading.Thread(target=countdown, args=(name, n))
    threads.append(thread)
    thread.start()

# Aguarda todas as threads concluírem
for thread in threads:
    thread.join()

print("Todas as contagens regressivas foram concluídas.")
