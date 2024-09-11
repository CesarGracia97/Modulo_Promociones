import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Servicios } from '../../../../interfaces/planes/servicios.interface';
import { environment } from '../../../../../environments/environment';

const MAIN_URL = environment.MAIN_URL;
const SERVIC = environment.API_GET_PLANES_SERV;

@Injectable({
  providedIn: 'root'
})
export class ServiciosService {

  constructor(private http:HttpClient) { }

  getServiciosALL():Observable<Servicios[]>{
    let params = new HttpParams().set('type', 'ALL_DATA')
    .set('stype', 'SERV');
    return this.http.get<Servicios[]>(MAIN_URL+SERVIC, { params: params });
  }
}
