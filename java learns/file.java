import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;


public class file {
    public static void main(String[] args) {
         try{
            File f = new File("Example.txt");
            FileWriter fw = new FileWriter(f);
            fw.write("the first project");
            fw.close();
         }
         catch(Exception e){
            System.out.println("file not fetch");
         }
          try{
            File f1 = new File("Example.txt");
            FileReader i = new FileReader(f1);
            while (i.hasNextLine()) {
                System.out.print("output console: ");
                System.out.println(i.nextLine());
            }
            i.close();
         }
         catch(Exception e){
            System.out.println("file not fetch");
         }
        
    }
}
