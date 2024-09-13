import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Servicios } from '../../../../interfaces/planes/servicios.interface';
import { environment } from '../../../../../environments/environment';
import { UuidgeneratorService } from '../../../complements/uuidgenerator.service';

const MAIN_URL = environment.MAIN_URL;
const SERVIC = environment.API_GET_PLANES_SERV;
const CHANNEL = environment.CHANNEL;

@Injectable({
  providedIn: 'root'
})
export class ServiciosService {

  constructor(private http:HttpClient, private  uuidService: UuidgeneratorService) { }

  getServiciosALL():Observable<Servicios[]>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: this.uuidService.generateUUID(),
      channel: CHANNEL,
      type: 'ALL_DATA',
      stype: 'SERV'
    };
    return this.http.post<Servicios[]>(MAIN_URL+SERVIC, body, { headers });
  }
}
