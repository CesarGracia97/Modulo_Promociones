import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Servicios } from '../../../../interfaces/planes/servicios.interface';
import { TipoServicios } from '../../../../interfaces/planes/tiposervicios.interface';
import { Tecnologias } from '../../../../interfaces/planes/tecnologias.interface';
import { Ciudades } from '../../../../interfaces/places/ciudad.interface';
import { Provincias } from '../../../../interfaces/places/provincias.interface';
import { TariffPlanesVariant } from '../../../../interfaces/planes/tariffplanes.interface';
import { CommunicationDataService } from '../../../../services/communication/communicationData.service';
import { FdCombosService } from '../../../../services/fetchData/fd-combos.service';
import { FdPlacesService } from '../../../../services/fetchData/fd-places.service';
import { Buro } from '../../../../interfaces/financial/buro.interface';
import { ModosPago } from '../../../../interfaces/financial/modos-pago.interface';
import { Sectores } from '../../../../interfaces/places/sector.interface';

@Component({
  selector: 'app-table-insert',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './table-insert.component.html',
  styleUrl: './table-insert.component.scss'
})
export class TableInsertComponent implements OnInit  {  

  _V1: string = ''; _V2: string = ''; _V3: string = ''; _V4: string = ''; _V5: string = ''; _V6: string = '';
  _V7: string = ''; _V8: string = ''; _V9: string = '';
  rows: any[] = []; //filas
  //v. Estructura de datos
  serviciosData: Servicios[] = [];
  tiposervicioData: TipoServicios[] = [];
  redData: Tecnologias[] = [];
  planData: TariffPlanesVariant[] = [];
  provinciaData: Provincias[] = [];
  ciudadData: Ciudades[] = [];
  sectoresData: Sectores[] = [];
  buroData: Buro[] = [];
  modoPagosData: ModosPago[] = [];

  dataREDT: {id: string, _V1: string, _V2: string} = {id: '', _V1: '',  _V2: ''}
  dataPLAN: {id: string, _V1: string, _V2: string, _V3: string} = {id: '', _V1: '',  _V2: '',  _V3: ''}
  
  //sub-variables inicializadores de elementos HTML

  constructor(
    private comData: CommunicationDataService,
    private fdCRequeriments: FdCombosService,
    private fdPlcRequeriments: FdPlacesService
  ){}

  ngOnInit(): void {
    this.addRow(); // Añade la primera fila automáticamente al cargar
    this.comData.dServicios$.subscribe(data => {this.serviciosData = data;});
    this.comData.dTipoServicios$.subscribe(data => {this.tiposervicioData = data;});
    this.comData.dRed$.subscribe(data => {this.redData = data;});
    this.comData.dPlan$.subscribe(data => {this.planData = data;});
    this.comData.dProvincia$.subscribe(data => {this.provinciaData = data;});
    this.comData.dCiudades$.subscribe(data => {this.ciudadData = data;});
    this.comData.dSectores$.subscribe(data => {this.sectoresData = data;})
    this.comData.dBuro$.subscribe(data => {this.buroData = data});
    this.comData.dModoPago$.subscribe(data => { this.modoPagosData = data});
  }

  addRow(): void {
    const newRow = {
      id: this.rows.length + 1,
      _V1: '',
      _V2: '',
      _V3: '',
      _V4: '',
      _V5: '',
      _V6: '',
      _V7: ''
    };
    this.rows.push(newRow); // Añade el nuevo objeto al array de filas
  }

  getDataREDT(value1: string, value2: string): void {
    try{
      this.dataREDT= {id: 'RED', _V1: value1, _V2: value2 }
      if(value1 && value2){
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
        this.fdCRequeriments.getComboPLAN(this.dataPLAN);
      }
    } catch (error) {
      console.log("Error detectado: ",error)
    }
  }

  getDataProvincias(tecnologias: string, tariffPlanesVariantID: string): void {
    try{
      if(tecnologias && tariffPlanesVariantID){
        this.fdPlcRequeriments.fetchDataProvinciasXTecnologiaXTariffplanVariant(tecnologias, parseInt(tariffPlanesVariantID))
      }
    }  catch (error) {
      console.log("Error detectado: ",error)
    }
  }

  checkSDLoading() {
    return this.serviciosData.length === 0;
  }
  
  checkTSDLoading() {
    return this.tiposervicioData.length === 0;
  }

  checkPDLoading() {
    return this.provinciaData.length === 0;
  }

  checkBDLoading(){
    return this.buroData.length === 0;
  }

  checkMPDLoading(){
    return this.modoPagosData.length === 0;
  }
}
