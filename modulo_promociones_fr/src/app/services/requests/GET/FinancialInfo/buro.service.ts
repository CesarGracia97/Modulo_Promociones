import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/internal/Observable';
import { Buro } from '../../../../interfaces/financial/buro.interface';
import { environment } from '../../../../environments/environment';

const MAIN_URL = environment.MAIN_URL;
const API_GET_FINANCE = environment.API_GET_FINANCE
const BURO = environment.API_GET_FINANCE_BURO 

@Injectable({
  providedIn: 'root'
})
export class BuroService {

  constructor(private http:HttpClient) { }

  getTiposBuro():Observable<Buro[]>{
    let params = new HttpParams().set('type', 'ALL_BURO');
    return this.http.get<Buro[]>(MAIN_URL+API_GET_FINANCE+BURO, { params: params });
  }
}
