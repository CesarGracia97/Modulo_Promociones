import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Servicios } from '../interfaces/servicios.interface';

@Injectable({
  providedIn: 'root'
})
export class ServiciosService {

  private baseUrl ='http://127.0.0.1:5012/api/ra/plnserv_endpoint';

  constructor(private http:HttpClient) { }

  getServiciosALL():Observable<Servicios[]>{
    let params = new HttpParams().set('type', 'ALL_DATA')
    .set('stype', 'SERV');
    return this.http.get<Servicios[]>(this.baseUrl, { params: params });
  }
}
