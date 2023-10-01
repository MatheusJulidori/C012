from SJF.sjf import SJF
from PS.ps import PS
from RR.rr import RR
from FCFS.fcfs import FCFS

class Process:
    def __init__(self,number, name, priority, burst_time):
        self.number = number
        self.name = name
        self.priority = priority
        self.burst_time = burst_time
      

def main():
    processes = []
    num_processes = int(input("Quantos processos deseja criar? "))
    
    for i in range(num_processes):
        num = i + 1
        name = input(f"Nome do processo {num}: ")
        priority = int(input(f"Prioridade do processo {num}: "))
        burst_time = int(input(f"Tempo de burst do processo {num}: "))
        processes.append(Process(num, name, priority, burst_time))
    
    print("\nEscolha o algoritmo de escalonamento:")
    print("1. FCFS")
    print("2. SJF")
    print("3. PS")
    print("4. RR")
    
    choice = int(input("Digite o número correspondente ao algoritmo: "))
    
    if choice == 1:
        fcfs_scheduler = FCFS(processes)
        fcfs_scheduler.run()
    elif choice == 2:
        sjf_scheduler = SJF(processes)
        sjf_scheduler.run()
    elif choice == 3:
        ps_scheduler = PS(processes)
        ps_scheduler.run()
    elif choice == 4:
        quantum = int(input("Digite o quantum time para o algoritmo RR: "))
        rr_scheduler = RR(processes, quantum)
        rr_scheduler.run()
    else:
        print("Escolha inválida.")
        return

if __name__ == "__main__":
    main()
