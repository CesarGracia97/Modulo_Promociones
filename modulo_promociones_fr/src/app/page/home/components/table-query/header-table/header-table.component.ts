import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Servicios } from '../../../../../interfaces/planes/servicios.interface';
import { TipoServicios } from '../../../../../interfaces/planes/tiposervicios.interface';
import { Tecnologias } from '../../../../../interfaces/planes/tecnologias.interface';
import { TariffPlanesVariant } from '../../../../../interfaces/planes/tariffplanes.interface';
import { Provincias } from '../../../../../interfaces/places/provincias.interface';
import { Ciudades } from '../../../../../interfaces/places/ciudad.interface';
import { TimeService } from '../../../../../services/complements/time.service';
import { CommunicationVisibleService } from '../../../../../services/communication/communicationVisible.service';
import { CommunicationDataService } from '../../../../../services/communication/communicationData.service';
import { FdCombosService } from '../../../../../services/fetchData/fd-combos.service';
import { FdPlanesService } from '../../../../../services/fetchData/fd-planes.service';
import { FdPlacesService } from '../../../../../services/fetchData/fd-places.service';

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
  tiposervicioData: TipoServicios[] = [];
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
  isLoading = true;

  constructor(    
    private cs_time: TimeService,
    private visible: CommunicationVisibleService,
    private comData: CommunicationDataService,
    private fdCRequeriments: FdCombosService,
    private fdPlnRequeriments: FdPlanesService,
    private fdPlcRequeriments: FdPlacesService
  ){ this.horaActual = this.cs_time.obtenerHoraActual(); }

  ngOnInit():void{
    this.visible.visbleItemS$.subscribe( id => {this.visibleDivId = id});
    this.comData.dServicios$.subscribe(data => {this.serviciosData = data;});
    this.comData.dTipoServicios$.subscribe(data => {this.tiposervicioData = data;});
    this.comData.dTecnologias$.subscribe(data => {this.tecnologiaData = data;});
    this.comData.dPlanes$.subscribe(data => {this.planData = data;});
    this.comData.dProvincia$.subscribe(data => {this.provinciaData = data;});
    this.comData.dCiudades$.subscribe(data => {this.ciudadData = data;});
  }

  getDataTISE(selectedValue: string): void {
    try{
      this.dataTISE= {id: 'TISE', _V1: selectedValue }
      if(selectedValue){
        console.log(this.horaActual+"----------------")
        console.log("Todos los selectores TISE han sido seleccionados. Enviando los datos...");
        this.fdCRequeriments.getComboTISE(this.dataTISE);
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
        this.fdCRequeriments.getComboRED(this.dataREDT);
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
        this.fdCRequeriments.getComboPLAN(this.dataPLAN);
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
        this.fdCRequeriments.getComboPROV(this.dataPROV);
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
        this.fdCRequeriments.getComboCITY(this.dataCITY);
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
        this.fdCRequeriments.getComboSECT(this.dataSECT);
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
    this.fdPlnRequeriments.fetchDataTariffPlanVariant(servicio, tipoServicio, tecnologia);
  }

  UpCiudad(){
    console.log(this.horaActual+"----------------")
    console.log("Actualizando las Ciudades...");
    const { id_Prov } = this.ssCity;
    console.log("Id Provincia:", id_Prov)
    this.fdPlcRequeriments.fetchDataCiudad(parseInt(id_Prov));
  }

  checkSDLoading() {
    return this.serviciosData.length === 0;
  }
  
  checkTSDLoading() {
    return this.tiposervicioData.length === 0;
  }

  checkTDLoading() {
    return this.tecnologiaData.length === 0;
  }

  checkPDLoading() {
    return this.provinciaData.length === 0;
  }
}
