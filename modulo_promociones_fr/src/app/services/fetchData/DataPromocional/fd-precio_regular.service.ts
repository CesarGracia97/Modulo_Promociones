import { Injectable } from '@angular/core';
import { PrecioRegular } from '../../../interfaces/DataPromocional/precio-regular.interface';
import { PrecioRegularService } from '../../requests/GET/DataPromocional/precio-regular.service';
import { DataPromocionInformationService } from '../../subscribeData/data-promocion-information.service';
import { map, Observable } from 'rxjs';
import { DataProdadicInformationService } from '../../subscribeData/data-prodadic-information.service';

@Injectable({
  providedIn: 'root'
})
export class FdPrecioRegularService {
  private precioData: PrecioRegular[] = [];

  constructor(
    private prec: PrecioRegularService,
    private data_promocion: DataPromocionInformationService,
    private data_adicional: DataProdadicInformationService
  ) { }

  fetchDataPrecioRegular(id_Producto: number, TFPV: number, index: number){
    this.prec.getPrecioRegular(id_Producto, TFPV).subscribe((response: any) => {
      if(response && response.PRECIO_REGULAR) {
        this.precioData = response.PRECIO_REGULAR.map((precio: any) => {
          return {
            PRECIO: precio.PRECIO
          }
        });
        this.data_promocion.sendDataPrecioRegular(this.precioData, index);
      }
    })
  }

  fetchDataPrecioRegularPA(ProductoId: number, VariantId: number, index: number, table: number, type: string){
    this.prec.getPrecioRegular(ProductoId, VariantId).subscribe((response: any) => {
      if(response && response.PRECIO_REGULAR) {
        this.precioData = response.PRECIO_REGULAR.map((precio: any) => {
          return {
            PRECIO: precio.PRECIO
          }
        });
        this.data_adicional.sendDataPreciosPA(this.precioData, index, table, type);
      }
    });
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
