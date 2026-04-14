import java.util.Scanner;

class for_loop{
    public static void main( String[]args){
        Scanner scan=new Scanner(System.in);
        int a=scan.nextInt();
        int b=scan.nextInt();
        for(int i=a;i<=b;i=i+1){
            if(i%3==0 && i%5==0){
                 System.out.println(i);
            }
        }
    }
}