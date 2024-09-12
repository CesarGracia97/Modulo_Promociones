import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ModosPago } from '../../../../interfaces/financial/modos-pago.interface';
import { environment } from '../../../../../environments/environment';

const MAIN_URL = environment.MAIN_URL;
const MDPG = environment.API_GET_FINANCE_MDPG;

@Injectable({
  providedIn: 'root'
})
export class FormaspagoService {

  constructor(private http:HttpClient) { }

  getModosPago():Observable<ModosPago[]> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: 'ihjqbhwbehbecbcehws',
      channel: 'web-modulos-promocionales',
      type: 'ALL_MPAGOS'
    }
    return this.http.post<ModosPago[]>(MAIN_URL+MDPG, body, { headers });
  }
}
