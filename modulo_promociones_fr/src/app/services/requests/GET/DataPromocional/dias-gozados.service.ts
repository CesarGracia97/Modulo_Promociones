import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { DiasGozados } from '../../../../interfaces/DataPromocional/dias-gozados.interface';
import { environment } from '../../../../environments/environment';

const MAIN_URL = environment.MAIN_URL;
const API_GET_FINANCE = environment.API_GET_FINANCE;
const DataPromo = environment.API_GET_FINANCE_DTPR

@Injectable({
  providedIn: 'root'
})
export class DiasGozadosService {

  constructor(private http:HttpClient) { }

  getDiasGozados():Observable<DiasGozados[]>{
    let params = new HttpParams().set('type', 'DIAS_GOZADOS');
    return this.http.get<DiasGozados[]>(MAIN_URL+API_GET_FINANCE+DataPromo, { params: params });
  }
}
