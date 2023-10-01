class SJF:
    def __init__(self, processes):
        self.processes = processes
        self.result = []
        self.waiting_time = []
        self.turnaround_time = []
        self.average_waiting_time = 0
        self.average_turnaround_time = 0
        self.total_waiting_time = 0
        self.total_turnaround_time = 0
        self.num_processes = len(processes)

    def run(self):
        self.sjf()
        self.print_result()
    
    def sjf(self):
        self.processes = SJF.sjf_sort(self.processes)
        for process in self.processes:
            self.result.append((process.name, process.burst_time))
        self.calculate_waiting_time()
        self.calculate_turnaround_time()
        self.calculate_averages()

    def sjf_sort(processes):
        processes.sort(key=lambda x: x.burst_time)
        return processes

    def calculate_waiting_time(self):
        for i in range(self.num_processes):
            if i == 0:
                self.waiting_time.append(0)
            else:
                self.waiting_time.append(self.result[i - 1][1] + self.waiting_time[i - 1])
        self.total_waiting_time = sum(self.waiting_time)

    def calculate_turnaround_time(self):
        for i in range(self.num_processes):
            self.turnaround_time.append(self.waiting_time[i] + self.result[i][1])
        self.total_turnaround_time = sum(self.turnaround_time)
    
    def calculate_averages(self):
        self.average_waiting_time = self.total_waiting_time / self.num_processes
        self.average_turnaround_time = self.total_turnaround_time / self.num_processes

    def print_result(self):
        print("Processo\tBurst Time\tTempo de espera\tTempo de retorno")
        for i in range(self.num_processes):
            print(f"{self.result[i][0]}\t{self.result[i][1]}\t\t{self.waiting_time[i]}\t\t{self.turnaround_time[i]}")
        print(f"Tempo de espera médio: {self.average_waiting_time}")
        print(f"Tempo de retorno médio: {self.average_turnaround_time}")
        print(f"Tempo de espera total: {self.total_waiting_time}")
        print(f"Total de retorno total: {self.total_turnaround_time}")
