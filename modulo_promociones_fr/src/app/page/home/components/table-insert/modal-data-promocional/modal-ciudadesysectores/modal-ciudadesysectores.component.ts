import { Component, OnInit } from '@angular/core';
import { DataPromocionInformationService } from '../../../../../../services/subscribeData/data-promocion-information.service';
import { DataViewService } from '../../../../../../services/subscribeData/data-view.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Ciudades } from '../../../../../../interfaces/places/ciudad.interface';
import { Sectores } from '../../../../../../interfaces/places/sector.interface';
import { FdPlacesService } from '../../../../../../services/fetchData/fd-places.service';

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

  constructor(
    private data_views: DataViewService,
    private data_information: DataPromocionInformationService,
    private fdata_place: FdPlacesService
  ){}
  
  ngOnInit(): void {
    this.data_views.dIndex$.subscribe( data => {this.rowId = data});
    this.data_views.dModalViewCS$.subscribe( data => {this.cs_state = data});
    this.data_information.dCiudades$.subscribe( data => {this.ciudadData = data});
    this.data_information.dSectores$.subscribe( data => {this.sectoresData = data});
  }

  closeModalCiudades_y_Sectores(): void {
    this.data_views.stateModalCS(false);
  }

  buscarSectores() {
    const ciudades = this.ciudadData[this.rowId].filter(city => city.selected).map(city => city.CIUDAD_ID);
    this.fdata_place.fetchDataSectoresMasivosXTariffplanVariantXProducto(ciudades, 0, 0, this.rowId);
  }

  disableBusqueda(): boolean {
    return this.ciudadData[this.rowId].some(ciudad => ciudad.selected);
  }
}
