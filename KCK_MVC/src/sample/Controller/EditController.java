package sample.Controller;

import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.fxml.FXML;
import javafx.stage.Stage;
import sample.Model.Person;

public class EditController {

    @FXML   private TextField nameEdit;
    @FXML   private TextField surnameEdit;
    @FXML   private TextField streetEdit;
    @FXML   private TextField cityEdit;
    @FXML   private TextField postalcodeEdit;

    @FXML   private Button okEdit;
    @FXML   private Button cancelEdit;


    public void initialize(){
        nameEdit.setText(Controller.osoby.get(Controller.selectedIndex).getName());
        surnameEdit.setText(Controller.osoby.get(Controller.selectedIndex).getSurname());
        streetEdit.setText(Controller.osoby.get(Controller.selectedIndex).getStreet());
        cityEdit.setText(Controller.osoby.get(Controller.selectedIndex).getCity());
        postalcodeEdit.setText(Integer.toString(Controller.osoby.get(Controller.selectedIndex).getPostal_code()));
    }

    @FXML public void editPerson(){
        String name, surname, city, street;
        int postalcode;
        name = nameEdit.getText();
        surname = surnameEdit.getText();
        city = cityEdit.getText();
        street = streetEdit.getText();
        postalcode = Integer.parseInt(postalcodeEdit.getText());
        Controller.osoby.get(Controller.selectedIndex).setName(name);
        Controller.osoby.get(Controller.selectedIndex).setSurname(surname);
        Controller.osoby.get(Controller.selectedIndex).setStreet(street);
        Controller.osoby.get(Controller.selectedIndex).setCity(city);
        Controller.osoby.get(Controller.selectedIndex).setPostal_code(postalcode);

        Stage stage = (Stage) okEdit.getScene().getWindow();
        stage.close();
    }

    @FXML public void cancel_edit(){
        Stage stage = (Stage) cancelEdit.getScene().getWindow();
        stage.close();
    }
}
