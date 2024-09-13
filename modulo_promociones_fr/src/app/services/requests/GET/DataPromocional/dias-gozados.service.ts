import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { DiasGozados } from '../../../../interfaces/DataPromocional/dias-gozados.interface';
import { environment } from '../../../../../environments/environment';
import { UuidgeneratorService } from '../../../complements/uuidgenerator.service';

const MAIN_URL = environment.MAIN_URL;
const DIAS_GOZADOS = environment.API_GET_FINANCE_DIAS_GOZADOS;
const CHANNEL = environment.CHANNEL;

@Injectable({
  providedIn: 'root'
})
export class DiasGozadosService {

  constructor(private http:HttpClient, private  uuidService: UuidgeneratorService) { }

  getDiasGozados():Observable<DiasGozados[]>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: this.uuidService.generateUUID(),
      channel: CHANNEL,
      type: 'DIAS_GOZADOS'
    }
    return this.http.post<DiasGozados[]>(MAIN_URL+DIAS_GOZADOS, body, { headers });
  }

}
