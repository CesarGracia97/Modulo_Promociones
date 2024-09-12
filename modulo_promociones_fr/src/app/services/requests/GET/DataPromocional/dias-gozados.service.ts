import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { DiasGozados } from '../../../../interfaces/DataPromocional/dias-gozados.interface';
import { environment } from '../../../../../environments/environment';

const MAIN_URL = environment.MAIN_URL;
const DIAS_GOZADOS = environment.API_GET_FINANCE_DIAS_GOZADOS;

@Injectable({
  providedIn: 'root'
})
export class DiasGozadosService {

  constructor(private http:HttpClient) { }

  getDiasGozados():Observable<DiasGozados[]>{
    let params = new HttpParams().set('type', 'DIAS_GOZADOS');
    return this.http.post<DiasGozados[]>(MAIN_URL+DIAS_GOZADOS, { params: params });
  }

  _getDiasGozados():Observable<DiasGozados[]>{
    let params = new HttpParams().set('type', 'DIAS_GOZADOS');
    return this.http.post<DiasGozados[]>(MAIN_URL+DIAS_GOZADOS, { params: params });
  }
}
