import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class serversock {
    public static void main(String[] args) throws IOException {
        ServerSocket ss = new ServerSocket(9999);
        Socket s = ss.accept();

        DataOutputStream dt = new DataOutputStream(s.getOutputStream());
        dt.writeUTF(" Unnaku second largest theriuma" );
        dt.flush();
        dt.close();

        DataInputStream di = new DataInputStream(s.getInputStream());
        String msg = di.readUTF();
        System.out.println(msg);

    }
}
