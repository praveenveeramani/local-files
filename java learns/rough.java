class rough {
    String name;
    int age;

    public void display(){
        System.out.println("Name: " + name + " Age: " + age);
    }
    // rough(String a, int n){
    //     name = a;
    //     age = n;

    // }
    void set_value(String s , int n){
        
        name = s;
        if (n<18){
            throw new ArithmeticException("invalid age");
        }
        else{
            age = n;
        }

    }
    
}
class m{

    public static void main(String[] args) {
        rough obj = new rough();
        try{
            obj.set_value("prvn", 15);
        }
        catch(ArithmeticException e){
            System.out.println(e);
        }
        obj.display();
    }

}