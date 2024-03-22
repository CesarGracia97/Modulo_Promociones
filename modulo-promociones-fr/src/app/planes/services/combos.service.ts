import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { TipoServicios } from '../interfaces/tiposervicios.interface';
import { Tecnologias } from '../interfaces/tecnologias.interface';
import { TariffPlanesVariant } from '../interfaces/tariffplanes.interface';
import { Provincias } from '../../places/interfaces/provincias.interface';
import { C_Ciudades, C_Sectores } from '../interfaces/combos.interface';

@Injectable({
  providedIn: 'root'
})
export class CombosService {

  private baseUrl ='http://127.0.0.1:5012/api/ra/plncomb_endpoint';

  constructor(private http:HttpClient) { }

  getCombosTipoServicios(SERVICIO: string):Observable<TipoServicios[]>{
    let params = new HttpParams()
    .set('type', 'ALL_COMBO')
    .set('stype', 'TIPO_SERVICIOS')
    .set('_V1', SERVICIO.toString());
    return this.http.get<TipoServicios[]>(this.baseUrl, { params: params });
  }

  getCombosRedTecnologia(SERVICIO: string, TIPO_SERVICIOS:string):Observable<Tecnologias[]>{
    let params = new HttpParams()
    .set('type', 'ALL_COMBO')
    .set('stype', 'RED_TECNOLOGIA')
    .set('_V1', SERVICIO.toString())
    .set('_V2', TIPO_SERVICIOS.toString());
    return this.http.get<Tecnologias[]>(this.baseUrl, { params: params });
  }

  getCombosPlanes(SERVICIO: string, TIPO_SERVICIOS:string, TECNOLOGIA: string):Observable<TariffPlanesVariant[]>{
    let params = new HttpParams()
    .set('type', 'ALL_COMBO')
    .set('stype', 'PLANES')
    .set('_V1', SERVICIO.toString())
    .set('_V2', TIPO_SERVICIOS.toString())
    .set('_V3', TECNOLOGIA.toString());
    return this.http.get<TariffPlanesVariant[]>(this.baseUrl, { params: params });
  }

  getCombosProvincia(SERVICIO: string, TIPO_SERVICIOS:string, TECNOLOGIA: string, TARIFFPLANIDVARIANTID: number):Observable<Provincias[]>{
    let params = new HttpParams()
    .set('type', 'ALL_COMBO')
    .set('stype', 'PROVINCIA')
    .set('_V1', SERVICIO.toString())
    .set('_V2', TIPO_SERVICIOS.toString())
    .set('_V3', TECNOLOGIA.toString())
    .set('_V4', TARIFFPLANIDVARIANTID.toString());
    return this.http.get<Provincias[]>(this.baseUrl, { params: params });
  }

  getCombosCiudad(SERVICIO: string, TIPO_SERVICIOS:string, TECNOLOGIA: string, TARIFFPLANIDVARIANTID: number, PROVINCIAID:number):Observable<C_Ciudades[]>{
    let params = new HttpParams()
    .set('type', 'ALL_COMBO')
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
    .set('type', 'ALL_COMBO')
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
