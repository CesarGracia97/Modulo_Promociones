import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { TipoServicios } from '../../../../interfaces/planes/tiposervicios.interface';
import { TariffPlanes, TariffPlanesVariant } from '../../../../interfaces/planes/tariffplanes.interface';
import { Productos } from '../../../../interfaces/planes/productos.interface';
import { environment } from '../../../../../environments/environment';
import { UuidgeneratorService } from '../../../complements/uuidgenerator.service';

const MAIN_URL = environment.MAIN_URL;
const COMBOS = environment.API_GET_PLANES_COMB;
const CHANNEL = environment.CHANNEL;

@Injectable({
  providedIn: 'root'
})
export class CombosService {

  constructor(private http:HttpClient, private  uuidService: UuidgeneratorService) { }

  getCombosProductos_Router(): Observable<Productos[]> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: this.uuidService.generateUUID(),
      channel: CHANNEL,
      type: 'COMBO',
      stype: 'PRODUCTO_ROUTER'
    }
    return this.http.post<Productos[]>(MAIN_URL+COMBOS, body, { headers });
  }

  getCombosTipoServicios(Id_TPV: number):Observable<TipoServicios[]>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: this.uuidService.generateUUID(),
      channel: CHANNEL,
      type: 'COMBO',
      stype: 'TIPO_SERVICIO',
      _V1: Id_TPV.toString()
    }
    return this.http.post<TipoServicios[]>(MAIN_URL+COMBOS, body, { headers });
  }

  getCombosProductos(Id_TPV: number):Observable<Productos[]>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: this.uuidService.generateUUID(),
      channel: CHANNEL,
      type: 'COMBO',
      stype: 'PRODUCTO',
      _V1: Id_TPV.toString()
    }
    return this.http.post<Productos[]>(MAIN_URL+COMBOS, body, { headers });
  }

  getCombosPlan(SERVICIO: string):Observable<TariffPlanes[]>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: this.uuidService.generateUUID(),
      channel: CHANNEL,
      type: 'COMBO',
      stype: 'PLAN',
      _V1: SERVICIO.toString()
    }
    return this.http.post<TariffPlanes[]>(MAIN_URL+COMBOS, body, { headers });
  }

  getCombosPlanVariant(Id_Plan: number):Observable<TariffPlanesVariant[]>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: this.uuidService.generateUUID(),
      channel: CHANNEL,
      type: 'COMBO',
      stype: 'PLANVARIANT',
      _V1: Id_Plan.toString()
    }
    return this.http.post<TariffPlanesVariant[]>(MAIN_URL+COMBOS, body, { headers });
  }
}
