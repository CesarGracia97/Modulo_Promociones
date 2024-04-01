import { Component, OnInit } from '@angular/core';
import { ServiciosService } from '../../../services/planes/servicios.service';
import { CommonModule } from '@angular/common';
import { TiposerviciosService } from '../../../services/planes/tiposervicios.service';
import { TecnologiasService } from '../../../services/planes/tecnologias.service';
import { TariffplanesService } from '../../../services/planes/tariffplanes.service';
import { CiudadService } from '../../../services/places/ciudad.service';
import { ProvinciasService } from '../../../services/places/provincias.service';
import { TariffPlanesVariant } from '../../../interfaces/planes/tariffplanes.interface';
import { TimeService } from '../../../services/complements/time.service';
import { Provincias } from '../../../interfaces/places/provincias.interface';
import { Ciudades } from '../../../interfaces/places/ciudad.interface';
import { CommunicationService } from '../../../services/complements/communication.service';

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
  planData: TariffPlanesVariant[] = [];
  provinciaData: Provincias[] = [];
  ciudadData: Ciudades[] = [];
  ssPlan: { servicio: string, tipoServicio: string, tecnologia: string } = { servicio: '', tipoServicio: '', tecnologia: ''  };
  horaActual: string;
  ssCity: { id_Prov: number } = { id_Prov: 0 } 

  visibleDivId: string | null = null;

  constructor(
    private serv: ServiciosService,
    private tise: TiposerviciosService,
    private tecn: TecnologiasService,
    private plan: TariffplanesService,
    private prov: ProvinciasService,
    private city: CiudadService,
    private cs_time: TimeService,
    private communicationService: CommunicationService
  ){ this.horaActual = this.cs_time.obtenerHoraActual(); }

  ngOnInit():void{
    this.Darth_Nihilus_funcion();
    this.communicationService.selectedButton$.subscribe(buttonId => {
      this.visibleDivId = buttonId;
    });
  }

  Darth_Nihilus_funcion(){
    try{
      this.fecthServiciosData(); 
      this.fecthTipoServiciosData(); 
      this.fecthTecnologiasData(); 
      this.fecthProvinciaData();
    } catch (error){
      console.log("---------------------------------------------------------------")
      console.log("header-table.compo - Darth_Nihilus_function | Error detectado: ")
      console.log(error)
      console.log("---------------------------------------------------------------")
    }
  }
  
  SIZProv(): void {
    // Verificar si se han seleccionado opciones en todos los selectores
    const servicio = (document.querySelector('select[name="PROV_V1"]') as HTMLSelectElement)?.value;
    const tipoServicio = (document.querySelector('select[name="PROV_V2"]') as HTMLSelectElement)?.value;
    const tecnologia = (document.querySelector('select[name="PROV_V3"]') as HTMLSelectElement)?.value;

    console.log(this.horaActual+" - Z Prov");
    console.log("Servicio seleccionado:", servicio);
    console.log("Tipo de Servicio seleccionado:", tipoServicio);
    console.log("Tecnología seleccionada:", tecnologia);
  
    this.ssPlan = { servicio, tipoServicio, tecnologia };
  
    // Actualizar los planes tarifarios si todos los selectores han sido seleccionados
    if (this.ssPlan .servicio && this.ssPlan .tipoServicio && this.ssPlan .tecnologia) {
      console.log(this.horaActual+"----------------")
      console.log("Todos los selectores han sido seleccionados. Actualizando los planes tarifarios...");
      this.UpTPVariant();
    }
  }

  SIZCity(): void {
    // Verificar si se han seleccionado opciones en todos los selectores
    const servicio = (document.querySelector('select[name="CITY_V1"]') as HTMLSelectElement)?.value;
    const tipoServicio = (document.querySelector('select[name="CITY_V2"]') as HTMLSelectElement)?.value;
    const tecnologia = (document.querySelector('select[name="CITY_V3"]') as HTMLSelectElement)?.value;

    console.log(this.horaActual+" - Z City");
    console.log("Servicio seleccionado:", servicio);
    console.log("Tipo de Servicio seleccionado:", tipoServicio);
    console.log("Tecnología seleccionada:", tecnologia);
    
    this.ssPlan = { servicio, tipoServicio, tecnologia };
    // Actualizar los planes tarifarios si todos los selectores han sido seleccionados
    if (this.ssPlan .servicio && this.ssPlan .tipoServicio && this.ssPlan .tecnologia) {
      console.log(this.horaActual+"----------------")
      console.log("Todos los selectores han sido seleccionados. Actualizando los planes tarifarios...");
      this.UpTPVariant();
    }
  }

  SIZSect(): void {
    // Verificar si se han seleccionado opciones en todos los selectores
    const servicio = (document.querySelector('select[name="SECT_V1"]') as HTMLSelectElement)?.value;
    const tipoServicio = (document.querySelector('select[name="SECT_V2"]') as HTMLSelectElement)?.value;
    const tecnologia = (document.querySelector('select[name="SECT_V3"]') as HTMLSelectElement)?.value;

    console.log(this.horaActual+" - Z Sect");
    console.log("Servicio seleccionado:", servicio);
    console.log("Tipo de Servicio seleccionado:", tipoServicio);
    console.log("Tecnología seleccionada:", tecnologia);
    
    this.ssPlan = { servicio, tipoServicio, tecnologia };
  
    // Actualizar los planes tarifarios si todos los selectores han sido seleccionados
    if (this.ssPlan .servicio && this.ssPlan .tipoServicio && this.ssPlan .tecnologia) {
      console.log(this.horaActual+"----------------")
      console.log("Todos los selectores han sido seleccionados. Actualizando los planes tarifarios...");
      this.UpTPVariant();
    }
  }
  
  SIZSectProv(): void {
    const id_Prov = (document.querySelector('select[name="SECT_V5"]') as HTMLSelectElement)?.value;
    // Verificar si id_Prov tiene un valor válido
    if (id_Prov !== null && id_Prov !== undefined) {
      const id_ProvNumber = parseInt(id_Prov, 10);
      // Verificar si id_ProvNumber es un número válido
      if (!isNaN(id_ProvNumber)) {
        console.log(this.horaActual + "----------------");
        console.log("Provincia seleccionada:", id_ProvNumber);
        this.ssCity = { id_Prov: id_ProvNumber };
        this.UpCiudad()
      } else {
        console.error("El valor de id_Prov no es un número válido.");
      }
    } else {
      console.error("El valor de id_Prov es nulo o indefinido.");
    }
  }
  
  UpTPVariant(): void {
    console.log(this.horaActual+"----------------")
    console.log("Actualizando los planes tarifarios...");
    const { servicio, tipoServicio, tecnologia } = this.ssPlan ;
    console.log("Servicio:", servicio);
    console.log("Tipo de Servicio:", tipoServicio);
    console.log("Tecnología:", tecnologia);
    this.fecthTariffPlanesVariantData(servicio, tipoServicio, tecnologia);
  }

  UpCiudad(): void {
    console.log(this.horaActual+"----------------")
    console.log("Actualizando las Ciudades...");
    const { id_Prov } = this.ssCity;
    console.log("Id Provincia:", id_Prov)
    this.fecthCiudadData(id_Prov);
  }

  private fecthCiudadData(id_Prov: number): void {
    console.log("CiudadData");
    this.city.getCiudadesESP(id_Prov).subscribe((response: any) => {
      console.log(response);
      if(response && response.CITIESxPROV){
        this.ciudadData = response.CITIESxPROV.map((city: any) =>{
          return{
            CIUDAD_ID: city.CIUDAD_ID,
            CIUDAD: city.CIUDAD
          };
        });
        console.log(this.ciudadData);
      }
    });
  }

  private fecthProvinciaData(): void {
    console.log("ProvinciaData");
    this.prov.getProvincias().subscribe((response: any) =>{
      console.log(response); 
      if (response && response.PROVINCIES){
        this.provinciaData = response.PROVINCIES.map((provincia: any) => {
          
          return {
            PROVINCIA_ID: provincia.PROVINCIA_ID,
            PROVINCIA: provincia.PROVINCIA
          };
        });
        console.log(this.provinciaData); 
      }
    });
  }

  private fecthTariffPlanesVariantData(servicio: string, tipoServicio: string, tecnologia: string): void {
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

  private fecthServiciosData(): void {
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