import { Component, Input, OnInit } from '@angular/core';
import { DataViewService } from '../../../../../services/subscribeData/data-view.service';
import { CommonModule } from '@angular/common';
import { DataPromocionInformationService } from '../../../../../services/subscribeData/data-promocion-information.service';
import { Servicios } from '../../../../../interfaces/planes/servicios.interface';
import { TariffPlanes, TariffPlanesVariant } from '../../../../../interfaces/planes/tariffplanes.interface';
import { Productos } from '../../../../../interfaces/planes/productos.interface';
import { Buro } from '../../../../../interfaces/financial/buro.interface';
import { ModosPago } from '../../../../../interfaces/financial/modos-pago.interface';
import { DiasGozados } from '../../../../../interfaces/DataPromocional/dias-gozados.interface';
import { PrecioRegular } from '../../../../../interfaces/DataPromocional/precio-regular.interface';
import { Upgrade } from '../../../../../interfaces/DataPromocional/upgrade.interface';
import { Canales } from '../../../../../interfaces/financial/canales.interface';
import { FdCombosService } from '../../../../../services/fetchData/fd-combos.service';
import { FdPlacesService } from '../../../../../services/fetchData/fd-places.service';
import { FdPrecioRegularService } from '../../../../../services/fetchData/DataPromocional/fd-precio_regular.service';
import { FdUpgradeService } from '../../../../../services/fetchData/DataPromocional/fd-upgrade.service';
import { FormsModule } from '@angular/forms';
import { ModalCiudadesysectoresComponent } from './modal-ciudadesysectores/modal-ciudadesysectores.component';
import { ModalPromocionesAdicionalesComponent } from './modal-promociones-adicionales/modal-promociones-adicionales.component';
import { ModalEntidadesComponent } from './modal-entidades/modal-entidades.component';
import { ModalTarjetasComponent } from './modal-tarjetas/modal-tarjetas.component';
import { ToggleSelectAllService } from '../../../../../services/complements/toggle-select-all.service';
import { DataPromocionSupportService } from '../../../../../services/subscribeData/data-promocion-support.service';
import { ModalUpgradeComponent } from './modal-upgrade/modal-upgrade.component';

@Component({
  selector: 'app-modal-data-promocional',
  standalone: true,
  imports: [CommonModule, FormsModule, ModalCiudadesysectoresComponent, ModalPromocionesAdicionalesComponent,
    ModalEntidadesComponent, ModalTarjetasComponent, ModalUpgradeComponent],
  templateUrl: './modal-data-promocional.component.html',
  styleUrl: './modal-data-promocional.component.scss'
})
export class ModalDataPromocionalComponent implements OnInit {
  //Variables de Vista
  rowId: number = 0;   rowData: any = {};
  dp_state: boolean = false;
  showDDMP: boolean[] = []; showDDB: boolean[] = []; closing: boolean = false; 
  permitirPA: boolean = false; precValid: boolean[] = [];
  //V. de Datos
  serviciosData: Servicios[] = []; planData: TariffPlanes[][] = []; planVData: TariffPlanesVariant[][] = [];
  productosData: Productos[][] = []; canalData: Canales[][] = [];
  modoPagosData: ModosPago[][] = []; buroData: Buro[][] = []; 
  upgradeData: Upgrade [][] = []; diasGozadosData: DiasGozados[][] = []; precioRegularData: PrecioRegular[][] = [];
  //Validaciones de errores
  errorM_V19: string[] = []; errorM_V20: string[] = [];


  //Dicionario de datos
  diccionario: { [key: string]: any }[] = [];
  
  constructor(
    private data_views: DataViewService,
    private data_information: DataPromocionInformationService,
    private fd_combos: FdCombosService, 
    private fd_lugares: FdPlacesService,
    private fd_precios: FdPrecioRegularService,
    private fd_upgrade: FdUpgradeService,
    private complement: ToggleSelectAllService,
    private support: DataPromocionSupportService
  ){}

  ngOnInit(): void {
    this.data_views.dIndex$.subscribe( data => {this.rowId = data});
    this.data_views.dRows$.subscribe( data => {if(data)this.rowData = data});
    this.data_views.dModalViewDP$.subscribe( data => {this.dp_state = data});
    this.data_information.dServicios$.subscribe( data => {this.serviciosData = data;});
    this.data_information.dPlan$.subscribe( data => {this.planData = data});
    this.data_information.dPlanV$.subscribe( data => {this.planVData = data});
    this.data_information.dProductos$.subscribe( data => {this.productosData = data});
    this.data_information.dCanal$.subscribe( data => {this.canalData = data});
    this.data_information.dModoPago$.subscribe( data => {this.modoPagosData = data});
    this.data_information.dBuro$.subscribe( data => {this.buroData = data});
    this.data_information.dUpgrade$.subscribe( data => {this.upgradeData = data});
    this.data_information.dDiasGozados$.subscribe( data => { this.diasGozadosData = data});
    this.data_information.dPrecioRegular$.subscribe( data => {this.precioRegularData = data});
    this.data_information.dDiccionario$.subscribe( data => {this.diccionario = data});
  }

  closeModalDatosPromocionales(): void {
    this.data_views.stateModalDP(false);
  }

  getPLAN(SERVICIO: string): void {
    if(SERVICIO){
      if (SERVICIO == "INTERNET")
        this.data_views.sendOptionsPAView(true, this.rowId);
      if(SERVICIO != "INTERNET")
        this.data_views.sendOptionsPAView(false, this.rowId,);
      this.fd_combos.fetchDataComboPLAN(SERVICIO, this.rowId);
      this.diccionario[this.rowId]['SERVICIO'] = SERVICIO;
      this.data_information.sendDataUptadeDiccionario(this.diccionario[this.rowId], this.rowId);
      this.support.sendDataServicio(SERVICIO, this.rowId);
    }
  }

  getPLANVARIANT(IdPlan: number): void{
    if(IdPlan)
      this.fd_combos.fetchDataComboPLANVARIANT(IdPlan, this.rowId)
    this.diccionario[this.rowId]['Plan_Id'] = IdPlan;
    this.data_information.sendDataUptadeDiccionario(this.diccionario[this.rowId], this.rowId);
  }

  getPROD_CiudadesTariffplanVariantProducto(idVariant: number, ProductoId: number): void {
    if(idVariant){
      this.fd_combos.fetchDataComboPROD(idVariant, this.rowId);
      if(idVariant && ProductoId){
        this.fd_lugares.fetchDataCiudadesALLXTariffplanVariant(idVariant, ProductoId, this.rowId);
        this.fd_precios.fetchDataPrecioRegular(ProductoId, idVariant, this.rowId);
        this.support.sendDataIdProducto(ProductoId, this.rowId);
        this.support.sendDataIdVariant(idVariant, this.rowId);
        this.diccionario[this.rowId]['Variant_Id'] = idVariant;
        this.diccionario[this.rowId]['Producto_Id'] = idVariant;
        this.data_information.sendDataUptadeDiccionario(this.diccionario[this.rowId], this.rowId);
      }
    }
  }

  getUpgrade(SERVICIO: string, id_Plan: number, IdVariant: number): void {
    if((SERVICIO && SERVICIO == 'INTERNET') && id_Plan && IdVariant)
      this.fd_upgrade.fetchDataUpgrade(id_Plan, IdVariant, this.rowId)
  }

  getCanalesPrecioUpgradeMIiMf(IdCanal: number, value: number, IdProdcuto: number, mInicio: number, mFin: string): void {
    this.validateV19(mInicio);
    this.validateV20(parseInt(mFin));
    if(IdCanal && value && IdProdcuto && mInicio){
      this.diccionario[this.rowId]['Canal'] = IdCanal;
      this.diccionario[this.rowId]['Precio Promocional'] = value;
      this.diccionario[this.rowId]['Precio Referencial'] = this.precioRegularData[this.rowId][0].PRECIO;
      this.diccionario[this.rowId]['Mes Inicio Promocion'] = mInicio
      if(!mFin || mFin ==''){
        this.diccionario[this.rowId]['Mes Fin Promocion'] = 'SIEMPRE';
      } else if(mFin) {
        this.diccionario[this.rowId]['Mes Fin Promocion'] = mFin;
      }
      this.data_information.sendDataUptadeDiccionario(this.diccionario[this.rowId], this.rowId);
    }
  }

  validateV19(value: number) {
    if (value < 0 || value > 24) {
      this.errorM_V19[this.rowId] = 'LIMITE SUPERADO 0-24';
    } else {
      this.errorM_V19[this.rowId] = '';
    }
  }

  validateV20(value: number) {
    if (value <= this.rowData._V19) {
      this.errorM_V20[this.rowId] = 'EL VALOR NO DEBE SER MENOR AL INICIAL';
    } else {
      this.errorM_V20[this.rowId]= '';
    }
  }

  openDropDown(type: string): void {
    switch(type){
      case 'MP':
        if (this.showDDMP) {
          this.closing = true;// Si está abierto y se va a cerrar, activa la transición rápida
          setTimeout(() => {
            this.showDDMP[this.rowId] = !this.showDDMP[this.rowId];
            this.closing = false;
          }, 30); // Espera el tiempo de la transición de cierre
        }
      break;
      case 'B':
        if (this.showDDB) {
          this.closing = true;// Si está abierto y se va a cerrar, activa la transición rápida
          setTimeout(() => {
            this.showDDB[this.rowId] = !this.showDDB[this.rowId];
            this.closing = false;
          }, 30); // Espera el tiempo de la transición de cierre
        }
      break;
    }
  }

  openModalCiudades_y_Sectores(): void {
    this.data_views.stateModalCS(true);
  }
  
  openModalProductosAdicionales(): void {
    this.data_views.stateModalPA(true);
  }

  openModalUpgrade(): void {
    this.data_views.stateModalUP(true);
  }

  toggleSelectAllCheckboxes(event: any, type: string){
    this.complement.SelectTypeALL(event, type, this.rowId)
  }

  validatePrice(value: number, precio_max: number): boolean {
    if(value){
      if(value <= 0 || value >= precio_max){
        this.precValid[this.rowId] = true;
        return true;
      } else {
        this.precValid[this.rowId] = false;
        return false;
      }
    }
    return false;
  }
}
