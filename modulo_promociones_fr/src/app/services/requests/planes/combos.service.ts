import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { TipoServicios } from '../../../interfaces/planes/tiposervicios.interface';
import { TariffPlanes, TariffPlanesVariant } from '../../../interfaces/planes/tariffplanes.interface';
import { Provincias } from '../../../interfaces/places/provincias.interface';
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

  getCombosProvincia(SERVICIO: string, TIPO_SERVICIOS:string, TECNOLOGIA: string, TARIFFPLANIDVARIANTID: number):Observable<Provincias[]>{
    let params = new HttpParams()
    .set('type', 'COMBO')
    .set('stype', 'PROVINCIA')
    .set('_V1', SERVICIO.toString())
    .set('_V2', TIPO_SERVICIOS.toString())
    .set('_V3', TECNOLOGIA.toString())
    .set('_V4', TARIFFPLANIDVARIANTID.toString());
    return this.http.get<Provincias[]>(this.baseUrl, { params: params });
  }

  getCombosCiudad(SERVICIO: string, TIPO_SERVICIOS:string, TECNOLOGIA: string, TARIFFPLANIDVARIANTID: number, PROVINCIAID:number):Observable<C_Ciudades[]>{
    let params = new HttpParams()
    .set('type', 'COMBO')
    .set('stype', 'CIUDAD')
    .set('_V1', SERVICIO.toString())
    .set('_V2', TIPO_SERVICIOS.toString())
    .set('_V3', TECNOLOGIA.toString())
    .set('_V4', TARIFFPLANIDVARIANTID.toString())
    .set('_V5', PROVINCIAID.toString());
    return this.http.get<C_Ciudades[]>(this.baseUrl, { params: params });
  }

  getCombosSectores(SERVICIO: string, TIPO_SERVICIOS:string, TECNOLOGIA: string, TARIFFPLANIDVARIANTID: number, PROVINCIAID:number, CIUDADID:number):Observable<C_Sectores[]>{
    let params = new HttpParams()
    .set('type', 'COMBO')
    .set('stype', 'SECTOR')
    .set('_V1', SERVICIO.toString())
    .set('_V2', TIPO_SERVICIOS.toString())
    .set('_V3', TECNOLOGIA.toString())
    .set('_V4', TARIFFPLANIDVARIANTID.toString())
    .set('_V5', PROVINCIAID.toString())
    .set('_V6', CIUDADID.toString());
    return this.http.get<C_Sectores[]>(this.baseUrl, { params: params });
  }
}
