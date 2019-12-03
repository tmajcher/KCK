package sample;

public class Model {
    private String nazwa;
    private int zarobki;

    Model(String nazwa, int zarobki){
        this.nazwa = nazwa;
        this.zarobki = zarobki;
    }

    public String getNazwa() {
        return nazwa;
    }

    public void setNazwa(String nazwa) {
        this.nazwa = nazwa;
    }

    public int getZarobki() {
        return zarobki;
    }

    public void setZarobki(int zarobki) {
        this.zarobki = zarobki;
    }
}
