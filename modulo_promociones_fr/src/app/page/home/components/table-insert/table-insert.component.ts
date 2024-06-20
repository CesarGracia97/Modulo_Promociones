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


@Component({
  selector: 'app-table-insert',
  standalone: true,
  imports: [CommonModule, FormsModule, ModalDataPromocionalComponent],
  templateUrl: './table-insert.component.html',
  styleUrl: './table-insert.component.scss'
})
export class TableInsertComponent implements OnInit {
  @Input() rows: any[] = [];

  //v. Estructura de datos
  serviciosData: Servicios[] = [];

  constructor(
    private comData: DataPromocionInformationService,
    private fdmp: FdModospagosService,
    private fdb: FdBuroService,
    private fddg: FdDiasGozadosService,
    private data_views: DataViewService, private data_information: DataPromocionInformationService
  ){}

  ngOnInit(): void {
    this.addRow(); // Añade la primera fila automáticamente al cargar
    this.comData.dServicios$.subscribe(data => {this.serviciosData = data;});
  }

  addRow(): void {
    const newRow = {
      id: this.rows.length,
      _V1: '', _V2: '', _V3: '', _V4: '', _V5: '', _V6: '',  _V7: '', _V8: ''
    };
    this.rows.push(newRow); // Añade el nuevo objeto al array de filas
  }

  openModalDatosPromocionales(index: number){
    const rowData = this.rows[index];
    this.data_views.indexMoment(index);
    this.data_views.rowMoment(index, rowData);
    this.data_views.stateModalDP(true);
    this.data_information.sendDataCanal(index);
    this.fdmp.fetchDataModosPago(index);
    this.fdb.fetchDataBuro(index);
    this.fddg.fetchDiasGozados(index);
  }

  checkSDLoading() {
    return this.serviciosData.length === 0;
  }

  isWeekend(date: string): boolean {
    const day = new Date(date).getDay();
    return day === 0 || day === 6; // Domingo = 0, Sábado = 6
  }

  validateV2(row: any): string | null {
    const today = new Date();
    today.setHours(0, 0, 0, 0); // Ignorar la parte de horas
    const dateV2 = new Date(row._V2);

    if (dateV2 < today) {
      return 'La fecha no puede ser menor a la fecha actual.';
    }
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
}