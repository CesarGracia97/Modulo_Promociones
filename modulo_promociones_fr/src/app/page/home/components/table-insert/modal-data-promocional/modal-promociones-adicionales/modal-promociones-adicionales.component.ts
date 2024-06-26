import { Component, OnInit } from '@angular/core';
import { DataViewService } from '../../../../../../services/subscribeData/data-view.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Options_PA } from '../../../../../../interfaces/Interfaces-View/Options_PA.interface';
import { FdPlanesService } from '../../../../../../services/fetchData/fd-planes.service';
import { FdCombosService } from '../../../../../../services/fetchData/fd-combos.service';
import { TariffPlanesVariant } from '../../../../../../interfaces/planes/tariffplanes.interface';
import { PrecioRegular } from '../../../../../../interfaces/DataPromocional/precio-regular.interface';
import { Productos } from '../../../../../../interfaces/planes/productos.interface';
import { DataPromocionInformationService } from '../../../../../../services/subscribeData/data-promocion-information.service';
import { DataPromocionSupportService } from '../../../../../../services/subscribeData/data-promocion-support.service';
import { DataProdadicInformationService } from '../../../../../../services/subscribeData/data-prodadic-information.service';
import { FdPrecioRegularService } from '../../../../../../services/fetchData/DataPromocional/fd-precio_regular.service';
import { Ciudades } from '../../../../../../interfaces/places/ciudad.interface';
import { Buro } from '../../../../../../interfaces/financial/buro.interface';
import { ModosPago } from '../../../../../../interfaces/financial/modos-pago.interface';
import { DiasGozados } from '../../../../../../interfaces/DataPromocional/dias-gozados.interface';

@Component({
  selector: 'app-modal-promociones-adicionales',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './modal-promociones-adicionales.component.html',
  styleUrl: './modal-promociones-adicionales.component.scss'
})
export class ModalPromocionesAdicionalesComponent implements OnInit {

  //Variables Visuales
  rowId: number = 0; rowData: any = {};
  pa_state: boolean = false; showPROAD: boolean[] = []; closing: boolean = false;
  optionsData: Options_PA[][] = [];
  selectedTableIndex: number[] = [];
  //Variables de Datos Externos
  modoPagosData: ModosPago[][] = []; buroData: Buro[][] = []; 
  diasGozadosData: DiasGozados[][] = [];
  //Variables de Datos
  paquetesStreaming: TariffPlanesVariant[][] = [];
  planesTelefonicos: TariffPlanesVariant[][] = []; planesTelevisivos: TariffPlanesVariant[][] = [];
  modelosRouter: Productos[][] = [];
  precioRegularTelefoniaData: PrecioRegular[][] = []; precioRegularTelevisioData: PrecioRegular[][] = [];
  precioRegularRouter: PrecioRegular[][] = []; precioRegularStreamingData: PrecioRegular[][][] = [];
  ciudadData: Ciudades[][] = [];
  idVariant: number[][] = [];

  //Dicionario de datos
  diccionario: { [key: string]: any }[] = [];

  constructor(
    private data_views: DataViewService,
    private data_information: DataPromocionInformationService,
    private data_promo_adi: DataProdadicInformationService,
    private support: DataPromocionSupportService,
    private fd_place: FdPlanesService,
    private fd_combos: FdCombosService,
    private fd_precio: FdPrecioRegularService

  ){}

  ngOnInit(): void {
    this.data_views.dRows$.subscribe(data => { if(data)this.rowData = data });
    this.data_views.dIndex$.subscribe(data => {this.rowId = data; if (!this.selectedTableIndex[this.rowId]) this.selectedTableIndex[this.rowId] = 0; }); // Inicializar selectedTableIndex para la fila actual si no existe
    this.data_views.dModalViewPA$.subscribe(data => { this.pa_state = data });
    this.data_views.dOptionsDataView$.subscribe(data => { this.optionsData = data });
    this.data_information.dDiccionario$.subscribe(data => { this.diccionario = data });
    this.data_information.dCiudades$.subscribe(data => {this.ciudadData = data});
    this.data_promo_adi.dPrRegST$.subscribe(data => {this.precioRegularStreamingData = data});
    this.data_promo_adi.dPrRefTF$.subscribe(data => {this.precioRegularTelefoniaData = data});
    this.data_promo_adi.dPrRefTV$.subscribe(data => {this.precioRegularTelevisioData = data});
    this.data_promo_adi.dPrRefRT$.subscribe(data => {this.precioRegularRouter = data});
    this.data_promo_adi.dPaquetesStreaming$.subscribe(data => {this.paquetesStreaming = data});
    this.data_promo_adi.dPlanesTelefonicos$.subscribe(data => {this.planesTelefonicos = data});
    this.data_promo_adi.dPlanesTelevisivos$.subscribe(data => {this.planesTelevisivos = data});
    this.data_promo_adi.dModelosRouter$.subscribe(data => {this.modelosRouter = data});
    this.support.dVariantId$.subscribe(data => {this.idVariant = data});
    this.data_information.dModoPago$.subscribe( data => {this.modoPagosData = data});
    this.data_information.dBuro$.subscribe( data => {this.buroData = data});
    this.data_information.dDiasGozados$.subscribe( data => { this.diasGozadosData = data});
  }

  closeModalProductosAdicionales(): void {
    this.data_views.stateModalPA(false);
  }

  getPrecioRegular(PlanesPaquetesModelos: number, type: string): void {
    const variantId = this.idVariant[this.rowId] ? this.idVariant[this.rowId][0] : null;
    if(PlanesPaquetesModelos){
      if(type == "STREAMING"){
        this.fd_precio.fetchDataPrecioRegularPA(1000065, PlanesPaquetesModelos, this.rowId, this.selectedTableIndex[this.rowId], type);
        this.diccionario[this.rowId]['STREAMING'][this.selectedTableIndex[this.rowId]] = [];
        this.diccionario[this.rowId]['STREAMING'][this.selectedTableIndex[this.rowId]]['PAQUETES'] = PlanesPaquetesModelos;
        this.data_information.sendDataUptadeDiccionario(this.diccionario[this.rowId], this.rowId);
      } else if(type == "TELEFONIA") {
        //
      } else if(type == "TELEVISION") {
        this.fd_precio.fetchDataPrecioRegularPA(this.darIdProducto(), PlanesPaquetesModelos, this.rowId, 0, type);
        this.diccionario[this.rowId]['TELEVISION']['PLANES'] = PlanesPaquetesModelos;
        this.data_information.sendDataUptadeDiccionario(this.diccionario[this.rowId], this.rowId);
      } else if(variantId !== null && type == "ROUTER") {
        this.fd_precio.fetchDataPrecioRegularPA(PlanesPaquetesModelos, variantId, this.rowId, 0, type);
        this.diccionario[this.rowId]['ROUTER']['MODELO'] = PlanesPaquetesModelos;
        this.data_information.sendDataUptadeDiccionario(this.diccionario[this.rowId], this.rowId);
      }
    }
  }

  getPrecMIniMFinCantidad(value: number, mIni: number, mFin: string, cantidad: number, type: string): void {
    if(type == 'STREAMING'){
      if(value && mIni) {
        this.diccionario[this.rowId]['STREAMING'][this.selectedTableIndex[this.rowId]]['PRECIO REFERENCIAL'] = this.precioRegularStreamingData[this.rowId][this.selectedTableIndex[this.rowId]][0].PRECIO;
        this.diccionario[this.rowId]['STREAMING'][this.selectedTableIndex[this.rowId]]['PRECIO PROMOCIONAL'] = value;
        this.diccionario[this.rowId]['STREAMING'][this.selectedTableIndex[this.rowId]]['MES INICIO'] = mIni;
        if(!mFin || mFin == '') {
          this.diccionario[this.rowId]['STREAMING'][this.selectedTableIndex[this.rowId]]['MES FIN'] = 'SIEMPRE';
        } else if (mFin){
          this.diccionario[this.rowId]['STREAMING'][this.selectedTableIndex[this.rowId]]['MES FIN'] = mFin;
        }
        this.data_information.sendDataUptadeDiccionario(this.diccionario[this.rowId], this.rowId);
      }
    } else if (type == 'TELEVISION' || type == 'TELEFONIA' || type == 'ROUTER'){
      if(value && mIni && cantidad) {
        this.diccionario[this.rowId][type]['CANTIDAD'] = cantidad;
        this.diccionario[this.rowId][type]['PRECIO PROMOCIONAL'] = value;
        if(type =='TELEVISION') {
          this.diccionario[this.rowId][type]['PRECIO REFERENCIAL'] = this.precioRegularTelevisioData[this.rowId][0].PRECIO;
        } else if (type == 'TELEFONIA') {
          this.diccionario[this.rowId][type]['PRECIO REFERENCIAL'] = this.precioRegularTelefoniaData[this.rowId][0].PRECIO;
        } else if (type == 'ROUTER') {
          this.diccionario[this.rowId][type]['PRECIO REFERENCIAL'] = this.precioRegularRouter[this.rowId][0].PRECIO;
        }
        this.diccionario[this.rowId][type]['MES INICIO'] = mIni;
        if (!mFin || mFin == '') {
          this.diccionario[this.rowId][type]['MES FIN'] = 'SIEMPRE';
        } else if (mFin) {
          this.diccionario[this.rowId][type]['MES INICIO'] = mIni;
        }
        this.data_information.sendDataUptadeDiccionario(this.diccionario[this.rowId], this.rowId);
      }
    }
  }

  sendDiccionario(): void {
    const buro = this.buroData[this.rowId].filter(buro => buro.selected).map(buro => buro.ID);
    const modo = this.modoPagosData[this.rowId].filter(modo => modo.selected).map(modo => modo.ID);
    const dias = this.diasGozadosData[this.rowId].filter(dias => dias.selected).map(dias => dias.NAME);
    if(buro != null && modo != null && dias != null){
      this.diccionario[this.rowId]['BURO'] = buro;
      this.diccionario[this.rowId]['MODO DE PAGO'] = modo;
      this.diccionario[this.rowId]['DIAS GOZADOS'] = dias;
      this.data_information.sendDataUptadeDiccionario(this.diccionario[this.rowId], this.rowId);
    }
    console.log(this.diccionario[this.rowId]);
  }

  darIdProducto(): number {
    const idsEspeciales = [95999, 96010, 96007];
    const ciudadesSeleccionadas = this.ciudadData[this.rowId].filter(ciudad => ciudad.selected);
    const idsSeleccionados = ciudadesSeleccionadas.map(ciudad => ciudad.CIUDAD_ID);
    const todosIdsEspecialesSeleccionados = idsEspeciales.every(id => idsSeleccionados.includes(id));
    if (todosIdsEspecialesSeleccionados) {
        return 170;
    } else {
        return 5;
    }
  }

  openDropDown(): void {
    if (this.showPROAD) {
      this.closing = true;
      setTimeout(() => {
        this.showPROAD[this.rowId] = !this.showPROAD[this.rowId];
        this.closing = false;
      }, 30); // Espera el tiempo de la transición de cierre
    }
  }

  updateSelection(index: number): void {
    const options = this.optionsData[this.rowId];
    if (index === 0 && options[0].selected) { // "NO APLICAR" ha sido seleccionado
      options.forEach((option, idx) => {
        if (idx !== 0) option.selected = false;
      });
    } else if (index !== 0 && options[index].selected) { // Otra opción que no es "NO APLICAR" ha sido seleccionada
      options[0].selected = false;
    }
    if (index === 1 && options[1].selected){
      this.fd_place.fetchDataTariffPlanVariantXProductoAdicional('STREAMING', this.rowId, this.selectedTableIndex[this.rowId])
      this.diccionario[this.rowId]['STREAMING'] = [];
      this.data_information.sendDataUptadeDiccionario(this.diccionario[this.rowId], this.rowId);
    } else if (index === 2 && options[2].selected) {
      this.fd_place.fetchDataTariffPlanVariantXProductoAdicional('TELEFONIA', this.rowId, 0)
      this.diccionario[this.rowId]['TELEFONIA'] = [];
      this.data_information.sendDataUptadeDiccionario(this.diccionario[this.rowId], this.rowId);
    } else if (index == 3 && options[3].selected) {
      this.fd_place.fetchDataTariffPlanVariantXProductoAdicional('TELEVISION', this.rowId, 0)
      this.diccionario[this.rowId]['TELEVISION'] = [];
      this.data_information.sendDataUptadeDiccionario(this.diccionario[this.rowId], this.rowId);
    } else if (index == 4 && options[4].selected){
      this.fd_combos.fetchDataComboPROD_ROUTER(this.rowId);
      this.diccionario[this.rowId]['ROUTER'] = [];
      this.data_information.sendDataUptadeDiccionario(this.diccionario[this.rowId], this.rowId);
    }
  }

  addNewTable(): void {
    const newTable = {
      id: this.rowData.tablas.length,
      PRAD_V1: '', PRAD_ST_V2: '', PRAD_ST_V3: '', PRAD_ST_V4: ''
    };
    this.rowData.tablas.push(newTable);
    this.selectedTableIndex[this.rowId] = this.rowData.tablas.length - 1;
  }

  changeTable(event: Event): void {
    const target = event.target as HTMLSelectElement;
    this.selectedTableIndex[this.rowId] = parseInt(target.value, 10);
  }
}
