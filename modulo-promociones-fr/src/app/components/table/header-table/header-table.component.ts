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
  _V1: string = ''; _V2: string = ''; _V3: string = ''; _V4: string = ''; _V5: string = ''; _V6: string = '';
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
    ssCity: { id_Prov: string } = { id_Prov: '' } 
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
    this.communicationService.visbleItemS$.subscribe(buttonId => {
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
    try{
      this.dataTISE= {id: 'TISE', _V1: selectedValue }
      this.communicationService.sendDataHeaderTable(this.dataTISE);
      if(selectedValue){
        console.log(this.horaActual+"----------------")
        console.log("Todos los selectores TISE han sido seleccionados. Enviando los datos...");
        this.communicationService.sendDataHeaderTable(this.dataTISE);
      }
    }
    catch(error){
      console.log("Error detectado: ",error)
    }
  } 

  getDataREDT(value1: string, value2: string): void {
    try{
      this.dataREDT= {id: 'RED', _V1: value1, _V2: value2 }
      if(value1 && value2){
        console.log(this.horaActual+"----------------");
        console.log("Todos los selectores RED han sido seleccionados. Enviando los datos...");
        console.log(this.dataREDT)
        this.communicationService.sendDataHeaderTable(this.dataREDT);
      }
    } catch(error){
      console.log("Error Detectado: ",error)
    }
  }

  getDataPLAN(value1: string, value2:string, value3: string): void {
    try{
      this.dataPLAN = {id:'PLAN', _V1: value1, _V2: value2, _V3: value3}
      if(value1 && value2 && value3){
        console.log(this.horaActual+"----------------");
        console.log("Todos los selectores PLAN han sido seleccionados. Enviando los datos...");
        console.log(this.dataPLAN);
        this.communicationService.sendDataHeaderTable(this.dataPLAN);
      }
    } catch (error){
      console.log("Error detectado: ",error)
    }
  }

  getDataPROV(value1: string, value2:string, value3: string, value4: string): void {
    try{
      this.dataPROV = {id: 'PROV', _V1: value1, _V2: value2, _V3: value3, _V4: value4}
      if(value1 && value2 && value3 && value4){
        console.log(this.horaActual+"----------------");
        console.log("Todos los selectores PROV han sido seleccionados. Enviando los datos...");
        console.log(this.dataPROV);
        this.communicationService.sendDataHeaderTable(this.dataPROV);
      }
    } catch (error) {
      console.log("Error detectado: ",error)
    }
  }

  getDataCITY(value1: string, value2:string, value3: string, value4: string, value5: string): void{
    try{
      this.dataCITY = {id: 'CITY', _V1: value1, _V2: value2, _V3: value3, _V4: value4, _V5: value5}
      if(value1 && value2 && value3 && value4 && value5){
        console.log(this.horaActual+"----------------");
        console.log("Todos los selectores CITY han sido seleccionados. Enviando los datos...");
        console.log(this.dataCITY);
        this.communicationService.sendDataHeaderTable(this.dataCITY);
      }
    } catch (error) {
      console.log("Error Detectado: ", error)
    }
  }

  getDataSECT(value1: string, value2:string, value3: string, value4: string, value5: string, value6: string): void{
    try{
      this.dataSECT = {id: 'SECT', _V1: value1, _V2: value2, _V3: value3, _V4: value4, _V5: value5, _V6: value6}
      if(value1 && value2 && value3 && value4 && value5 && value6){
        console.log(this.horaActual+"----------------");
        console.log("Todos los selectores SECT han sido seleccionados. Enviando los datos...");
        console.log(this.dataSECT);
        this.communicationService.sendDataHeaderTable(this.dataSECT);
      }
    } catch (error) {
      console.log("Error Detectado: ", error)
    }
  }
  
  SITPVariant(value1: string, value2: string, value3: string): void {
    try{
    // Verificar si se han seleccionado opciones en todos los selectores
    console.log(this.horaActual+" - SITPVariant");
    console.log("Servicio seleccionado:", value1);
    console.log("Tipo de Servicio seleccionado:", value2);
    console.log("Tecnología seleccionada:", value3);
    this.ssPlan = { servicio: value1, tipoServicio: value2, tecnologia: value3 };
    // Actualizar los planes tarifarios si todos los selectores han sido seleccionados
    if (value1 && value2 && value3) {
      console.log(this.horaActual+"----------------")
      console.log("Todos los selectores han sido seleccionados. Actualizando los planes tarifarios...");
      this.UpTPVariant();
    }
    } catch (error) {
      console.log("Error Detectado: ", error)
    }
  }
  
  SIProv(value: string): void {
    try{
      console.log(this.horaActual+" - SIProv");
      console.log("Id Provincia Seleccionado:",value)
      this.ssCity = {id_Prov: value}
      if (value) {
        this.UpCiudad();
      }
    } catch (error) {
      console.log("Error detectado: ",error)
    }
  }
  
  UpTPVariant(){
    console.log(this.horaActual+"----------------")
    console.log("Actualizando los planes tarifarios...");
    const { servicio, tipoServicio, tecnologia } = this.ssPlan ;
    console.log("Servicio:", servicio);
    console.log("Tipo de Servicio:", tipoServicio);
    console.log("Tecnología:", tecnologia);
    this.fecthTariffPlanesVariantData(servicio, tipoServicio, tecnologia);
  }

  UpCiudad(){
    console.log(this.horaActual+"----------------")
    console.log("Actualizando las Ciudades...");
    const { id_Prov } = this.ssCity;
    console.log("Id Provincia:", id_Prov)
    this.fecthCiudadData(parseInt(id_Prov));
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