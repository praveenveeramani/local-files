import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;


 public class sample{

    sample(){
        Frame f = new Frame("dashboard");
        TextField t = new TextField("enter words");
        TextArea ta = new TextArea("about");
        Label l = new Label("please login");
        Choice c = new Choice();
        c.add("india");
        c.add("usa");

        Button btu = new Button("click me");

        ActionListener sl = new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                System.out.println(t.getText());
                System.out.println(ta.getText());
            }
        };

        btu.addActionListener(sl);

        f.add(t);
        f.add(ta);
        f.add(l);
        f.add(btu);
        f.add(c);
        
        f.setLayout(new FlowLayout());
        f.setVisible(true);
        f.setSize(900,800);
        
    }
    public static void main(String[] args) {
        new sample();
    }
}