package sample.Model;

public class Person {
    private String name;
    private String surname;
    private String street = "no data";
    private String city = "no data";
    private int postal_code = 0;

    public Person(String name, String surname, String street, String city, int postal_code) {
        super();
        this.name = name;
        this.surname = surname;
        this.city = city;
        this.postal_code = postal_code;
        this.street = street;
    }



    public void setName(String name) {
        this.name = name;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }

    public void setStreet(String street) {
        this.street = street;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public void setPostal_code(int postal_code) {
        this.postal_code = postal_code;
    }

    public String getName() {
        return name;
    }

    public String getSurname() {
        return surname;
    }

    public String getStreet() {
        return street;
    }

    public String getCity() {
        return city;
    }

    public int getPostal_code() {
        return postal_code;
    }
}
