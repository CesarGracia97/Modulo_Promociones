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
import { Servicios } from '../../../interfaces/planes/servicios.interface';
import { Tecnologias } from '../../../interfaces/planes/tecnologias.interface';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-header-table',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './header-table.component.html',
  styleUrl: './header-table.component.scss'
})
export class HeaderTableComponent implements OnInit{
  sTISE: string = '';
  sRED_V1: string = ''; sRED_V2: string = '';
  sPLAN_V1: string = ''; sPLAN_V2: string = ''; sPLAN_V3: string = '';
  sPROV_V1: string = ''; sPROV_V2: string = ''; sPROV_V3: string = ''; sPROV_V4: number = 0;
  sCITY_V1: string = ''; sCITY_V2: string = ''; sCITY_V3: string = ''; sCITY_V4: number = 0; sCITY_V5: number = 0;
  sSECT_V1: string = ''; sSECT_V2: string = ''; sSECT_V3: string = ''; sSECT_V4: number = 0; sSECT_V5: number = 0; sSECT_V6: number = 0;
  //v. Estructura de datos
  serviciosData: Servicios[] = [];
  tiposervicioData: TiposerviciosService[] = [];
  tecnologiaData: Tecnologias[] = [];
  planData: TariffPlanesVariant[] = [];
  provinciaData: Provincias[] = [];
  ciudadData: Ciudades[] = [];
  //v. inicializadores de elementos HTML
  dataTISE: {id: string, _V1: string} = {id: '', _V1: ''}
  dataREDT: {id: string, _V1: string, _V2: string} = {id: '', _V1: '',  _V2: ''}
  dataPLAN: {id: string, _V1: string, _V2: string, _V3: string} = {id: '', _V1: '',  _V2: '',  _V3: ''}
  dataPROV: {id: string, _V1: string, _V2: string, _V3: string, _V4: string} = {id: '', _V1: '',  _V2: '',  _V3: '',  _V4: ''}
  dataCITY: {id: string, _V1: string, _V2: string, _V3: string, _V4: string, _V5: string} = {id: '', _V1: '',  _V2: '',  _V3: '',  _V4: '',  _V5: ''}
  dataSECT: {id: string, _V1: string, _V2: string, _V3: string, _V4: string, _V5: string, _V6: string} = {id: '', _V1: '',  _V2: '',  _V3: '',  _V4: '',  _V5: '',  _V6: ''}
    //sub-variables inicializadores de elementos HTML
    ssPlan: { servicio: string, tipoServicio: string, tecnologia: string } = { servicio: '', tipoServicio: '', tecnologia: ''  };
    ssCity: { id_Prov: number } = { id_Prov: 0 } 
  //v. complemento y soporte
  horaActual: string;
  visibleDivId: string | null = null;
  diccionario: any = {};

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

  getDataTISE(selectedValue: string): void {
    console.log(this.horaActual+"\n Datos seleccionados - Enviar");
    this.dataTISE= {id: 'TISE', _V1: selectedValue }
    this.communicationService.sendDataHeaderTable(this.dataTISE);
    if(selectedValue){
        console.log(this.horaActual+"----------------")
        console.log("Todos los selectores TISE han sido seleccionados. Enviando los datos...");
        this.communicationService.sendDataHeaderTable(this.dataTISE);
    }
  }

  getDataREDT(value1: string, value2: string): void {
    console.log(this.horaActual+"\n Datos seleccionados - Enviar");
    this.dataREDT= {id: 'RED', _V1: value1, _V2: value2 }
    if(value1 && value2){
        console.log(this.horaActual+"----------------");
        console.log("Todos los selectores RED han sido seleccionados. Enviando los datos...");
        console.log(this.dataREDT)
        this.communicationService.sendDataHeaderTable(this.dataREDT);
    }
}

  getDataPLAN(){
    const id = "PLAN";
    const _V1 = (document.querySelector('select[name="PLAN_V1"]') as HTMLSelectElement)?.value;
    const _V2 = (document.querySelector('select[name="PLAN_V2"]') as HTMLSelectElement)?.value;
    const _V3 = (document.querySelector('select[name="PLAN_V3"]') as HTMLSelectElement)?.value;
    console.log(this.horaActual+"\n Datos seleccionados - Enviar");
    this.dataPLAN= {id ,_V1, _V2, _V3 }
    if(this.dataPLAN ._V1 && this.dataPLAN ._V2 && this.dataPLAN ._V3){
      console.log(this.horaActual+"----------------");
      console.log("Todos los selectores PLAN han sido seleccionados. Enviando los datos...");
      this.communicationService.sendDataHeaderTable(this.dataPLAN);
    }
  }

  getDataPROV(){
    const id = "PROV";
    const _V1 = (document.querySelector('select[name="PROV_V1"]') as HTMLSelectElement)?.value;
    const _V2 = (document.querySelector('select[name="PROV_V2"]') as HTMLSelectElement)?.value;
    const _V3 = (document.querySelector('select[name="PROV_V3"]') as HTMLSelectElement)?.value;
    const _V4 = (document.querySelector('select[name="PROV_V4"]') as HTMLSelectElement)?.value;
    console.log(this.horaActual+"\n Datos seleccionados - Enviar");
    this.dataPROV= {id ,_V1, _V2, _V3, _V4}
    if(this.dataPROV._V1 && this.dataPROV ._V2 && this.dataPROV ._V3 && this.dataPROV ._V4){
      console.log(this.horaActual+"----------------");
      console.log("Todos los selectores PROV han sido seleccionados. Enviando los datos...");
      this.communicationService.sendDataHeaderTable(this.dataPROV);
    }
  }

  getDataCITY(){
    const id = "CITY";
    const _V1 = (document.querySelector('select[name="CITY_V1"]') as HTMLSelectElement)?.value;
    const _V2 = (document.querySelector('select[name="CITY_V2"]') as HTMLSelectElement)?.value;
    const _V3 = (document.querySelector('select[name="CITY_V3"]') as HTMLSelectElement)?.value;
    const _V4 = (document.querySelector('select[name="CITY_V4"]') as HTMLSelectElement)?.value;
    const _V5 = (document.querySelector('select[name="CITY_V5"]') as HTMLSelectElement)?.value;
    console.log(this.horaActual+"\n Datos seleccionados - Enviar");
    this.dataCITY= {id ,_V1, _V2, _V3, _V4, _V5}
    if(this.dataCITY._V1 && this.dataCITY ._V2 && this.dataCITY ._V3 && this.dataCITY ._V4 && this.dataCITY ._V5){
      console.log(this.horaActual+"----------------");
      console.log("Todos los selectores CITY han sido seleccionados. Enviando los datos...");
      this.communicationService.sendDataHeaderTable(this.dataCITY);
    }
  }

  getDataSECT(){
    const id = "SECT";
    const _V1 = (document.querySelector('select[name="SECT_V1"]') as HTMLSelectElement)?.value;
    const _V2 = (document.querySelector('select[name="SECT_V2"]') as HTMLSelectElement)?.value;
    const _V3 = (document.querySelector('select[name="SECT_V3"]') as HTMLSelectElement)?.value;
    const _V4 = (document.querySelector('select[name="SECT_V4"]') as HTMLSelectElement)?.value;
    const _V5 = (document.querySelector('select[name="SECT_V5"]') as HTMLSelectElement)?.value;
    const _V6 = (document.querySelector('select[name="SECT_V6"]') as HTMLSelectElement)?.value;
    console.log(this.horaActual+"\n Datos seleccionados - Enviar");
    this.dataSECT= {id ,_V1, _V2, _V3, _V4, _V5, _V6}
    if(this.dataSECT._V1 && this.dataSECT ._V2 && this.dataSECT ._V3 && this.dataSECT ._V4 && this.dataSECT ._V5 && this.dataSECT ._V6){
      console.log(this.horaActual+"----------------");
      console.log("Todos los selectores SECT han sido seleccionados. Enviando los datos...");
      this.communicationService.sendDataHeaderTable(this.dataSECT);
    }
  }
  
  SIZProv(){
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