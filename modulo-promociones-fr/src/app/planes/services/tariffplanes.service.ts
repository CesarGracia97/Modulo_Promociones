import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { TariffPlan_X_TariffPlanVariant, TariffPlanes, TariffPlanesVariant } from '../interfaces/tariffplanes.interface';

@Injectable({
  providedIn: 'root'
})
export class TariffplanesService {

  private baseUrl ='http://127.0.0.1:5012/api/ra/plnplan_endpoint';

  constructor(private http:HttpClient) { }

  getTariffPlanesALL():Observable<TariffPlanes[]>{
    let params = new HttpParams().set('type', 'ALL_DATA')
    .set('stype', 'PLAN').set('ttype', '1');
    return this.http.get<TariffPlanes[]>(this.baseUrl, { params: params });
  }

  getTariffPlanesVariantALL():Observable<TariffPlanesVariant[]>{
    let params = new HttpParams().set('type', 'ALL_DATA')
    .set('stype', 'PLAN').set('ttype', '2');
    return this.http.get<TariffPlanesVariant[]>(this.baseUrl, { params: params });
  }

  getTariffPlan_X_TariffPlanVariantALL():Observable<TariffPlan_X_TariffPlanVariant[]>{
    let params = new HttpParams().set('type', 'ALL_DATA')
    .set('stype', 'PLAN').set('ttype', '3');
    return this.http.get<TariffPlan_X_TariffPlanVariant[]>(this.baseUrl, { params: params });
  }
}
