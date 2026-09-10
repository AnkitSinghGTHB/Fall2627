import java.util.*;

// HackerRank - FOP Course 1 - Series - Number Transformation Challenge for Game Developement
public class Solution1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.print(n);
        while (n != 1) {
            if (n % 2 == 0) {
                n /= 2;
            } else {
                n = (n * 3) + 1;
            }
            System.out.print(" " + n);
        }
        sc.close();
    }
}