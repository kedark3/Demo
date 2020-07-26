package sample;

import com.sun.deploy.util.StringUtils;
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.geometry.Orientation;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.CheckBox;
import javafx.scene.control.Label;
import javafx.scene.layout.FlowPane;
import javafx.stage.Stage;

public class Main extends Application  {

    private Label title;
    private Label response;
    private Label selected;

    private CheckBox gozine1;
    private CheckBox gozine2;
    private CheckBox gozine3;
    private CheckBox gozine4;
    private String friuts ;
    String temp;
    String new_string;

    @Override
    public void start(Stage primaryStage) throws Exception{
        primaryStage.setTitle("Favourit Fruits ");

        title = new Label("which fruit so you like most ?");
        selected = new Label("selected : ");
        response = new Label("");

        gozine1 = new CheckBox("Banana");
        gozine2 = new CheckBox("peaches");
        gozine3 = new CheckBox("apple");
        gozine4 = new CheckBox("orange");



        FlowPane flowPane = new FlowPane(Orientation.VERTICAL  , 5 , 5);
        flowPane.setAlignment(Pos.CENTER);


        flowPane.getChildren().add(title);
        flowPane.getChildren().addAll(gozine1 , gozine2 , gozine3 , gozine4 ,
                 response ,selected);




        Scene scene = new Scene(flowPane , 400 , 250);
        primaryStage.setScene(scene);
        primaryStage.show();

        gozine1.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                    if(gozine1.isSelected()) {
                        selected.setText(selected.getText() + " " + gozine1.getText());
                        response.setText(gozine1.getText() + " selected");
                    }
                    else {
                        temp = selected.getText();
                        new_string = temp.replace(" " + gozine1.getText(), "");
                        selected.setText(new_string);
                        response.setText(gozine1.getText() + " cleared");
                    }
            }
        });

        gozine2.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                if(gozine2.isSelected()) {
                    selected.setText(selected.getText() + " " + gozine2.getText());
                    response.setText(gozine2.getText() + " selected");
                }
                else {
                    temp = selected.getText();
                    new_string = temp.replace(" " + gozine2.getText(), "");
                    selected.setText(new_string);
                    response.setText(gozine2.getText() + " cleared");
                }
            }
        });

        gozine3.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                if(gozine3.isSelected()) {
                    selected.setText(selected.getText() + " " + gozine3.getText());
                    response.setText(gozine3.getText() + " selected");
                }
                else {
                    temp = selected.getText();
                    new_string = temp.replace(" " + gozine3.getText(), "");
                    selected.setText(new_string);
                    response.setText(gozine3.getText() + " cleared");
                }
            }
        });

        gozine4.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                if(gozine4.isSelected()) {
                    selected.setText(selected.getText() + " " + gozine4.getText());
                    response.setText(gozine4.getText() + " selected");
                }
                else {
                    temp = selected.getText();
                    new_string = temp.replace(" " + gozine4.getText(), "");
                    selected.setText(new_string);
                    response.setText(gozine4.getText() + " cleared");
                }
            }
        });

    }


    public static void main(String[] args) {
        launch(args);
    }



}

