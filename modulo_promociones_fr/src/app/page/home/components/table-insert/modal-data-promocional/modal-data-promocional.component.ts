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

@Component({
  selector: 'app-modal-data-promocional',
  standalone: true,
  imports: [CommonModule, FormsModule, ModalCiudadesysectoresComponent, ModalPromocionesAdicionalesComponent,
    ModalEntidadesComponent, ModalTarjetasComponent],
  templateUrl: './modal-data-promocional.component.html',
  styleUrl: './modal-data-promocional.component.scss'
})
export class ModalDataPromocionalComponent implements OnInit {
  //Variables de Vista
  rowId: number = 0; rowData: any[] = [];
  dp_state: boolean = false;
  showDDMP: boolean[] = []; showDDB: boolean[] = []; closing: boolean = false; 
  permitirPA: boolean = false;
  //V. de Datos b1
  serviciosData: Servicios[] = []; planData: TariffPlanes[][] = []; planVData: TariffPlanesVariant[][] = [];
  productosData: Productos[][] = []; canalData: Canales[][] = [];
  //V. de Datos b2
  modoPagosData: ModosPago[][] = []; buroData: Buro[][] = []; 
  //V. de Datos b2
  upgradeData: Upgrade [][] = []; diasGozadosData: DiasGozados[][] = []; precioRegularData: PrecioRegular[][] = [];

  constructor(
    private data_views: DataViewService,
    private data_information: DataPromocionInformationService,
    private fd_combos: FdCombosService, private fd_lugares: FdPlacesService,
    private fd_precios: FdPrecioRegularService,
    private fd_upgrade: FdUpgradeService
  ){}

  ngOnInit(): void {
    this.data_views.dIndex$.subscribe( data => {this.rowId = data});
    this.data_views.dRows$.subscribe( data => {this.rowData = data});
    this.data_views.dModalViewDP$.subscribe( data => {this.dp_state = data});
    this.data_information.dServicios$.subscribe( data => {this.serviciosData = data;});
    this.data_information.dPlan$.subscribe( data => {this.planData = data});
    this.data_information.dPlanV$.subscribe( data => {this.planVData = data});
    this.data_information.dProductos$.subscribe( data => {this.productosData = data});
    this.data_information.dCanal$.subscribe( data => {this.canalData = data});
    this.data_information.dModoPago$.subscribe( data => {this.modoPagosData = data});
    this.data_information.dBuro$.subscribe( data => {this.buroData = data})
    this.data_information.dUpgrade$.subscribe( data => {this.upgradeData = data});
    this.data_information.dDiasGozados$.subscribe( data => { this.diasGozadosData = data});
    this.data_information.dPrecioRegular$.subscribe( data => {this.precioRegularData = data});
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
    }
  }

  getPLANVARIANT(IdPlan: number): void{
    if(IdPlan)
      this.fd_combos.fetchDataComboPLANVARIANT(IdPlan, this.rowId)
  }

  getPROD_CiudadesTariffplanVariantProducto(IdVariant: number, ProductoId: number): void {
    if(IdVariant){
      this.fd_combos.fetchDataComboPROD(IdVariant, this.rowId);
      if(IdVariant && ProductoId){
        this.fd_lugares.fetchDataCiudadesALLXTariffplanVariant(IdVariant, ProductoId, this.rowId);
        this.fd_precios.fetchDataPrecioRegular(ProductoId, IdVariant, this.rowId);
      }
    }
  }

  getDataUpgrade(SERVICIO: string, id_Plan: number, IdVariant: number): void {
    if((SERVICIO && SERVICIO == 'INTERNET') && id_Plan && IdVariant)
      this.fd_upgrade.fetchDataUpgrade(id_Plan, IdVariant, this.rowId)
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
}
