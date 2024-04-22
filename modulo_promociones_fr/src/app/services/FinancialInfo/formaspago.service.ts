import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ModosPago } from '../../interfaces/financial/modos-pago.interface';

@Injectable({
  providedIn: 'root'
})
export class FormaspagoService {

  private baseUrl ='http://127.0.0.1:5014/api/ra/fncmpag_endpoint';

  constructor(private http:HttpClient) { }

  getModosPago():Observable<ModosPago[]> {
    let params = new HttpParams().set('type', 'ALL_MPAGOS');
    return this.http.get<ModosPago[]>(this.baseUrl, { params: params });
  }
}
