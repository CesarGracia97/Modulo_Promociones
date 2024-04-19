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
import { FdPlanesService } from '../../../../services/fetchData/fd-planes.service';

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

  dataREDT: {id: string, _V1: string, _V2: string} = {id: '', _V1: '',  _V2: ''}
  dataPLAN: {id: string, _V1: string, _V2: string, _V3: string} = {id: '', _V1: '',  _V2: '',  _V3: ''}
  dataPROV: {id: string, _V1: string, _V2: string, _V3: string, _V4: string} = {id: '', _V1: '',  _V2: '',  _V3: '',  _V4: ''}
  dataCITY: {id: string, _V1: string, _V2: string, _V3: string, _V4: string, _V5: string} = {id: '', _V1: '',  _V2: '',  _V3: '',  _V4: '',  _V5: ''}
  dataSECT: {id: string, _V1: string, _V2: string, _V3: string, _V4: string, _V5: string, _V6: string} = {id: '', _V1: '',  _V2: '',  _V3: '',  _V4: '',  _V5: '',  _V6: ''}
  //sub-variables inicializadores de elementos HTML
  ssPlan: { servicio: string, tipoServicio: string, tecnologia: string } = { servicio: '', tipoServicio: '', tecnologia: ''  };
  ssCity: { id_Prov: string } = { id_Prov: '' } 

  constructor(
    private comData: CommunicationDataService,
    private fdCRequeriments: FdCombosService,
    private fdPlnRequeriments: FdPlanesService,
    private fdPlcRequeriments: FdPlacesService
  ){}

  ngOnInit(): void {
    this.addRow(); // Añade la primera fila automáticamente al cargar
    this.comData.dServicios$.subscribe(data => {this.serviciosData = data;});
    this.comData.dTipoServicios$.subscribe(data => {this.tiposervicioData = data;});
    this.comData.dRed$.subscribe(data => {this.redData = data;});
    this.comData.dPlanes$.subscribe(data => {this.planData = data;});
    this.comData.dProvincia$.subscribe(data => {this.provinciaData = data;});
    this.comData.dCiudades$.subscribe(data => {this.ciudadData = data;});
  }

  addRow(): void {
    const newRow = {
      id: this.rows.length + 1
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

  checkSDLoading() {
    return this.serviciosData.length === 0;
  }
  
  checkTSDLoading() {
    return this.tiposervicioData.length === 0;
  }

  checkPDLoading() {
    return this.provinciaData.length === 0;
  }
}
