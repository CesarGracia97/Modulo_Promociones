import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { TipoServicios } from '../../../interfaces/planes/tiposervicios.interface';
import { TariffPlanes, TariffPlanesVariant } from '../../../interfaces/planes/tariffplanes.interface';
import { C_Ciudades, C_Sectores } from '../../../interfaces/planes/combos.interface';
import { Productos } from '../../../interfaces/planes/productos.interface';

@Injectable({
  providedIn: 'root'
})
export class CombosService {

  private baseUrl ='http://127.0.0.1:5013/api/ra/plncomb_endpoint';

  constructor(private http:HttpClient) { }

  getCombosPlan(SERVICIO: string):Observable<TariffPlanes[]>{
    let params = new HttpParams()
    .set('type', 'COMBO')
    .set('stype', 'COMBO_PLAN')
    .set('_V1', SERVICIO.toString());
    return this.http.get<TariffPlanes[]>(this.baseUrl, { params: params });
  }

  getCombosPlanVariant(Id_Plan: number):Observable<TariffPlanesVariant[]>{
    let params = new HttpParams()
    .set('type', 'COMBO')
    .set('stype', 'COMBO_PLANVARIANT')
    .set('_V1', Id_Plan.toString());
    return this.http.get<TariffPlanesVariant[]>(this.baseUrl, { params: params });
  }

  getCombosProductos(Id_TPV: number):Observable<Productos[]>{
    let params = new HttpParams()
    .set('type', 'COMBO')
    .set('stype', 'COMBO_PRODUCTO')
    .set('_V1', Id_TPV.toString());
    return this.http.get<Productos[]>(this.baseUrl, { params: params });
  }

  getCombosTipoServicios(Id_TPV: number):Observable<TipoServicios[]>{
    let params = new HttpParams()
    .set('type', 'COMBO')
    .set('stype', 'COMBO_TIPO_SERVICIO')
    .set('_V1', Id_TPV.toString());
    return this.http.get<TipoServicios[]>(this.baseUrl, { params: params });
  }
}
