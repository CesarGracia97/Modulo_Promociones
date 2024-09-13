import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Upgrade } from '../../../../interfaces/DataPromocional/upgrade.interface';
import { Observable } from 'rxjs/internal/Observable';
import { environment } from '../../../../../environments/environment';
import { UuidgeneratorService } from '../../../complements/uuidgenerator.service';

const MAIN_URL = environment.MAIN_URL;
const UPGRADE = environment.API_GET_UPGRADE;
const CHANNEL = environment.CHANNEL;

@Injectable({
  providedIn: 'root'
})
export class UpgradeService {

  constructor(private http:HttpClient, private  uuidService: UuidgeneratorService) { }

  getUpgrade(Tariffplan: number, TFPV: number):Observable<Upgrade[]>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: this.uuidService.generateUUID(),
      channel: CHANNEL,
      type: 'UPGRADE',
      TARIFFPLANVARIANT: TFPV,
      TARIFFPLAN: Tariffplan
    }
    return this.http.post<Upgrade[]>(MAIN_URL+UPGRADE, body, { headers });
  }
}
