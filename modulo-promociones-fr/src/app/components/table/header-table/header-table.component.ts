import { Component, OnInit } from '@angular/core';
import { ServiciosService } from '../../../services/planes/servicios.service';
import { CommonModule } from '@angular/common';
import { TiposerviciosService } from '../../../services/planes/tiposervicios.service';
import { TecnologiasService } from '../../../services/planes/tecnologias.service';
import { TariffplanesService } from '../../../services/planes/tariffplanes.service';
import { CiudadService } from '../../../services/places/ciudad.service';
import { ProvinciasService } from '../../../services/places/provincias.service';

@Component({
  selector: 'app-header-table',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './header-table.component.html',
  styleUrl: './header-table.component.scss'
})
export class HeaderTableComponent implements OnInit{
  serviciosData: string[] = [];
  tiposervicioData: string[] = [];
  tecnologiaData: string[] = [];
  planData: string[] = [];
  provinciaData: string[] = [];
  ciudadData: string[] = [];


  constructor(
    private serv: ServiciosService,
    private tise: TiposerviciosService,
    private tecn: TecnologiasService,
    private plan: TariffplanesService,
    private prov: ProvinciasService,
    private city: CiudadService
  ){}

  ngOnInit():void{
    this.Darth_Nihilus_function();
  }

  Darth_Nihilus_function(){
    try{
      this.fetchServiciosData(); this.fecthTipoServiciosData(); 
      this.fecthTecnologiasData(); 
      this.fecthTariffPlanesVariantData(); 
      //this.fecthProvinciaData();
    } catch (error){
      console.log("---------------------------------------------------------------")
      console.log("header-table.compo - Darth_Nihilus_function | Error detectado: ")
      console.log(error)
      console.log("---------------------------------------------------------------")
    }
  }
  private fecthProvinciaData(): void {
    console.log("ProvinciaData");
    this.prov.getProvincias().subscribe((response: any) =>{
      console.log(response); 
      if (response && response.PROVINCIES){
        this.provinciaData = response.PROVINCIES.map((provincia: any) => provincia.PROVINCIES);
        console.log(this.provinciaData); 
      }
    });
  }

  private fecthTariffPlanesVariantData(): void {
    console.log("TariffPlanesVariantData");
    this.plan.getTariffPlanesVariantALL().subscribe((response: any) =>{
      console.log(response); 
      if (response && response.PLANES){
        this.planData = response.PLANES.map((plan: any) => plan.PLANES);
        console.log(this.planData); 
      }
    });
  }

  private fecthTecnologiasData(): void {
    console.log("TecnologiasData");
    this.tecn.getTecnologiasALL().subscribe((response: any) =>{
      console.log(response); 
      if (response && response.TECNOLOGIAS){
        this.tecnologiaData = response.TECNOLOGIAS.map((tecnologia: any) => tecnologia.TECNOLOGIA);
        console.log(this.tecnologiaData); 
      } else {
        console.error("La respuesta no contiene la propiedad 'TECNOLOGIAS'.");
      }
    });
  }

  private fecthTipoServiciosData(): void {
    console.log("TipoServiciosData");
    this.tise.getTipoServicioALL().subscribe((response: any) =>{
      console.log(response); 
      if (response && response.TIPO_SERVICIO){
        this.tiposervicioData = response.TIPO_SERVICIO.map((tipo_servicio: any) => tipo_servicio.TIPO_SERVICIO);
        console.log(this.tiposervicioData); 
      } else {
        console.error("La respuesta no contiene la propiedad 'TIPO_SERVICIO'.");
      }
    });
  }

  private fetchServiciosData(): void {
    console.log("ServiciosData");
    this.serv.getServiciosALL().subscribe((response: any) => {
      console.log(response);
      if (response && response.SERVICIOS) {
        this.serviciosData = response.SERVICIOS.map((servicio: any) => servicio.SERVICIO);
        console.log(this.serviciosData); 
      } else {
        console.error("La respuesta no contiene la propiedad 'SERVICIOS'.");
      }
    });
  }
}