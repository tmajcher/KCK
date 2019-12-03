package sample;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.chart.BarChart;
import javafx.scene.chart.XYChart;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;

public class Controller {
    public static XYChart.Series<String, Integer> wykres = new XYChart.Series<>();
    public static ObservableList<Model> lista = FXCollections.observableArrayList(
            new Model("Styczeń", 5000),
            new Model("Luty", 2000),
            new Model("Marzec", 1000),
            new Model("Kwiecień", 2000),
            new Model("Maj", 1000),
            new Model("Czerwiec", 3000),
            new Model("Lipiec", 2000),
            new Model("Sierpień", 3000),
            new Model("Wrzesień", 1000),
            new Model("Paźdzernik", 4000),
            new Model("Listopad", 3500),
            new Model("Grudzień", 6000)
    );

    @FXML private TableView<Model> table;
    @FXML private TableColumn<Model, String> tableMiesiac;
    @FXML private TableColumn<Model, Integer> tableZarobki;
    @FXML private TextField textFieldMiesiac;
    @FXML private TextField textFieldZarobki;
    @FXML private BarChart<String, Integer> barChart;

    private void showInTextFields(Model p){
        if(p != null){
            textFieldMiesiac.setText(p.getNazwa());
            textFieldZarobki.setText(String.valueOf(p.getZarobki()));
        }
        else{
            textFieldMiesiac.setText("");
            textFieldZarobki.setText("");
        }
    }

    @FXML
    private void actualize(){
        int selectedIndex = table.getSelectionModel().getSelectedIndex();
        table.getItems().get(selectedIndex).setNazwa(textFieldMiesiac.getText());
        table.getItems().get(selectedIndex).setZarobki(Integer.parseInt(textFieldZarobki.getText()));
        table.refresh();

        wykres.getData().removeAll();
        for (int i = 0; i < lista.size() ; i++) {
            wykres.getData().add(new XYChart.Data<>(lista.get(i).getNazwa(), lista.get(i).getZarobki()));
        }
    }

    public void initialize(){
        tableMiesiac.setCellValueFactory(new PropertyValueFactory<>("nazwa"));
        tableZarobki.setCellValueFactory(new PropertyValueFactory<>("zarobki"));
        table.setItems(lista);

        for (int i = 0; i < lista.size() ; i++) {
            wykres.getData().add(new XYChart.Data<>(lista.get(i).getNazwa(), lista.get(i).getZarobki()));
        }
        barChart.getData().add(wykres);

        showInTextFields(null);
        table.getSelectionModel().selectedItemProperty()
                .addListener((observable, oldValue, newValue) -> showInTextFields(newValue));
    }





}
