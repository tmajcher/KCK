package sample.Controller;

import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.fxml.FXML;
import javafx.stage.Stage;
import sample.Model.Person;

public class AddController {

    @FXML   private TextField textName;
    @FXML   private TextField textSurname;
    @FXML   private TextField textStreet;
    @FXML   private TextField textCity;
    @FXML   private TextField intPostalCode;

    @FXML   private Button ok_add;
    @FXML   private Button cancel_add;


    @FXML public void addPerson(){
        String name, surname, city, street;
        int postalcode;
        name = textName.getText();
        surname = textSurname.getText();
        city = textCity.getText();
        street = textStreet.getText();
        postalcode = Integer.parseInt(intPostalCode.getText());
        Person person = new Person(name, surname, street, city, postalcode);
        Controller.osoby.add(person);
        Stage stage = (Stage) ok_add.getScene().getWindow();
        stage.close();
    }

    @FXML public void cancel_add(){
        Stage stage = (Stage) cancel_add.getScene().getWindow();
        stage.close();
    }
}