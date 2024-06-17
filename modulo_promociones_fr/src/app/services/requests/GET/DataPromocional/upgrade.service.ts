import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Upgrade } from '../../../../interfaces/DataPromocional/upgrade.interface';
import { Observable } from 'rxjs/internal/Observable';
import { environment } from '../../../../../environments/environment';

const MAIN_URL = environment.MAIN_URL;
const API_GET_FINANCE = environment.API_GET_FINANCE;
const DataPromo = environment.API_GET_FINANCE_DTPR

@Injectable({
  providedIn: 'root'
})
export class UpgradeService {

  constructor(private http:HttpClient) { }

  getUpgrade(Tariffplan: number, TFPV: number):Observable<Upgrade[]>{
    let params = new HttpParams().set('type', 'UPGRADE')
    .set('TARIFFPLAN', Tariffplan.toString())
    .set('TARIFFPLANVARIANT', TFPV.toString());
    return this.http.get<Upgrade[]>(MAIN_URL+API_GET_FINANCE+DataPromo, { params: params });
  }
}
