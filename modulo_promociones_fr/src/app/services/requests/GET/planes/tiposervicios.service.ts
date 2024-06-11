import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { TipoServicios } from '../../../../interfaces/planes/tiposervicios.interface';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TiposerviciosService {

  private baseUrl ='http://127.0.0.1:5013/api/ra/plntise_endpoint';

  constructor(private http:HttpClient) { }

  getTipoServicioALL():Observable<TipoServicios[]>{
    let params = new HttpParams().set('type', 'ALL_DATA')
    .set('stype', 'TISE');
    return this.http.get<TipoServicios[]>(this.baseUrl, { params: params });
  }
}
