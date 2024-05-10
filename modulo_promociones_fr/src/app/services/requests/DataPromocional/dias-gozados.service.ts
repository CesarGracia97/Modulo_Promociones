import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { DiasGozados } from '../../../interfaces/DataPromocional/dias-gozados.interface';

@Injectable({
  providedIn: 'root'
})
export class DiasGozadosService {

  private baseUrl ='http://127.0.0.1:5014/api/ra/dtpro_endpoint';

  constructor(private http:HttpClient) { }

  getDiasGozados():Observable<DiasGozados[]>{
    let params = new HttpParams().set('type', 'DIAS_GOZADOS');
    return this.http.get<DiasGozados[]>(this.baseUrl, { params: params });
  }
}
