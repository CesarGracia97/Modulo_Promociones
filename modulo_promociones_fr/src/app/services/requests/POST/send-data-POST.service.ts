import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../../../environments/environment';
import { Observable } from 'rxjs';
import { UuidgeneratorService } from '../../complements/uuidgenerator.service';

const API_MAIN = environment.MAIN_URL;
const MODULO_PROMOCIONAL = environment.API_POST_MODULO_PROMOCIONAL;
const CHANNEL = environment.CHANNEL;

@Injectable({
  providedIn: 'root'
})
export class SendDataPOSTService {
  
  constructor(private http: HttpClient, private  uuidService: UuidgeneratorService) { }

  InjectionData_POST(data:{ [key: string]: any }): Observable<any> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: this.uuidService.generateUUID(),
      channel: CHANNEL,
      diccionarioDatos : data 
    }
    return this.http.post<any>(API_MAIN+MODULO_PROMOCIONAL, body, { headers });
  }
}
