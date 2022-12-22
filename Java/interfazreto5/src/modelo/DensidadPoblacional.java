package modelo;
public class DensidadPoblacional extends ObjetoGeografico{
    private int numhabitantes;

    public DensidadPoblacional(
            int numhabitantesp, 
            String nombre, 
            int idcuerpo, 
            String municipio) {
        super(nombre, idcuerpo, municipio);
        this.numhabitantes = numhabitantesp;

    }

    public int getNumhabitantesp() {
        return numhabitantes;
    }

    public void setNumhabitantesp(int numhabitantesp) {
        this.numhabitantes = numhabitantesp;
    }
    
    public int afeccion(){
        int nivel=0; 
        if(numhabitantes<10000)
            nivel=0;
        if(numhabitantes>=10000 && numhabitantes<=50000)
            nivel=1;
        if(numhabitantes>50000)
            nivel = 2;
        return nivel;
    }
 
}
