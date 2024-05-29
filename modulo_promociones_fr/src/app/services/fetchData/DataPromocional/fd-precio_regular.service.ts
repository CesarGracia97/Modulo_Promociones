import { Injectable } from '@angular/core';
import { PrecioRegular } from '../../../interfaces/DataPromocional/precio-regular.interface';
import { PrecioRegularService } from '../../requests/DataPromocional/precio-regular.service';
import { CommunicationDataService } from '../../communication/communicationData.service';

@Injectable({
  providedIn: 'root'
})
export class FdPrecioRegularService {
  private precioData: PrecioRegular[] = [];

  constructor(
    private prec: PrecioRegularService,
    private comData: CommunicationDataService
  ) { }

  getPrecioRegular(id_Producto: number, TFPV: number, index: number){
    this.prec.getPrecioRegular(id_Producto, TFPV).subscribe((response: any) => {
      if(response && response.PRECIO_REGULAR) {
        this.precioData = response.PRECIO_REGULAR.map((precio: any) => {
          return {
            PRECIO: precio.PRECIO
          }
        });
        this.comData.sendDataPrecioRegular(this.precioData, index);
      }
    })
  }
}
