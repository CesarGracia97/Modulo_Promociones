import { Component, OnInit } from '@angular/core';
import { DataPromocionInformationService } from '../../../../../../services/subscribeData/data-promocion-information.service';
import { DataViewService } from '../../../../../../services/subscribeData/data-view.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Ciudades } from '../../../../../../interfaces/places/ciudad.interface';
import { Sectores } from '../../../../../../interfaces/places/sector.interface';
import { FdPlacesService } from '../../../../../../services/fetchData/fd-places.service';
import { ToggleSelectAllService } from '../../../../../../services/complements/toggle-select-all.service';
import { DataPromocionSupportService } from '../../../../../../services/subscribeData/data-promocion-support.service';

@Component({
  selector: 'app-modal-ciudadesysectores',
  standalone: true,
  imports: [CommonModule, FormsModule,],
  templateUrl: './modal-ciudadesysectores.component.html',
  styleUrl: './modal-ciudadesysectores.component.scss'
})
export class ModalCiudadesysectoresComponent implements OnInit {

  //Variables de vista
  rowId: number = 0;
  cs_state: boolean = false;
  //Variables de datos
  ciudadData: Ciudades[][] = []; sectoresData: Sectores[][] = [];
  idVariant: number[][] = []; idProducto: number[][] = [];
  //Dicionario de datos
  diccionario: { [key: string]: any }[] = [];

  constructor(
    private data_views: DataViewService,
    private data_information: DataPromocionInformationService,
    private fdata_place: FdPlacesService,
    private complement: ToggleSelectAllService,
    private support: DataPromocionSupportService
  ){}
  
  ngOnInit(): void {
    this.data_views.dIndex$.subscribe( data => {this.rowId = data});
    this.data_views.dModalViewCS$.subscribe( data => {this.cs_state = data});
    this.data_information.dCiudades$.subscribe( data => {this.ciudadData = data});
    this.data_information.dSectores$.subscribe( data => {this.sectoresData = data});
    this.support.dProductoId$.subscribe( data => {this.idProducto = data});
    this.support.dVariantId$.subscribe( data => {this.idVariant = data});
    this.data_information.dDiccionario$.subscribe( data => {this.diccionario = data});
  }

  closeModalCiudades_y_Sectores(): void {
    const sectores = this.sectoresData[this.rowId].filter(sect => sect.selected).map(sect => sect.SECTOR_ID);
    if (sectores.length > 0) {
      this.diccionario[this.rowId]['SECTORES'] = sectores;
      this.data_information.sendDataUptadeDiccionario(this.diccionario[this.rowId], this.rowId);
    }
    this.data_views.stateModalCS(false);
  }

  buscarSectores() {
    const ciudades = this.ciudadData[this.rowId].filter(city => city.selected).map(city => city.CIUDAD_ID);
    const variantId = this.idVariant[this.rowId] ? this.idVariant[this.rowId][0] : null; // Asegúrate de obtener un solo valor
    const productoId = this.idProducto[this.rowId] ? this.idProducto[this.rowId][0] : null;
    if (variantId !== null && productoId !== null){
      this.fdata_place.fetchDataSectoresMasivosXTariffplanVariantXProducto(ciudades, variantId, productoId, this.rowId);
      this.diccionario[this.rowId]['CIUDADES'] = ciudades;
      this.data_information.sendDataUptadeDiccionario(this.diccionario[this.rowId], this.rowId);
    }
  }

  disableBusqueda(): boolean {
    return this.ciudadData[this.rowId]?.some(ciudad => ciudad.selected);
  }

  toggleSelectAllCheckboxes(event: any, type: string){
    this.complement.SelectTypeALL(event, type, this.rowId)
  }
}
