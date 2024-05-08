import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { TipoServicios } from '../../../interfaces/planes/tiposervicios.interface';
import { TariffPlanesVariant } from '../../../interfaces/planes/tariffplanes.interface';
import { Provincias } from '../../../interfaces/places/provincias.interface';
import { C_Ciudades, C_Sectores } from '../../../interfaces/planes/combos.interface';
import { Productos } from '../../../interfaces/planes/productos.interface';

@Injectable({
  providedIn: 'root'
})
export class CombosService {

  private baseUrl ='http://127.0.0.1:5013/api/ra/plncomb_endpoint';

  constructor(private http:HttpClient) { }

  getCombosTipoServicios(SERVICIO: string):Observable<TipoServicios[]>{
    let params = new HttpParams()
    .set('type', 'COMBO')
    .set('stype', 'TIPO_SERVICIOS')
    .set('_V1', SERVICIO.toString());
    return this.http.get<TipoServicios[]>(this.baseUrl, { params: params });
  }

  getCombosProductos(SERVICIO: string, TIPO_SERVICIOS:string):Observable<Productos[]>{
    let params = new HttpParams()
    .set('type', 'COMBO')
    .set('stype', 'PRODUCTOS')
    .set('_V1', SERVICIO.toString())
    .set('_V2', TIPO_SERVICIOS.toString());
    return this.http.get<Productos[]>(this.baseUrl, { params: params });
  }

  getCombosPlanes(SERVICIO: string, TIPO_SERVICIOS:string, PRODUCTID: number):Observable<TariffPlanesVariant[]>{
    let params = new HttpParams()
    .set('type', 'COMBO')
    .set('stype', 'PLANES')
    .set('_V1', SERVICIO.toString())
    .set('_V2', TIPO_SERVICIOS.toString())
    .set('_V3', PRODUCTID.toString());
    return this.http.get<TariffPlanesVariant[]>(this.baseUrl, { params: params });
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
