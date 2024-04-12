import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Ofertas } from '../../interfaces/planes/ofertas.interface';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class OfertasService {
  private baseUrl ='http://127.0.0.1:5013/api/ra/plnofer_endpoint';

  constructor(private http:HttpClient) { }

  getOfertasALL():Observable<Ofertas[]>{
    let params = new HttpParams().set('type', 'ALL_DATA')
    .set('stype', 'OFER');
    return this.http.get<Ofertas[]>(this.baseUrl, { params: params });
  }
}
