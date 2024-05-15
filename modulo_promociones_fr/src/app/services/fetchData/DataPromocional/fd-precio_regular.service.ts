import { Injectable } from '@angular/core';
import { map, Observable } from 'rxjs';
import { PrecioRegular } from '../../../interfaces/DataPromocional/precio-regular.interface';
import { PrecioRegularService } from '../../requests/DataPromocional/precio-regular.service';

@Injectable({
  providedIn: 'root'
})
export class FdPrecioRegularService {

  constructor(
    private prec: PrecioRegularService
  ) { }

  getPrecioRegular_RETURN(id_Producto: number, TFPV: number): Observable<PrecioRegular[]> {
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
