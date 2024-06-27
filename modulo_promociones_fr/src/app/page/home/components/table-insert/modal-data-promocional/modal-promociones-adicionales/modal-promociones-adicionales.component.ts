import { Component, Input, OnInit } from '@angular/core';
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
  
  //Variables de Datos
  paquetesStreaming: TariffPlanesVariant[][] = [];
  planesTelefonicos: TariffPlanesVariant[][] = []; planesTelevisivos: TariffPlanesVariant[][] = [];
  modelosRouter: Productos[][] = [];
  precioRegularTelefoniaData: PrecioRegular[][] = []; precioRegularTelevisioData: PrecioRegular[][] = [];
  precioRegularRouter: PrecioRegular[][] = []; precioRegularStreamingData: PrecioRegular[][][] = [];

  //Dicionario de datos
  diccionario: { [key: string]: any }[] = [];

  constructor(
    private data_views: DataViewService,
    private fd_place: FdPlanesService,
    private fd_planes: FdCombosService,
    private data_promo_adicional: DataPromocionInformationService
  ){}

  ngOnInit(): void {
    this.data_views.dIndex$.subscribe( data => {this.rowId = data });
    this.data_views.dModalViewPA$.subscribe(data => { this.pa_state = data });
    this.data_views.dOptionsDataView$.subscribe(data => { this.optionsData = data });
    this.data_views.dRows$.subscribe(data => { if (data) { this.rowData = data }});
    this.data_promo_adicional.dDiccionario$.subscribe(data => { this.diccionario = data });
  }

  closeModalProductosAdicionales(): void {
    this.data_views.stateModalPA(false);
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
      //this.fd_place.fetchDataTariffPlanVariantXProductoAdicional('STREAMING', this.rowId, 0)
    } else if (index === 2 && options[2].selected) {
      this.fd_place.fetchDataTariffPlanVariantXProductoAdicional('TELEFONIA', this.rowId, 0)
    } else if (index == 3 && options[3].selected) {
      this.fd_place.fetchDataTariffPlanVariantXProductoAdicional('TELEVISION', this.rowId, 0)
    } else if (index == 4 && options[4].selected){
      this.fd_planes.fetchDataComboPROD_ROUTER(this.rowId);
    }
  }
}
