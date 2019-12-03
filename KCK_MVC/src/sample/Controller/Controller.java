package sample.Controller;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import sample.Model.Person;
import sample.Main;


import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;

import java.io.IOException;

public class Controller{

    public static ObservableList<Person> osoby = FXCollections.observableArrayList(
            new Person("Tomasz", "Majcher", "Młynarska", "Skierniewice", 96100),
            new Person("Adam", "Wójt", "Nieśmiała", "Łódź", 45678),
            new Person("Maciej", "Kupczak", "Pomarańczowa", "Warszawa", 12345),
            new Person("Izabela", "Mazgaja", "Brzozowa", "Poznań", 98272),
            new Person("Edward", "Nikt", "Cicha", "Szczecin", 46812),
            new Person("Magdalena", "Kołatka", "Zła", "Wrocław", 94632),
            new Person("Bonifacy", "Kleofas", "Dobra", "Kraków", 75913)
    );

    public static int selectedIndex;

    @FXML   private TableView<Person> table;
    @FXML   private TableColumn<Person, String> table_name;
    @FXML   private TableColumn<Person, String> table_surname;

    @FXML   private Label name;
    @FXML   private Label surname;
    @FXML   private Label street;
    @FXML   private Label city;
    @FXML   private Label postal_code;

    private void showPersonDetails(Person p){
        if(p != null){
            name.setText(p.getName());
            surname.setText(p.getSurname());
            street.setText(p.getStreet());
            city.setText(p.getCity());
            postal_code.setText(Integer.toString(p.getPostal_code()));
        }
        else{
            name.setText("");
            surname.setText("");
            street.setText("");
            city.setText("");
            postal_code.setText("");
        }
    }

    @FXML
    private void deletePerson(){
        int selectedIndex = table.getSelectionModel().getSelectedIndex();
        table.getItems().remove(selectedIndex);
    }

    @FXML
    private void openAddPerson() throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("add_person.fxml"));
        Parent root1 = fxmlLoader.load();
        Stage stage = new Stage();
        stage.setTitle("Add person");
        stage.setScene(new Scene(root1, 260, 400));
        stage.setResizable(false);
        stage.show();
    }

    @FXML
    private void openEditPerson() throws IOException {
        selectedIndex = table.getSelectionModel().getSelectedIndex();
        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("edit_person.fxml"));
        Parent root1 = fxmlLoader.load();
        Stage stage = new Stage();
        stage.setTitle("Edit person");
        stage.setScene(new Scene(root1, 260, 400));
        stage.setResizable(false);
        stage.show();
    }

    public void initialize(){
        table_name.setCellValueFactory(new PropertyValueFactory<>("name"));
        table_surname.setCellValueFactory(new PropertyValueFactory<>("surname"));

        table.setItems(osoby);
        showPersonDetails(null);
        table.getSelectionModel().selectedItemProperty()
                .addListener((observable, oldValue, newValue) -> showPersonDetails(newValue));
    }
}
