import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { PrecioRegular } from '../../../../interfaces/DataPromocional/precio-regular.interface';
import { environment } from '../../../../environments/environment';

const MAIN_URL = environment.MAIN_URL;
const API_GET_FINANCE = environment.API_GET_FINANCE;
const DataPromo = environment.API_GET_FINANCE_DTPR

@Injectable({
  providedIn: 'root'
})
export class PrecioRegularService {

  constructor(private http:HttpClient) { }

  getPrecioRegular(id_Producto: number, TFPV: number):Observable<PrecioRegular[]>{
    let params = new HttpParams().set('type', 'PRECIO_REGULAR')
    .set('TARIFFPLANVARIANT', TFPV.toString())
    .set('id_Prod', id_Producto.toString());
    return this.http.get<PrecioRegular[]>(MAIN_URL+API_GET_FINANCE+DataPromo, { params: params });
  }

}
