import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Upgrade } from '../../../interfaces/DataPromocional/upgrade.interface';
import { Observable } from 'rxjs/internal/Observable';

@Injectable({
  providedIn: 'root'
})
export class UpgradeService {

  private baseUrl ='';

  constructor(private http:HttpClient) { }

  getUpgrade(TFPV: number):Observable<Upgrade[]>{
    let params = new HttpParams().set('type', 'UPGRADE')
                                  .set('TFPV', TFPV.toString());
    return this.http.get<Upgrade[]>(this.baseUrl, { params: params });
  }
}
