import { Injectable } from '@angular/core';
import { ServiciosService } from '../planes/servicios.service';
import { TiposerviciosService } from '../planes/tiposervicios.service';
import { TariffplanesService } from '../planes/tariffplanes.service';
import { TecnologiasService } from '../planes/tecnologias.service';
import { Servicios } from '../../interfaces/planes/servicios.interface';
import { TipoServicios } from '../../interfaces/planes/tiposervicios.interface';
import { Tecnologias } from '../../interfaces/planes/tecnologias.interface';
import { TariffPlanesVariant } from '../../interfaces/planes/tariffplanes.interface';
import { CommunicationDataService } from '../communication/communicationData.service';

@Injectable({
  providedIn: 'root'
})
export class FdPlanesService {

  serviciosData: Servicios[] = [];
  tiposervicioData: TipoServicios[] = [];
  tecnologiaData: Tecnologias[] = [];
  planData: TariffPlanesVariant[] = [];
  
  constructor(
    private serv: ServiciosService,
    private tise: TiposerviciosService,
    private tecn: TecnologiasService,
    private plan: TariffplanesService,
    private comData: CommunicationDataService
  ) { }

  switchFD(id: string){
    switch(id){
      case 'TISE':
        this.fetchDataServicio();
      break;
      case 'RED':
        this.fetchDataServicio();
        this.fetchDataTipoServicio();
      break;
      case 'PLAN': case'PROV': case 'CITY': case'SECT' :
        this.fetchDataServicio();
        this.fetchDataTipoServicio();
        this.fetchDataTecnologias();
      break;
      default:
        console.log("Opcion no reconocida: "+id);
        break;
    }
  }

  fetchDataServicio(){
    console.log("ServiciosData");
    this.serv.getServiciosALL().subscribe((response: any) => {
      console.log(response);
      if (response && response.SERVICIOS) {
        this.serviciosData = response.SERVICIOS.map((servicio: any) => servicio.SERVICIO);
        console.log(this.serviciosData); 
        this.comData.sendDataServicio(this.serviciosData);
      } else {
        console.error("La respuesta no contiene la propiedad 'SERVICIOS'.");
      }
    });
  }

  fetchDataTipoServicio(){
    console.log("TipoServiciosData");
    this.tise.getTipoServicioALL().subscribe((response: any) =>{
      console.log(response); 
      if (response && response.TIPO_SERVICIO){
        this.tiposervicioData = response.TIPO_SERVICIO.map((tipo_servicio: any) => tipo_servicio.TIPO_SERVICIO);
        console.log(this.tiposervicioData); 
        this.comData.sendDataTipoServicios(this.tiposervicioData);
      } else {
        console.error("La respuesta no contiene la propiedad 'TIPO_SERVICIO'.");
      }
    });
  }

  fetchDataTecnologias(){
    console.log("TecnologiasData");
    this.tecn.getTecnologiasALL().subscribe((response: any) =>{
      console.log(response); 
      if (response && response.TECNOLOGIAS){
        this.tecnologiaData = response.TECNOLOGIAS.map((tecnologia: any) => tecnologia.TECNOLOGIA);
        console.log(this.tecnologiaData); 
        this.comData.sendDataTecnologias(this.tecnologiaData);
      } else {
        console.error("La respuesta no contiene la propiedad 'TECNOLOGIAS'.");
      }
    });
  }
  
  fetchDataTariffPlanVariant(servicio: string, tipoServicio: string, tecnologia: string){
    console.log("TariffPlanesVariantData");
    this.plan.getTariffPlanesVariantALL(servicio, tipoServicio, tecnologia).subscribe((response: any) =>{
      console.log(response); 
      if (response && response.PLANES){
        this.planData = response.PLANES.map((plan: any) => {
          return {
            TARIFFPLANVARIANTID: plan.TARIFFPLANVARIANTID,
            TARIFFPLANVARIANT: plan.TARIFFPLANVARIANT
          };
        });
        console.log(this.planData); 
        this.comData.sendDataPlanes(this.planData);
      }
    });
  }

  //Retorno de Informacion Directa

  
}
