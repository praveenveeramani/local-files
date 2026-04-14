import java.util.Scanner;

class ternary{
    public static void main( String[]args){
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        String result =(a>b)? a+"is greatest number":b+"is greatest number";
        System.out.println(result);
    }
}