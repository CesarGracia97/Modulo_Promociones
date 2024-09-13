import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/internal/Observable';
import { Buro } from '../../../../interfaces/financial/buro.interface';
import { environment } from '../../../../../environments/environment';
import { UuidgeneratorService } from '../../../complements/uuidgenerator.service';

const MAIN_URL = environment.MAIN_URL;
const CHANNEL = environment.CHANNEL;
const BURO = environment.API_GET_FINANCE_BURO 

@Injectable({
  providedIn: 'root'
})
export class BuroService {

  constructor(private http:HttpClient, private  uuidService: UuidgeneratorService) { }

  getTiposBuro():Observable<Buro[]>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: this.uuidService.generateUUID(),
      channel: CHANNEL,
      type: 'ALL_BURO'
    }
    return this.http.post<Buro[]>(MAIN_URL+BURO, body, { headers });
  }
}
