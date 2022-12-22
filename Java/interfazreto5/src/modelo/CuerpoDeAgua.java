package modelo;

public class CuerpoDeAgua extends ObjetoGeografico{
    private String tipoCuerpo;
    private String tipoAgua;
    private Double irca; 

    public CuerpoDeAgua(
            String tipoCuerpo,
            String tipoAgua, 
            Double irca, 
            String nombre, 
            int idcuerpo, 
            String municipio) {
        super(nombre, idcuerpo, municipio);
        this.tipoCuerpo = tipoCuerpo;
        this.tipoAgua = tipoAgua;
        this.irca = irca;
    }

    public Double getIrca() {
        return irca;
    }

    public void setIrca(Double irca) {
        this.irca = irca;
    }

    public String getTipoCuerpo() {
        return tipoCuerpo;
    }

    public void setTipoCuerpo(String tipoCuerpo) {
        this.tipoCuerpo = tipoCuerpo;
    }

    public String getTipoAgua() {
        return tipoAgua;
    }

    public void setTipoAgua(String tipoAgua) {
        this.tipoAgua = tipoAgua;
    }
    
    public String nivel(){
        String riesgo = "";
        if(irca >=0 && irca <=5){
            riesgo = "SIN RIESGO";
        }
        if(irca > 5 && irca <=14){
            riesgo = "BAJO";
        }
        if(irca > 14 && irca <=35){
            riesgo = "MEDIO";
        }
        if(irca >35 && irca <=80){
            riesgo = "ALTO";
        }
        if(irca > 80 && irca <= 100){
            riesgo = "INVIABLE SANITARIAMENTE";
        }
        return riesgo;
    }   
}
