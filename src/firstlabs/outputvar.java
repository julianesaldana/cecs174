package firstlabs;

import java.util.Scanner;

public class outputvar {
    public static void main(String[]arg)
    { Scanner in = new Scanner(System.in);
    System.out.println("Enter an integer: ");
    int int1 = in.nextInt();
    System.out.println("You entered: " + int1);
    System.out.println(int1 + " squared is " + Math.pow(int1, 2));
    System.out.println(int1 + " cubed is " + Math.pow(int1, 3));
    System.out.println("Enter another integer: ");
    int int2 = in.nextInt();
    System.out.println(int1 + " + " + int2 + " is " + int1+int2);
    System.out.println(int1 + " * " + int2 + " is " + int1*int2);
    in.close();
    }
}
