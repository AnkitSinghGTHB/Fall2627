public class FibonacciRecursive {
    public static int calculateFibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        return calculateFibonacci(n - 1) + calculateFibonacci(n - 2);
    }

    public static void main(String[] args) {
        int terms = 10;
        System.out.println("Fibonacci series up to " + terms + " terms:");
        for (int i = 0; i < terms; i++) {
            System.out.print(calculateFibonacci(i) + " ");
        }
        System.out.println();
    }
}