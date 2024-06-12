import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ModosPago } from '../../../../interfaces/financial/modos-pago.interface';
import { environment } from '../../../../environments/environment';

const MAIN_URL = environment.MAIN_URL;
const API_GET_FINANCE = environment.API_GET_FINANCE;
const MDPG = environment.API_GET_FINANCE_MDPG;

@Injectable({
  providedIn: 'root'
})
export class FormaspagoService {

  constructor(private http:HttpClient) { }

  getModosPago():Observable<ModosPago[]> {
    let params = new HttpParams().set('type', 'ALL_MPAGOS');
    return this.http.get<ModosPago[]>(MAIN_URL+API_GET_FINANCE+MDPG, { params: params });
  }
}
