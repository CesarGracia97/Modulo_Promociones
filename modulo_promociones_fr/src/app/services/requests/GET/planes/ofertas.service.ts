import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Ofertas } from '../../../../interfaces/planes/ofertas.interface';
import { Observable } from 'rxjs';
import { environment } from '../../../../../environments/environment';
import { UuidgeneratorService } from '../../../complements/uuidgenerator.service';

const MAIN_URL = environment.MAIN_URL;
const OFERTA = environment.API_GET_PLANES_OFER;
const CHANNEL = environment.CHANNEL;

@Injectable({
  providedIn: 'root'
})
export class OfertasService {

  constructor(private http:HttpClient, private  uuidService: UuidgeneratorService) { }

  getOfertasALL():Observable<Ofertas[]> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: this.uuidService.generateUUID(),
      channel: CHANNEL,
      type: 'ALL_DATA',
      stype: 'OFER'
    }
    return this.http.post<Ofertas[]>(MAIN_URL+OFERTA, body, { headers });
  }
}
