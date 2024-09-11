import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Upgrade } from '../../../../interfaces/DataPromocional/upgrade.interface';
import { Observable } from 'rxjs/internal/Observable';
import { environment } from '../../../../../environments/environment';

const MAIN_URL = environment.MAIN_URL;
const UPGRADE = environment.API_GET_UPGRADE;

@Injectable({
  providedIn: 'root'
})
export class UpgradeService {

  constructor(private http:HttpClient) { }

  getUpgrade(Tariffplan: number, TFPV: number):Observable<Upgrade[]>{
    let params = new HttpParams().set('type', 'UPGRADE')
    .set('TARIFFPLAN', Tariffplan.toString())
    .set('TARIFFPLANVARIANT', TFPV.toString());
    return this.http.get<Upgrade[]>(MAIN_URL+UPGRADE, { params: params });
  }
}
