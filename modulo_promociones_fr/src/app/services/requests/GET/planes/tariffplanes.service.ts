import { Injectable } from '@angular/core';
import { TariffPlan_X_TariffPlanVariant, TariffPlanes, TariffPlanesVariant } from '../../../../interfaces/planes/tariffplanes.interface';
import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../../../environments/environment';

const MAIN_URL = environment.MAIN_URL;
const PLANES = environment.API_GET_PLANES_PLAN;

@Injectable({
  providedIn: 'root'
})
export class TariffplanesService {

  constructor(private http:HttpClient) { }

  getTariffPlanesALL():Observable<TariffPlanes[]>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: 'ihjqbhwbehbecbcehws',
      channel: 'web-modulos-promocionales',
      type: 'ALL_DATA',
      stype: 'AD_TARIFFPLAN'
    }
    return this.http.post<TariffPlanes[]>(MAIN_URL+PLANES, body, { headers });
  }

  getTariffPlan_X_TariffPlanVariantALL():Observable<TariffPlan_X_TariffPlanVariant[]>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: 'ihjqbhwbehbecbcehws',
      channel: 'web-modulos-promocionales',
      type: 'ALL_DATA',
      stype: 'AD_TARIFFPLAN_TARIFFPLANVARIANT'
    }
    return this.http.post<TariffPlan_X_TariffPlanVariant[]>(MAIN_URL+PLANES, body, { headers });
  }

  getTariffPlanesVariantXProducto_Adicional(SERVICIO: string): Observable <TariffPlanesVariant[]> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: 'ihjqbhwbehbecbcehws',
      channel: 'web-modulos-promocionales',
      type: 'ALL_DATA',
      stype: 'AD_TARIFFPLANVARIANT_PRODUCTO_ADICIONAL',
      SERVICIO: SERVICIO
    }
    return this.http.post<TariffPlanesVariant[]>(MAIN_URL+PLANES, body, { headers });
  }

  getTariffPlanesVariantALL(servicio: string, tipo_servicio: string):Observable<TariffPlanesVariant[]>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: 'ihjqbhwbehbecbcehws',
      channel: 'web-modulos-promocionales',
      type: 'ALL_DATA',
      stype: 'AD_TARIFFPLANVARIANT_PRODUCTO_ADICIONAL',
      SERVICIO: servicio,
      TIPO_SERVICIO: tipo_servicio
    }
    return this.http.post<TariffPlanesVariant[]>(MAIN_URL+PLANES, body, { headers });
  }
}
