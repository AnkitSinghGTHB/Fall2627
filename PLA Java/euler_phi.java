import java.util.*;

public class euler_phi {
    // euler's phi algo
    // factorize n into its distinct prime factors, with their corresponding powers
    // for reach prime factor p, compute p^(k-1) and p^k, where k is the power of p
    // in te prime factorization of n
    // compute the product of all (p-1)*p^(k-1) for each prime factor p
    // return the product from step 3 as the value of euler's totient function
    // phi(n)

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int result = n;
        for (int i = 2; i <= n / i; i++) {
            if (n % i == 0) {
                while (n % i == 0)
                    n /= i;
                result -= result / i;
            }
        }
        if (n > 1)
            result -= result / n;
        System.out.println(result);
        sc.close();
    }
}
