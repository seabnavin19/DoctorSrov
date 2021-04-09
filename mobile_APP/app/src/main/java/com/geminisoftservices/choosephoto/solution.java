package com.geminisoftservices.choosephoto;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;

public class solution extends AppCompatActivity {
    private Button play;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_solution);
        getSupportActionBar().hide();
        play=findViewById(R.id.video_start);
        play.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                AlertDialog.Builder alertDialog = new AlertDialog.Builder(solution.this);
                final View customLayout = getLayoutInflater().inflate(R.layout.solution, null);
                alertDialog.setView(customLayout);
                AlertDialog alert = alertDialog.create();
                alert.setCanceledOnTouchOutside(false);
                alert.show();

            }
        });
    }
}