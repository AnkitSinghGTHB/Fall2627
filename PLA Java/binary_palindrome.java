import java.util.*;

public class binary_palindrome {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int mul = 1;
        int b = 0;
        int br = 0;
        while (n > 0) {
            int r = n % 2;
            b = (mul * r) + b;
            br = (br * 10) + r;
            mul *= 10;
            n /= 2;
        }
        System.out.println((b == br) ? "Binary Palindrome" : "Not a Binary Palindrome");
        sc.close();
    }
}
