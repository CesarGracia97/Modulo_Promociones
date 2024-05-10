import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { PrecioRegular } from '../../../interfaces/DataPromocional/precio-regular.interface';

@Injectable({
  providedIn: 'root'
})
export class PrecioRegularService {

  private baseUrl ='http://127.0.0.1:5014/api/ra/dtpro_endpoint';

  constructor(private http:HttpClient) { }

  getPrecioRegular(id_Producto: number, TFPV: number):Observable<PrecioRegular[]>{
    let params = new HttpParams().set('type', 'PRECIO_REGULAR').set('TFPV', TFPV.toString())
    .set('id_Prod', id_Producto.toString());
    return this.http.get<PrecioRegular[]>(this.baseUrl, { params: params });
  }

}
