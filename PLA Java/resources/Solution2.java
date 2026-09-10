import java.util.*;

public class Solution2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum = 0;
        // lets break n into sum of 3 and 2
        // then efficiency is the multiplication of the broken down numbers
        // e.g. 10=3+3+2+2 -> 3*3*2*2=36
        int a = n / 3;
        int b = n % 3;
        if (b == 1) {
            a--;
            b = 2;
        } else if (b == 2) {
            b = 1;
        }
        sum = 1;
        for (int i = 0; i < a; i++) {
            sum *= 3;
        }
        for (int i = 0; i < b; i++) {
            sum *= 2;
        }
        System.out.println(sum);
        sc.close();
    }
}
