package com.tarek.myvault;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import d.m;
import i.c;
import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStream;

public class MainActivity extends m {
    public final void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        setContentView((int) R.layout.activity_main);
        File file = new File(getCacheDir() + "/vault.enc");
        if (!file.exists()) {
            try {
                InputStream open = getAssets().open("vault.enc");
                byte[] bArr = new byte[open.available()];
                open.read(bArr);
                open.close();
                FileOutputStream fileOutputStream = new FileOutputStream(file);
                fileOutputStream.write(bArr);
                fileOutputStream.close();
                ((Button) findViewById(R.id.btnSubmit)).setOnClickListener(new c(this, (EditText) findViewById(R.id.editTextOTP), 2));
            } catch (Exception e3) {
                throw new RuntimeException(e3);
            }
        }
    }
}
