import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Ofertas } from '../../../../interfaces/planes/ofertas.interface';
import { Observable } from 'rxjs';
import { environment } from '../../../../../environments/environment';

const MAIN_URL = environment.MAIN_URL;
const API_GET_PLANES = environment.API_GET_PLANES;
const OFERTA = environment.API_GET_PLANES_OFER;

@Injectable({
  providedIn: 'root'
})
export class OfertasService {

  constructor(private http:HttpClient) { }

  getOfertasALL():Observable<Ofertas[]>{
    let params = new HttpParams().set('type', 'ALL_DATA')
    .set('stype', 'OFER');
    return this.http.get<Ofertas[]>(MAIN_URL+API_GET_PLANES+OFERTA, { params: params });
  }
}
