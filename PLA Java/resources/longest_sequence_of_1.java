import java.util.*;

public class longest_sequence_of_1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int maxc = 0;
        int count = 0;
        while (n > 0) {
            int r = n % 10;
            if (r == 1) {
                count++;
            } else {
                maxc = Math.max(maxc, count);
                count = 0;
            }
            n /= 10;
        }
        // final pass i forgot
        maxc = Math.max(maxc, count);
        System.out.println(maxc);
        sc.close();
    }
}
