package firstlabs;

import java.util.Scanner;

public class javalab515 {
    public static void main(String[]arg)
    { Scanner in = new Scanner(System.in);
    System.out.println("Enter the income: ");
    float income = in.nextFloat();
    double tax = 0;
    if (income <= 50000) {
        tax = income * 0.01;
    } else if (income > 50000 && income <= 75000){
        tax = (income - 50000) * 0.02 + 500;
    } else if (income > 75000 && income <= 100000){
        tax = (income - 75000) * 0.03 + 1000;
    } else if (income > 100000 && income <= 250000){
        tax = (income - 100000) * 0.04 + 1750;
    } else if (income > 250000){
        tax = (income - 250000) * 0.05 + 7750;
    }
    System.out.println("The tax payable would be: " + tax);
    }
    }