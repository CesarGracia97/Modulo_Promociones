import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Ofertas } from '../interfaces/ofertas.interface';

@Injectable({
  providedIn: 'root'
})
export class OfertasSService {

  private baseUrl ='http://127.0.0.1:5012/api/ra/plnofer_endpoint';

  constructor(private http:HttpClient) { }

  getOfertasALL():Observable<Ofertas[]>{
    let params = new HttpParams().set('type', 'ALL_DATA')
    .set('stype', 'OFER');
    return this.http.get<Ofertas[]>(this.baseUrl, { params: params });
  }
}
