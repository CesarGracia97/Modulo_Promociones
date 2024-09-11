import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../../../environments/environment';
import { Observable } from 'rxjs';

const API_MAIN = environment.MAIN_URL;
const MODULO_PROMOCIONAL = environment.API_POST_MODULO_PROMOCIONAL;

@Injectable({
  providedIn: 'root'
})
export class SendDataPOSTService {
  
  constructor(private http: HttpClient) { }

  InjectionData_POST(data:{ [key: string]: any }): Observable<any> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    return this.http.post<any>(API_MAIN+MODULO_PROMOCIONAL, data, { headers });
  }
}
