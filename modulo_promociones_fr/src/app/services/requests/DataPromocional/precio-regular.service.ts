import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { PrecioRegular } from '../../../interfaces/DataPromocional/precio-regular.interface';

@Injectable({
  providedIn: 'root'
})
export class PrecioRegularService {

  private baseUrl ='';

  constructor(private http:HttpClient) { }

  getPrecioRegular(id_Producto: number, TFPV: number):Observable<PrecioRegular[]>{
    let params = new HttpParams().set('type', 'PRECIO_REGULAR')
                                  .set('id_Producto', id_Producto.toString())
                                  .set('TFPV', TFPV.toString());
    return this.http.get<PrecioRegular[]>(this.baseUrl, { params: params });
  }

}
