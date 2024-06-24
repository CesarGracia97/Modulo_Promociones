import { Injectable } from '@angular/core';
import { Buro } from '../../interfaces/financial/buro.interface';
import { ModosPago } from '../../interfaces/financial/modos-pago.interface';
import { Ciudades } from '../../interfaces/places/ciudad.interface';
import { Sectores } from '../../interfaces/places/sector.interface';
import { DataPromocionInformationService } from '../subscribeData/data-promocion-information.service';

@Injectable({
  providedIn: 'root'
})
export class ToggleSelectAllService {
  private modoPagosData: ModosPago[][] = [];
  private buroData: Buro[][] = [];
  private ciudadData: Ciudades[][] = [];
  private sectoresData: Sectores[][] = [];
  
  constructor(
    private data_information: DataPromocionInformationService
  ) { 
    this.data_information.dModoPago$.subscribe( data => {this.modoPagosData = data});
    this.data_information.dBuro$.subscribe( data => {this.buroData = data});
    this.data_information.dCiudades$.subscribe( data => {this.ciudadData = data});
    this.data_information.dSectores$.subscribe( data => {this.sectoresData = data});
  }

  SelectTypeALL(event: any, type: string, rowId: number){
    const isChecked = event.target.checked;
    switch(type){
      case 'MP':
        this.modoPagosData[rowId]?.forEach(mdpg => { mdpg.selected = isChecked; });
        break;
      case 'B':
        this.buroData[rowId]?.forEach(buro => { buro.selected = isChecked; });
        break;
      case 'C':
        this.ciudadData[rowId]?.forEach(ciudad => { ciudad.selected = isChecked; });
        break;
      case 'S':
        this.sectoresData[rowId]?.forEach(sector => { sector.selected = isChecked; });
        break;
    }
  }
}
