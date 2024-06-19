import { CommonModule } from '@angular/common';
import { Component, Input, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Servicios } from '../../../../interfaces/planes/servicios.interface';
import { Ciudades } from '../../../../interfaces/places/ciudad.interface';
import { TariffPlanes, TariffPlanesVariant } from '../../../../interfaces/planes/tariffplanes.interface';
import { DataPromocionInformationService } from '../../../../services/subscribeData/data-promocion-information.service';
import { Buro } from '../../../../interfaces/financial/buro.interface';
import { ModosPago } from '../../../../interfaces/financial/modos-pago.interface';
import { Sectores } from '../../../../interfaces/places/sector.interface';
import { FdCombosService } from '../../../../services/fetchData/fd-combos.service';
import { FdPlacesService } from '../../../../services/fetchData/fd-places.service';
import { FdModospagosService } from '../../../../services/fetchData/FinancialInfo/fd-modospagos.service';
import { FdBuroService } from '../../../../services/fetchData/FinancialInfo/fd-buro.service';
import { Productos } from '../../../../interfaces/planes/productos.interface';
import { DiasGozados } from '../../../../interfaces/DataPromocional/dias-gozados.interface';
import { FdDiasGozadosService } from '../../../../services/fetchData/DataPromocional/fd-dias_gozados.service';
import { FdPrecioRegularService } from '../../../../services/fetchData/DataPromocional/fd-precio_regular.service';
import { PrecioRegular } from '../../../../interfaces/DataPromocional/precio-regular.interface';
import { FdUpgradeService } from '../../../../services/fetchData/DataPromocional/fd-upgrade.service';
import { Upgrade } from '../../../../interfaces/DataPromocional/upgrade.interface';
import { Options_PA } from '../../../../interfaces/Interfaces-View/Options_PA.interface';
import { FdPlanesService } from '../../../../services/fetchData/fd-planes.service';
import { InjectionDataService } from '../../../../services/injection/injection-data.service';
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
  @Input() rows: any[] = []; rowId: number = 0;

  tablesRow: any[][] = [];
  PRAD_ST_V1: string =''; PRAD_ST_V2: string ='';  PRAD_ST_V3: string ='';
  selectedTable: number[] = []; tableId = 0;

  //v. Estructura de datos
  serviciosData: Servicios[] = [];
  productosData: Productos[][] = [];
  planData: TariffPlanes[][] = []; planVData: TariffPlanesVariant[][] = [];
  ciudadData: Ciudades[][] = []; sectoresData: Sectores[][] = [];
  buroData: Buro[][] = []; modoPagosData: ModosPago[][] = []; diasGozadosData: DiasGozados[][] = [];
  precioRegularData: PrecioRegular[][] = [];
  upgradeData: Upgrade [][] = [];
  optionsData: Options_PA[][] = [];
  paquetesStreaming: TariffPlanesVariant[][] = []; planesTelevisivos: TariffPlanesVariant[][] = []; 
  planesTelefonicos: TariffPlanesVariant[][] = [];   modelosRouter: Productos[][]= [];
  precioRegularStreamingData: PrecioRegular[][][] = []; precioRegularTelefoniaData: PrecioRegular[][] = [];
  precioRegularTelevisioData: PrecioRegular[][] = []; precioRegularRouter: PrecioRegular[][] = [];

  showMDPDD: boolean[] = []; showBDD: boolean[] = []; showPROAD: boolean[] = [];
  visibleUpgrade: boolean[] = []; visibleBtnPromocionAdicional: boolean[] = [];permitido: boolean[] = []; 
  vPA: { [index: number]: { [type: string]: boolean } } = [];
  vPR: { [index: number]: { [type: string]: boolean } } = [];

  closing: boolean = false; modal_cs: boolean = false; modal_dp: boolean = false;

  constructor(
    private comData: DataPromocionInformationService,
    private fdpl: FdPlacesService,
    private fdpln: FdPlanesService,
    private fdcb: FdCombosService,
    private fdmp: FdModospagosService,
    private fdb: FdBuroService,
    private fddg: FdDiasGozadosService,
    private fdpr: FdPrecioRegularService,
    private fdup: FdUpgradeService,
    private send: InjectionDataService,
    private data_views: DataViewService, private data_information: DataPromocionInformationService
  ){}

  ngOnInit(): void {
    this.addRow(); // Añade la primera fila automáticamente al cargar
    this.comData.dServicios$.subscribe(data => {this.serviciosData = data;});
  }

  addRow(): void {
    const newRow = {
      id: this.rows.length,
      _V1: '', _V2: '', _V3: '', _V4: '', _V9: '', _V11: '', 
      planData: [], planVData: [], productosData: [], ciudadData: [], sectoresData: [],
      diasGozadosData: [], upgradeData: [], selectedTable: [], // Cambiado de array a un solo número
      tablesRow: [{
        id: 0, paquetesStreaming: [], PRAD_ST_V1: '', PRAD_ST_V2: '', PRAD_ST_V3: ''
      }], planesTelevisivos: [], planesTelefonicos: [], modelosRouter: [],
      PRAD_TF_V1: '', PRAD_TF_V2: '', PRAD_TF_V3: '', PRAD_TF_V4: '',
      PRAD_TV_V1: '', PRAD_TV_V2: '', PRAD_TV_V3: '', PRAD_TV_V4: '',
      PRAD_RT_V1: '', PRAD_RT_V2: '', PRAD_RT_V3: '', PRAD_RT_V4: ''
    };
    this.rows.push(newRow); // Añade el nuevo objeto al array de filas
    this.planData.push([]);
    this.planVData.push([]);
    this.productosData.push([]); 
    this.upgradeData.push([]);
    this.ciudadData.push([]);
    this.sectoresData.push([]);
    this.upgradeData.push([]);
    this.showMDPDD.push(false);
    this.showBDD.push(false);
    this.showPROAD.push(false);
    this.optionsData.push([
      {name: 'NO APLICAR', selected: false},
      {name: 'STREAMING', selected: false},
      {name: 'TELEFONIA', selected: false},
      {name: 'TELEVISION', selected: false}
    ]);
    this.tablesRow.push([{id: 0, paquetesStreaming: [], PRAD_ST_V1: '', PRAD_ST_V2: '',  PRAD_ST_V3: ''}]);
    this.paquetesStreaming.push([]);
    this.planesTelefonicos.push([]);
    this.planesTelevisivos.push([]);
    this.modelosRouter.push([])
    this.selectedTable.push(0); 
    this.precioRegularStreamingData.push([[]]);
    this.precioRegularTelefoniaData.push([]);
    this.precioRegularTelevisioData.push([]);
    this.precioRegularRouter.push([]);
    this.permitido[this.rows.length - 1] = false;
    this.vPA[this.rows.length - 1] = { 'STREAMING': false, 'TELEFONIA': false, 'TELEVISION': false, 'ROUTER': false };
    this.vPR[this.rows.length - 1] = { 'NORMAL': false, 'TELEFONIA': false, 'TELEVISION': false, 'ROUTER': false };

  }

  openModalDatosPromocionales(index: number, row: any){
    this.data_views.indexMoment(index);
    this.data_views.stateModalDP(true);
    this.data_information.sendDataCanal(index);
    this.fdmp.fetchDataModosPago(index);
    this.fdb.fetchDataBuro(index);
    this.fddg.fetchDiasGozados(index);
  }

  darIdProducto(index: number): number {
    const idsEspeciales = [95999, 96010, 96007];
    const ciudadesSeleccionadas = this.ciudadData[index].filter(ciudad => ciudad.selected);
    const idsSeleccionados = ciudadesSeleccionadas.map(ciudad => ciudad.CIUDAD_ID);
    const todosIdsEspecialesSeleccionados = idsEspeciales.every(id => idsSeleccionados.includes(id));
    if (todosIdsEspecialesSeleccionados) {
        return 170;
    } else {
        return 5;
    }
  }

  buscarSectores() {
    const index = this.rowId; 
    const indexRow = this.rows[index]; 
    const _V3 = indexRow._V3; const _V4 = indexRow._V4;
    const ciudades = this.ciudadData[index].filter(city => city.selected).map(city => city.CIUDAD_ID);
    this.fdpl.fetchDataSectoresMasivosXTariffplanVariantXProducto_RETURN(ciudades, _V3, _V4)
    .subscribe((sectores) => { this.sectoresData[index] = sectores; });
  }

  button_V1_V6(row: any, index: number): boolean {
    const trueSelect = row._V1 && row._V2 && row._V3 && row._V4;
    const trueMP = this.modoPagosData[index] && this.modoPagosData[index].some(mdpg => mdpg.selected);
    const trueB = this.buroData[index] && this.buroData[index].some(buro => buro.selected);
    return trueSelect && trueMP && trueB;
  }

  button_search_sect(index: number): boolean {
    return this.ciudadData[index].some(ciudad => ciudad.selected);
  }

  button_V1_V8(row: any, index: number): boolean {
    const trueC = this.ciudadData[index] && this.ciudadData[index].some(ciudad => ciudad.selected);
    const trueS = this.sectoresData[index] && this.sectoresData[index].some(sectores => sectores.selected);
    return this.button_V1_V6(row, index) && trueC && trueS;
  }

  updateSelection(rowId: number, index: number): void {
    const options = this.optionsData[rowId];
    if (index === 0 && options[0].selected) { // "NO APLICAR" ha sido seleccionado
      options.forEach((option, idx) => {
        if (idx !== 0) option.selected = false;
      });
    } else if (index !== 0 && options[index].selected) { // Otra opción que no es "NO APLICAR" ha sido seleccionada
      options[0].selected = false;
    }
    if (index === 1 && options[1].selected){
      this.fdpln.fetchDataTariffPlanVariantXProductoAdicional_RETURN('STREAMING')
      .subscribe((PROAD: TariffPlanesVariant[]) => { this.paquetesStreaming[rowId] = PROAD; });
    } else if (index === 2 && options[2].selected) {
      this.fdpln.fetchDataTariffPlanVariantXProductoAdicional_RETURN('TELEFONIA')
      .subscribe((PROAD: TariffPlanesVariant[]) => { this.planesTelefonicos[rowId] = PROAD; });
    } else if (index == 3 && options[3].selected) {
      this.fdpln.fetchDataTariffPlanVariantXProductoAdicional_RETURN('TELEVISION')
      .subscribe((PROAD: TariffPlanesVariant[]) => { this.planesTelevisivos[rowId] = PROAD; });
    } else if (index == 4 && options[4].selected){
      this.fdcb.fetchDataComboPROD_ROUTER_RETURN()
      .subscribe((modelos: Productos[]) => { this.modelosRouter[rowId] = modelos; });
    }
  }

  button_sendInformation(index: number, posicion: number){
    const row = this.rows[index]; 
    let true1: boolean;
    if(this.upgradeData[index].length > 0){
      true1 = !!row._V9 && !!row._V11;
    } else {
      true1 = !!row._V9;
    }
    const true2 = this.diasGozadosData[index] && this.diasGozadosData[index].some(dias => dias.selected);
    const options = this.optionsData[index];
    let isValid = true;
    if(options[posicion].selected){
      if (posicion == 0 && options[0].selected){
        this.permitido[index] = this.button_V1_V8(row, index) && true1 && true2 && isValid;
      } else if (posicion != 0 && options[posicion].selected){
        switch(posicion){
          case 1: // STREAMING
            //isValid = isValid && this.validateStreamingData(row, index);
          break;
          case 2: // TELEFONIA
            isValid = isValid && this.vPA[index]['TELEFONIA'];
          break;
          case 3: // TELEVISION
            isValid = isValid && this.vPA[index]['TELEVISION'];
          break;
          case 4: // ROUTER
            isValid = isValid && this.vPA[index]['ROUTER'];
          break;
        }
      }
    } else {
      isValid = false;
    }
    this.permitido[index] = this.button_V1_V8(row, index) && true1 && true2 && isValid;
  }

  toggDD(index: number, type: string) {
    switch(type){
      case 'MP':
        if (this.showMDPDD) {
          this.closing = true;// Si está abierto y se va a cerrar, activa la transición rápida
          setTimeout(() => {
            this.showMDPDD[index] = !this.showMDPDD[index];
            this.closing = false;
          }, 30); // Espera el tiempo de la transición de cierre
        }
      break;
      case 'B':
        if (this.showBDD) {
          this.closing = true;// Si está abierto y se va a cerrar, activa la transición rápida
          setTimeout(() => {
            this.showBDD[index] = !this.showBDD[index];
            this.closing = false;
          }, 30); // Espera el tiempo de la transición de cierre
        }
      break;
      case 'PA':
        if (this.showPROAD) {
          this.closing = true;
          setTimeout(() => {
            this.showPROAD[index] = !this.showPROAD[index];
            this.closing = false;
          }, 30); // Espera el tiempo de la transición de cierre
        }
      break;
    }
  }

  checkSDLoading() {
    return this.serviciosData.length === 0;
  }

  openModal(row: number, type: string): void {
    this.rowId = row;
    switch(type){
      case 'CS':
        this.modal_cs = true;
      break;
      case 'DP':
        this.modal_dp = true;
      break;
    }
  }

  closeModal(type: string): void {
    switch(type){
      case 'CS':
        this.modal_cs = false;
      break;
      case 'DP':
        this.modal_dp = false;
      break;
    }
  }

  addNewTable(rowId: number): void {
    const newTable = {
        id: this.tablesRow[rowId].length,
        paquetesStreaming: [], PRAD_ST_V1: '', PRAD_ST_V2: '', PRAD_ST_V3: ''
    };
    this.tablesRow[rowId].push(newTable);
    if (!this.selectedTable[rowId])
      this.selectedTable[rowId] = 0;
    this.selectedTable[rowId] = this.tablesRow[rowId].length - 1;
    if (!this.precioRegularStreamingData[rowId])
      this.precioRegularStreamingData[rowId] = [];
    this.precioRegularStreamingData[rowId].push([]);
  }

  changeTable(event: Event, rowId: number): void {
    const target = event.target as HTMLSelectElement;
    const index = parseInt(target.value, 10);
    if (!isNaN(index)) this.selectedTable[rowId] = index; // Actualiza la tabla seleccionada para la fila específica
  }

  sendInformation(row: number) {
    const index = this.rows[row];
    const _V5: number[] = this.modoPagosData[row].filter(mdpg => mdpg.selected).map(mdpg => mdpg.ID); //MODOS DE PAGO
    const _V6: number[] = this.buroData[row].filter(buro => buro.selected).map(buro => buro.ID); //BURO
    const _V7: number[] = this.ciudadData[row].filter(ciudad => ciudad.selected).map(ciudad => ciudad.CIUDAD_ID); //CIUDADES
    const _V8: number[] = this.sectoresData[row].filter(sector => sector.selected).map(sector => sector.SECTOR_ID); //SECTORES
    const selectedDiasGozados = this.diasGozadosData[row].find(dias => dias.selected);
    const _V10 = selectedDiasGozados ? selectedDiasGozados.NAME : null; //DIAS GOZADOS
    const options = this.optionsData[row];
    let _diccionario: { [key: string]: any } = {'SERVICIO': index._V1, 'PLAN': index._V2, 'VARIANT': index._V3, 'PRODUCTO': index._V4, 'MODOS_PAGO': _V5, 
      'BURO': _V6, 'CIUDADES': _V7, ' SECTORES': _V8, 'PRECIO_PROMOCIONAL': index._V9, 'DIAS': _V10, 'UPGRADE': index._V11};
    if (options[0].selected){
      this.send.injectionData(_diccionario);
    } 
    if (options[1].selected){
      const _dStreaming = {}
    }
    if (options[2].selected){
      const _dTelefonia = {'PLAN': index.PRAD_TF_V1, 'PRECIO_PROMOCIONAL': index.PRAD_TF_V2, 'CANTIDAD': index.PRAD_TF_V3, ' MESES': index.PRAD_TF_V4}
      _diccionario['TELEFONIA'] = _dTelefonia;
    }
    if (options[3].selected){
      const _dTelevision = {'PLAN': index.PRAD_TV_V1, 'PRECIO_PROMOCIONAL': index.PRAD_TV_V2, 'CANTIDAD': index.PRAD_TV_V3, ' MESES': index.PRAD_TV_V4}
      _diccionario['TELEVISION'] = _dTelevision;
    }
    if (options.length > 4 && options[4].selected){
      const _dRouter = {'MODELO': index.PRAD_RT_V1, 'PRECIO_PROMOCIONAL': index.PRAD_RT_V2, 'CANTIDAD': index.PRAD_RT_V3, ' MESES': index.PRAD_RT_V4}
      _diccionario['ROUTER'] = _dRouter;
    }
  }

  validate(plan: number, prec: number, cant: number, meses: number, index: number, type: string): void {
    if(plan && prec && cant && meses && (type == 'TELEFONIA' || type == 'TELEVISION' || type == 'ROUTER')){
      this.vPA[index][type] = true;
    }
  }

  validatePrice(inputValue: number, maxPrice: number, type: string): boolean {
    if(type != 'STREAMING'){
      if(inputValue <= maxPrice){
        this.vPR[this.rowId][type] = true;
        return true
      } else {
        this.vPR[this.rowId][type] = false;
        return false
      }
    } else {
      if(inputValue <= maxPrice){
        //this.vPRS[this.rowId][this.tableId]['STREAMING'] = true;
        return true
      } else {
        //this.vPRS[this.rowId][this.tableId]['STREAMING'] = false;
        return false
      }
    }
  }
}