import { Injectable } from '@angular/core';
import { TariffPlan_X_TariffPlanVariant, TariffPlanes, TariffPlanesVariant } from '../../../interfaces/planes/tariffplanes.interface';
import { Observable } from 'rxjs';
import { HttpClient, HttpParams } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class TariffplanesService {

  private baseUrl ='http://127.0.0.1:5013/api/ra/plnplan_endpoint';

  constructor(private http:HttpClient) { }

  getTariffPlanesALL():Observable<TariffPlanes[]>{
    let params = new HttpParams().set('type', 'ALL_DATA')
    .set('stype', 'AD_TARIFFPLAN');
    return this.http.get<TariffPlanes[]>(this.baseUrl, { params: params });
  }

  getTariffPlanesVariantALL(servicio: string, tipo_servicio: string):Observable<TariffPlanesVariant[]>{
    let params = new HttpParams().set('type', 'ALL_DATA')
    .set('stype', 'AD_TARIFFPLANVARIANT')
    .set('SERVICIO', servicio)
    .set('TIPO_SERVICIO', tipo_servicio);
    return this.http.get<TariffPlanesVariant[]>(this.baseUrl, { params: params });
  }

  getTariffPlan_X_TariffPlanVariantALL():Observable<TariffPlan_X_TariffPlanVariant[]>{
    let params = new HttpParams().set('type', 'ALL_DATA')
    .set('stype', 'AD_TARIFFPLAN_TARIFFPLANVARIANT');
    return this.http.get<TariffPlan_X_TariffPlanVariant[]>(this.baseUrl, { params: params });
  }

  getTariffPlanesVariantXProducto_Adicional(SERVICIO: string): Observable <TariffPlanesVariant[]> {
    let params = new HttpParams().set('type', 'ALL_DATA')
    .set('stype', 'AD_TARIFFPLANVARIANT_PRODUCTO_ADICIONAL')
    .set('SERVICIO', SERVICIO);
    return this.http.get<TariffPlanesVariant[]>(this.baseUrl, { params: params });
  }
}
