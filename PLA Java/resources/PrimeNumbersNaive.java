public class PrimeNumbersNaive {
    public static void printPrimesInRange(int start, int end) {
        for (int i = start; i <= end; i++) {
            if (i <= 1) {
                continue;
            }
            boolean isPrime = true;
            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                System.out.print(i + " ");
            }
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int start = 10;
        int end = 50;
        System.out.println("Prime numbers between " + start + " and " + end + ":");
        printPrimesInRange(start, end);
    }
}