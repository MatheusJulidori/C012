public class Main {
    public static void main(String[] args) {
        System.out.println("Demonstração COM semáforo:");
        ComSemaforo comSemaforoDemo = new ComSemaforo();
        comSemaforoDemo.runDemo();

        System.out.println("\nDemonstração SEM semáforo:");
        SemSemaforo semSemaforoDemo = new SemSemaforo();
        semSemaforoDemo.runDemo();
    }
}
