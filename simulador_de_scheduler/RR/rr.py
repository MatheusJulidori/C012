class RR:
    def __init__(self, processes, quantum):
        self.processes = processes
        self.quantum = quantum
        self.result = []  # To store the execution order
        self.waiting_time = []
        self.turnaround_time = []
        self.average_waiting_time = 0
        self.average_turnaround_time = 0
        self.total_waiting_time = 0
        self.total_turnaround_time = 0
        self.num_processes = len(processes)
        self.rounds = 0  # To keep track of the number of rounds

    def run(self):
        self.rr()
        self.print_result()
    
    def rr(self):
        while self.processes:
            process = self.processes.pop(0)
            if process.burst_time > self.quantum:
                self.result.append((process.name, self.quantum))
                process.burst_time -= self.quantum
                self.processes.append(process)
                print(f"Processo {process.name} - Tempo restante: {process.burst_time}")
            else:
                self.result.append((process.name, process.burst_time))
                print(f"Processo {process.name} concluído")
            self.rounds += 1
        self.calculate_waiting_time()
        self.calculate_turnaround_time()
        self.calculate_averages()
    
    @staticmethod
    def rr_sort(processes):
        processes.sort(key=lambda x: x.number)
        return processes
    
    def calculate_waiting_time(self):
        for i in range(self.num_processes):
            if i == 0:
                self.waiting_time.append(0)
            else:
                self.waiting_time.append(self.waiting_time[i - 1] + self.result[i - 1][1])
        self.total_waiting_time = sum(self.waiting_time)

    def calculate_turnaround_time(self):
        for i in range(self.num_processes):
            self.turnaround_time.append(self.waiting_time[i] + self.result[i][1])
        self.total_turnaround_time = sum(self.turnaround_time)
    
    def calculate_averages(self):
        self.average_waiting_time = self.total_waiting_time / self.num_processes
        self.average_turnaround_time = self.total_turnaround_time / self.num_processes

    def print_result(self):
        print("Ordem de execução:")
        for process, time in self.result:
            print(f"{process} ({time} U.T.)", end=" -> ")
        print("Tempo médio de espera:", self.average_waiting_time)
        print("Tempo de Retorno Médio:", self.average_turnaround_time)
        print("Rounds totais:", self.rounds)