import java.util.concurrent.Semaphore;

public class ComSemaforo {
    public void runDemo() {
        BankAccountComSemaforo account = new BankAccountComSemaforo
        (1000);
        Semaphore semaphore = new Semaphore(1);

        Thread depositThread = new Thread(() -> {
            for (int i = 0; i < 5; i++) {
                account.deposit(100, semaphore);
            }
        });

        Thread withdrawThread = new Thread(() -> {
            for (int i = 0; i < 5; i++) {
                account.withdraw(200, semaphore);
            }
        });

        depositThread.start();
        withdrawThread.start();

        try {
            depositThread.join();
            withdrawThread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("Saldo final (COM semáforo): " + account.getBalance());
    }
}

class BankAccountComSemaforo {
    private int balance;

    public BankAccountComSemaforo(int initialBalance) {
        this.balance = initialBalance;
    }

    public void deposit(int amount, Semaphore semaphore) {
        try {
            semaphore.acquire();
            int newBalance = balance + amount;
            Thread.sleep(100);
            balance = newBalance;
            System.out.println("Depósito de " + amount + " realizado. Novo saldo: " + balance);
            semaphore.release();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void withdraw(int amount, Semaphore semaphore) {
        try {
            semaphore.acquire();
            if (balance >= amount) {
                int newBalance = balance - amount;
                Thread.sleep(100);
                balance = newBalance;
                System.out.println("Saque de " + amount + " realizado. Novo saldo: " + balance);
            } else {
                System.out.println("Saldo insuficiente para saque de " + amount + ". Saldo atual: " + balance);
            }
            semaphore.release();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public int getBalance() {
        return balance;
    }
}
