import { Injectable } from '@angular/core';
import { TariffPlan_X_TariffPlanVariant, TariffPlanes, TariffPlanesVariant } from '../../../../interfaces/planes/tariffplanes.interface';
import { Observable } from 'rxjs';
import { HttpClient, HttpParams } from '@angular/common/http';
import { environment } from '../../../../../environments/environment';

const MAIN_URL = environment.MAIN_URL;
const API_GET_PLANES = environment.API_GET_PLANES;
const PLANES = environment.API_GET_PLANES_PLAN;

@Injectable({
  providedIn: 'root'
})
export class TariffplanesService {

  constructor(private http:HttpClient) { }

  getTariffPlanesALL():Observable<TariffPlanes[]>{
    let params = new HttpParams().set('type', 'ALL_DATA')
    .set('stype', 'AD_TARIFFPLAN');
    return this.http.get<TariffPlanes[]>(MAIN_URL+API_GET_PLANES+PLANES, { params: params });
  }

  getTariffPlan_X_TariffPlanVariantALL():Observable<TariffPlan_X_TariffPlanVariant[]>{
    let params = new HttpParams().set('type', 'ALL_DATA')
    .set('stype', 'AD_TARIFFPLAN_TARIFFPLANVARIANT');
    return this.http.get<TariffPlan_X_TariffPlanVariant[]>(MAIN_URL+API_GET_PLANES+PLANES, { params: params });
  }

  getTariffPlanesVariantXProducto_Adicional(SERVICIO: string): Observable <TariffPlanesVariant[]> {
    let params = new HttpParams().set('type', 'ALL_DATA')
    .set('stype', 'AD_TARIFFPLANVARIANT_PRODUCTO_ADICIONAL')
    .set('SERVICIO', SERVICIO);
    return this.http.get<TariffPlanesVariant[]>(MAIN_URL+API_GET_PLANES+PLANES, { params: params });
  }

  getTariffPlanesVariantALL(servicio: string, tipo_servicio: string):Observable<TariffPlanesVariant[]>{
    let params = new HttpParams().set('type', 'ALL_DATA')
    .set('stype', 'AD_TARIFFPLANVARIANT')
    .set('SERVICIO', servicio)
    .set('TIPO_SERVICIO', tipo_servicio);
    return this.http.get<TariffPlanesVariant[]>(MAIN_URL+API_GET_PLANES+PLANES, { params: params });
  }
}
