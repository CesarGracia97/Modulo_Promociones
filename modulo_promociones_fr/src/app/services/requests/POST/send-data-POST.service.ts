import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../../../environments/environment';
import { Observable } from 'rxjs';

const API_MAIN = environment.MAIN_URL;
const API_POST = environment.API_BEND_POST;

@Injectable({
  providedIn: 'root'
})
export class SendDataPOSTService {
  
  constructor(private http: HttpClient) { }

  InjectionData_POST(data:{ [key: string]: any }): Observable<any> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const url='http://192.0.0.1:5012/rest/backendpoint-modulos-promocionales-api/v1.0/post'
    return this.http.post<any>(API_MAIN+API_POST, data, { headers });
  }
}
