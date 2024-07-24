import { CommonModule } from '@angular/common';
import { Component, Input, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Servicios } from '../../../../interfaces/planes/servicios.interface';
import { DataPromocionInformationService } from '../../../../services/subscribeData/data-promocion-information.service';
import { FdModospagosService } from '../../../../services/fetchData/FinancialInfo/fd-modospagos.service';
import { FdBuroService } from '../../../../services/fetchData/FinancialInfo/fd-buro.service';
import { FdDiasGozadosService } from '../../../../services/fetchData/DataPromocional/fd-dias_gozados.service';
import { DataViewService } from '../../../../services/subscribeData/data-view.service';
import { ModalDataPromocionalComponent } from './modal-data-promocional/modal-data-promocional.component';
import { ModalInformacionComponent } from './modal-informacion/modal-informacion.component';


@Component({
  selector: 'app-table-insert',
  standalone: true,
  imports: [CommonModule, FormsModule, ModalDataPromocionalComponent, ModalInformacionComponent],
  templateUrl: './table-insert.component.html',
  styleUrl: './table-insert.component.scss'
})
export class TableInsertComponent implements OnInit {
  @Input() rows: any[] = [];

  //Variables de Datos
  serviciosData: Servicios[] = [];

  //Variables de vista 
  _inp1: boolean[] = []; _inp2: boolean[] = []; valideBtn: boolean = false; cont: number[] = [];
  minDate_V2: string = ''; minDate_V3: string [] = [];

  //Diccionario de Datos
  private diccionario: { [key: string]: any }[] = [];

  constructor(
    private data_information: DataPromocionInformationService,
    private fdmp: FdModospagosService,
    private fdb: FdBuroService,
    private fddg: FdDiasGozadosService,
    private data_views: DataViewService

  ){}

  ngOnInit(): void {
    this.addRow(); // Añade la primera fila automáticamente al cargar
    this.data_information.dServicios$.subscribe(data => {this.serviciosData = data;});
    this.data_information.dDiccionario$.subscribe(data => {this.diccionario = data;});
    this.data_views.dModalViewDP$.subscribe( data => {this.valideBtn = data;})
    this.minDate_V2 = this.formatDate(new Date());
  }

  addRow(): void {
    const newRow = {
      id: this.rows.length,
      _V1: '', _V2: '', _V3: '', _V4: '', _V5: '', _V6: '',  _V7: '', _V8: '', _V11:'', _V15:'', _V16: '', _V17: '',
      _V18: '', _V19: '',
      serviciosData: [], planData: [], planVData: [], productosData: [], ciudadData: [], sectoresData: [], upgradeData: [],
      selectedTable: 0, // Cambiado de array a un solo número
      tablas: [
        {
          id: 0,
          PRAD_V1: '', PRAD_ST_V2: '', PRAD_ST_V3: '', PRAD_ST_V4: ''
        }
      ],
      planesTelevisivos: [], planesTelefonicos: [], modelosRouter: [],
      PRAD_TF_V1: '', PRAD_TF_V2: '', PRAD_TF_V3: '', PRAD_TF_V4: '', PRAD_TF_V5: '',
      PRAD_TV_V1: '', PRAD_TV_V2: '', PRAD_TV_V3: '', PRAD_TV_V4: '', PRAD_TV_V5: '',
      PRAD_RT_V1: '', PRAD_RT_V2: '', PRAD_RT_V3: '', PRAD_RT_V4: '', PRAD_RT_V5: '', // Cambiado de array a un solo número
    };
    this.rows.push(newRow); // Añade el nuevo objeto al array de filas
    this.data_information.sendDataNewDiccionario(this.rows.length - 1); // Manda a generar un nuevo diccionario
    this.diccionario[this.rows.length - 1] = {};
  }

  getNombrePromocion(NombrePromocion: string, index: number): void {
    if(NombrePromocion){
      this.diccionario[index]['Id Registro'] = index
      this.diccionario[index]['Nombre Promocion'] = NombrePromocion;
      this.data_information.sendDataUptadeDiccionario(this.diccionario[index], index);
      this._inp1[index] = true;
    } else  {
      this._inp2[index] = false;
    }
  }

  getFechasInicioFin(Fecha_Inicio: Date, Fecha_Finalizacion: Date, index: number): void{
    let newDate = new Date(Fecha_Inicio);
    newDate.setDate(newDate.getDate() + 2);
    this.minDate_V3[index] = this.formatDate(newDate);
    if(Fecha_Inicio && Fecha_Finalizacion){
      const today = new Date();
      today.setHours(0, 0, 0, 0); // Ignorar la parte de horas
      if (Fecha_Inicio < today) {
        console.error('La fecha de inicio no puede ser menor a la fecha actual.');
        this._inp2[index] = false;
        return;
      }
      if (Fecha_Inicio >= Fecha_Finalizacion) {
        console.error('La fecha de inicio debe ser menor a la fecha de finalización.');
        this._inp2[index] = false;
        return;
      }
      if (this.isWeekend(Fecha_Inicio.toString()) || this.isWeekend(Fecha_Finalizacion.toString())) {
        console.error('Las fechas de inicio y finalización no pueden ser en fines de semana.');
        this._inp2[index] = false;
        return;
      }
      this.diccionario[index]['Fecha Inicio Promocion'] = Fecha_Inicio.toString();
      this.diccionario[index]['Fecha Finalizacion Promocion'] = Fecha_Finalizacion.toString();
      this.data_information.sendDataUptadeDiccionario(this.diccionario[index], index);
      this._inp2[index] = true;
    }
  }

  openModalDatosPromocionales(index: number): void {
    const rowData = this.rows[index];
    this.data_views.indexMoment(index);
    this.data_views.rowMoment(rowData);
    this.data_views.stateModalDP(true);
    this.data_information.sendDataCanal(index);
    this.fdmp.fetchDataModosPago(index);
    this.fdb.fetchDataBuro(index);
    this.fddg.fetchDiasGozados(index);
  }

  checkSDLoading() {
    return this.serviciosData.length === 0;
  }

  sendDiccionario(index: number): void {
    this.data_views.indexMoment(index);
    this.data_information.sendDiccionario();
  }
  
  formatDate(date: Date): string {
    const day = date.getDate().toString().padStart(2, '0');
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const year = date.getFullYear();
    return `${year}-${month}-${day}`;
  }


  isWeekend(date: string): boolean {
    const day = new Date(date).getDay();
    return day === 5 || day === 6; // Domingo = 6, Sábado = 5
  }

  validateV2(row: any): string | null {
    if (this.isWeekend(row._V2)) {
      return 'Las fechas de fin de semana no son permitidas.';
    }
    return null;
  }

  validateV3(row: any): string | null {
    if (!row._V2) {
      return 'Debe seleccionar una fecha de inicio primero.';
    }
    const dateV2 = new Date(row._V2);
    const dateV3 = new Date(row._V3);
    if (dateV3 <= dateV2) {
      return 'La fecha de fin debe ser mayor a la fecha de inicio.';
    }
    if (this.isWeekend(row._V3)) {
      return 'Las fechas de fin de semana no son permitidas.';
    }
    return null;
  }

  disableDatosPromocionales(index: number): boolean{
    return this._inp1[index] && this._inp2[index];
  }
}