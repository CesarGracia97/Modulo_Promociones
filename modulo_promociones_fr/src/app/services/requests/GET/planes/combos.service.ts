import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { TipoServicios } from '../../../../interfaces/planes/tiposervicios.interface';
import { TariffPlanes, TariffPlanesVariant } from '../../../../interfaces/planes/tariffplanes.interface';
import { Productos } from '../../../../interfaces/planes/productos.interface';
import { environment } from '../../../../../environments/environment';

const MAIN_URL = environment.MAIN_URL;
const API_GET_PLANES = environment.API_GET_PLANES;
const COMBOS = environment.API_GET_PLANES_COMB;

@Injectable({
  providedIn: 'root'
})
export class CombosService {

  constructor(private http:HttpClient) { }

  getCombosPlan(SERVICIO: string):Observable<TariffPlanes[]>{
    let params = new HttpParams()
    .set('type', 'COMBO')
    .set('stype', 'PLAN')
    .set('_V1', SERVICIO.toString());
    return this.http.get<TariffPlanes[]>(MAIN_URL+API_GET_PLANES+COMBOS, { params: params });
  }

  getCombosPlanVariant(Id_Plan: number):Observable<TariffPlanesVariant[]>{
    let params = new HttpParams()
    .set('type', 'COMBO')
    .set('stype', 'PLANVARIANT')
    .set('_V1', Id_Plan.toString());
    return this.http.get<TariffPlanesVariant[]>(MAIN_URL+API_GET_PLANES+COMBOS, { params: params });
  }

  getCombosProductos(Id_TPV: number):Observable<Productos[]>{
    let params = new HttpParams()
    .set('type', 'COMBO')
    .set('stype', 'PRODUCTO')
    .set('_V1', Id_TPV.toString());
    return this.http.get<Productos[]>(MAIN_URL+API_GET_PLANES+COMBOS, { params: params });
  }

  getCombosProductos_Router(): Observable<Productos[]> {
    let params = new HttpParams()
    .set('type', 'COMBO')
    .set('stype', 'PRODUCTO_ROUTER');
    return this.http.get<Productos[]>(MAIN_URL+API_GET_PLANES+COMBOS, { params: params });
  }

  getCombosTipoServicios(Id_TPV: number):Observable<TipoServicios[]>{
    let params = new HttpParams()
    .set('type', 'COMBO')
    .set('stype', 'TIPO_SERVICIO')
    .set('_V1', Id_TPV.toString());
    return this.http.get<TipoServicios[]>(MAIN_URL+API_GET_PLANES+COMBOS, { params: params });
  }
}
