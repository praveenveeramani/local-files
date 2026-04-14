import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

public class sock {
    public static void main(String[] args) throws IOException {
        Socket sk = new Socket("localhost",9999);

        DataInputStream di = new DataInputStream(sk.getInputStream());
        String msg = di.readUTF();
        System.out.println(msg);

        DataOutputStream dt = new DataOutputStream(sk.getOutputStream());
        dt.writeUTF("illa");
        dt.flush();
        dt.close();

    }
}
