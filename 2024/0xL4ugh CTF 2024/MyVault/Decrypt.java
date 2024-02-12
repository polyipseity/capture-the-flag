import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class Decrypt {
  public static void main(String[] args) throws IOException {
    var encrypted = Files.readAllBytes(Paths.get("vault.enc"));
    for (var otp = 0; otp < 10000; ++otp) {
      String obj3 = String.valueOf(otp);
      String sb = new StringBuilder(obj3).reverse().toString();
      SecretKeySpec secretKeySpec = new SecretKeySpec((obj3 + sb + obj3 + sb).getBytes(), "AES");
      byte[] doFinal;
      try {
        Cipher instance = Cipher.getInstance("AES");
        instance.init(2, secretKeySpec);
        doFinal = instance.doFinal(encrypted);
      } catch (Exception ex) {
        continue;
      }
      Files.write(Paths.get("vault" + otp + ".txt"), doFinal);
      System.out.printf("A possible OTP is %d%n", otp);
    }
  }
}
