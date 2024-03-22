import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Tecnologias } from '../interfaces/tecnologias.interface';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TecnologiasService {

  private baseUrl ='http://127.0.0.1:5012/api/ra/plntecn_endpoint';

  constructor(private http:HttpClient) { }

  getTecnologiasALL():Observable<Tecnologias[]>{
    let params = new HttpParams().set('type', 'ALL_DATA')
    .set('stype', 'TECN');
    return this.http.get<Tecnologias[]>(this.baseUrl, { params: params });
  }
}
