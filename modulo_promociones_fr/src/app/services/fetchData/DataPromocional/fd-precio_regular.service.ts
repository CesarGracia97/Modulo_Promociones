import { Injectable } from '@angular/core';
import { PrecioRegular } from '../../../interfaces/DataPromocional/precio-regular.interface';
import { PrecioRegularService } from '../../requests/GET/DataPromocional/precio-regular.service';
import { CommunicationDataService } from '../../communication/communicationData.service';
import { map, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FdPrecioRegularService {
  private precioData: PrecioRegular[] = [];

  constructor(
    private prec: PrecioRegularService,
    private comData: CommunicationDataService
  ) { }

  fetchDataPrecioRegular(id_Producto: number, TFPV: number, index: number){
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

  //RETORNO DIRECTO
  
  fetchDataPrecioRegular_RETURN(id_Producto: number, TFPV: number): Observable<PrecioRegular[]> {
    return this.prec.getPrecioRegular(id_Producto, TFPV).pipe(
      map((response: any) => {
        if(response && response.PRECIO_REGULAR){
          return response.PRECIO_REGULAR.map((precio: any) => {
            return {
              PRECIO: precio.PRECIO
            }
          })
        }
      })
    )
  }
}
