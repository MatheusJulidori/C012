public class SemSemaforo {
    public void runDemo() {
        BankAccountSemSemaforo account = new BankAccountSemSemaforo(1000);

        Thread depositThread = new Thread(() -> {
            for (int i = 0; i < 5; i++) {
                account.deposit(100);
            }
        });

        Thread withdrawThread = new Thread(() -> {
            for (int i = 0; i < 5; i++) {
                account.withdraw(200);
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

        System.out.println("Saldo final (SEM semáforo): " + account.getBalance());
    }
}

class BankAccountSemSemaforo {
    private int balance;

    public BankAccountSemSemaforo(int initialBalance) {
        this.balance = initialBalance;
    }

    public void deposit(int amount) {
        int newBalance = balance + amount;
        try {
            Thread.sleep(100);
            balance = newBalance;
            System.out.println("Depósito de " + amount + " realizado. Novo saldo: " + balance);
        } catch (InterruptedException e) {
            e.printStackTrace();
    }
}

    public void withdraw(int amount) {
        try { 
            if (balance >= amount) {
            int newBalance = balance - amount;
                Thread.sleep(100);
                balance = newBalance;
                System.out.println("Saque de " + amount + " realizado. Novo saldo: " + balance);
            } else {
                System.out.println("Saldo insuficiente para saque de " + amount + ". Saldo atual: " + balance);
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public int getBalance() {
        return balance;
    }
}

