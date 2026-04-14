public class palindrome{
    public static void main(String[] args) {
        String s = "madam";
        String s2 = "";
        for (int i = s.length()-1; i>=0; i--)
        {
            s2 = s2 + s.charAt(i);
        }
        if (s.isequal(s2){
           System.out.println("given string palindrome"); 
        }
        else{
            System.out.println("given string is not a palindrome");
        }
    }
}
