
//java program to simulate rock paper scissors
import java.util.*;

public class rps {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        // use .equals() instead of == for string comparison
        if (s == "rock") {
            System.out.println("Paper");
        } else if (s == "paper") {
            System.out.println("Scissors");
        } else if (s == "scissors") {
            System.out.println("Rock");
        } else {
            System.out.println("Invalid");
        }
        sc.close();
    }
}