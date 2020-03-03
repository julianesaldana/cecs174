package firstlabs;

import java.util.Scanner;

public class calculator {
    public static void main(String[]arg){
        Scanner in = new Scanner(System.in);
        while (true) {
            System.out.println("Please select an operation");
            System.out.println("******** menu ********");
            System.out.println("1 - Addition");
            System.out.println("2 - Subtraction");
            System.out.println("3 - Multiplication");
            System.out.println("4 - Division");
            System.out.println("5 - Exit");
            int option = in.nextInt();
            if (option >= 1 && option <= 4){
                System.out.println("Enter the first number:");
                int num1 = in.nextInt();
                System.out.println("Enter the second number:");
                int num2 = in.nextInt();
                switch (option){
                    case 1:
                        int summation = num1 + num2;
                        System.out.println("The result is: " + summation);
                        break;
                    case 2:
                        int subtraction = num1 - num2;
                        System.out.println("The subtraction is: " + subtraction);
                        break;
                    case 3:
                        int multiplication = num1 * num2;
                        System.out.println("The product is: " + multiplication);
                        break;
                    case 4:
                        int division = num1 / num2;
                        System.out.println("The dividend is: " + division);
                        break;
                }
            }
            else {
                System.out.println("Goodbye!");
                break;
            }
        }
    }
}