package i;

import android.view.KeyEvent;
import android.view.View;
import android.view.Window;
import android.widget.EditText;
import android.widget.Toast;
import com.tarek.myvault.MainActivity;
import h.a;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public final class c implements View.OnClickListener {

    /* renamed from: a  reason: collision with root package name */
    public final /* synthetic */ int f2015a;

    /* renamed from: b  reason: collision with root package name */
    public final Object f2016b;

    /* renamed from: c  reason: collision with root package name */
    public final /* synthetic */ Object f2017c;

    public /* synthetic */ c(KeyEvent.Callback callback, Object obj, int i3) {
        this.f2015a = i3;
        this.f2017c = callback;
        this.f2016b = obj;
    }

    public final void onClick(View view) {
        String str;
        int i3 = this.f2015a;
        Object obj = this.f2017c;
        Object obj2 = this.f2016b;
        switch (i3) {
            case 0:
                ((g.c) obj2).a();
                return;
            case 1:
                c4 c4Var = (c4) obj;
                Window.Callback callback = c4Var.f2031k;
                if (callback != null && c4Var.f2032l) {
                    callback.onMenuItemSelected(0, (a) obj2);
                    return;
                }
                return;
            default:
                String obj3 = ((EditText) obj2).getText().toString();
                MainActivity mainActivity = (MainActivity) obj;
                mainActivity.getClass();
                try {
                    String sb = new StringBuilder(obj3).reverse().toString();
                    File file = new File(mainActivity.getCacheDir(), "vault.txt");
                    File file2 = new File(mainActivity.getCacheDir(), "vault.enc");
                    SecretKeySpec secretKeySpec = new SecretKeySpec((obj3 + sb + obj3 + sb).getBytes(), "AES");
                    Cipher instance = Cipher.getInstance("AES");
                    instance.init(2, secretKeySpec);
                    FileInputStream fileInputStream = new FileInputStream(file2);
                    byte[] bArr = new byte[((int) file2.length())];
                    fileInputStream.read(bArr);
                    byte[] doFinal = instance.doFinal(bArr);
                    FileOutputStream fileOutputStream = new FileOutputStream(file);
                    fileOutputStream.write(doFinal);
                    fileInputStream.close();
                    fileOutputStream.close();
                    str = "Congrats!";
                } catch (Exception unused) {
                    str = "Incorrect OTP";
                }
                Toast.makeText(mainActivity, str, 0).show();
                return;
        }
    }

    public c(c4 c4Var) {
        this.f2015a = 1;
        this.f2017c = c4Var;
        this.f2016b = new a(c4Var.f2021a.getContext(), c4Var.f2028h);
    }
}
