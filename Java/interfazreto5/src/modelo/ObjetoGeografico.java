package modelo;
public class ObjetoGeografico {
    
    private String nombre;
    private int idcuerpo;
    private String municipio;

    public ObjetoGeografico(
            String nombre, 
            int idcuerpo, 
            String municipio) {
        this.nombre = nombre;
        this.idcuerpo = idcuerpo;
        this.municipio = municipio;
    }

    public String getMunicipio() {
        return municipio;
    }

    public void setMunicipio(String municipio) {
        this.municipio = municipio;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getIdcuerpo() {
        return idcuerpo;
    }

    public void setIdcuerpo(int idcuerpo) {
        this.idcuerpo = idcuerpo;
    }

}
