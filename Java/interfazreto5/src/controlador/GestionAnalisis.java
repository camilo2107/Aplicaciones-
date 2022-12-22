package controlador;

import java.util.ArrayList;
import modelo.CuerpoDeAgua;
import modelo.DensidadPoblacional;

public class GestionAnalisis {

    public static ArrayList<CuerpoDeAgua> body = new ArrayList<>();
    public static ArrayList<DensidadPoblacional> densidades = new ArrayList<>();

    public static void CrearCuerposAgua(
            String tipoCuerpo,
            String tipoAgua,
            String irca,
            String nombre,
            String IdCuerpo,
            String municipio,
            String densidad
    ) {
        body.add(new CuerpoDeAgua(
                tipoCuerpo,
                tipoAgua,
                Double.parseDouble(irca),
                nombre,
                Integer.parseInt(IdCuerpo),
                municipio));

        densidades.add(new DensidadPoblacional(
                Integer.parseInt(densidad),
                nombre,
                Integer.parseInt(IdCuerpo),
                municipio));
    }
    public static ArrayList<String> calculoNivel() {
        ArrayList<String> listar = new ArrayList<>();
        int cont = 0;
       
        for (int i = 0; i < body.size(); i++) {
            listar.add(body.get(i).nivel() + " "
                    + densidades.get(i).afeccion());
           

            if ("SIN RIESGO".equals(body.get(i).nivel())
                    || "BAJO".equals(body.get(i).nivel())
                    || "MEDIO".equals(body.get(i).nivel())) 
            {
        cont += 1;
    }
}

    listar.add(Integer.toString(cont));
        boolean encontrar = false;
        String a ="";
        for (int i= 0; i < body.size (); i++){
            if(body.get(i).nivel().equals("MEDIO")){
            a += body.get(i).getNombre()+" ";
            encontrar =true;
        }
}
        listar.add(a);
        if(encontrar==false)
            listar.add("NA");
        
    
        double menor = body.get(0).getIrca();
        String nombre = body.get(0).getNombre();
        int identificador = body.get(0).getIdcuerpo();
        for(int i = 0; i < body.size(); i++){
            if(body.get(i).getIrca()<menor){
            menor = body.get(i).getIrca();
            nombre= body.get(i).getNombre();
            identificador = body.get(i).getIdcuerpo();
            }
        }
        listar.add(nombre +" "+ identificador);
        return listar; 
    }
}
