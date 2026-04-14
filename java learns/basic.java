import java.util.Scanner;

class basic{
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);
        String Name = scan.nextLine();
        double Mark = scan.nextDouble();
        scan.nextLine();
        String Department = scan.nextLine();
        System.out.println("Name is "+Name);
        System.out.println("Mark precentage is "+Mark/5+" %");
        System.out.println("Department is "+Department);
    
    }
}