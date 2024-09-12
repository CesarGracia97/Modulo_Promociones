import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Ciudades } from '../../../../interfaces/places/ciudad.interface';
import { environment } from '../../../../../environments/environment';

const API_MAIN = environment.MAIN_URL;
const CITY = environment.API_GET_PLACES_CITY;

@Injectable({
  providedIn: 'root'
})
export class CiudadService {

  constructor(private http:HttpClient) { }

  getCiudadesALL(): Observable<Ciudades[]>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: 'ihjqbhwbehbecbcehws',
      channel: 'web-modulos-promocionales',
      type: 'ALL_CITIES',
    }
    return this.http.post<Ciudades[]>(API_MAIN+CITY, body, { headers });
  }

  getCiudadesESP(id_Prov:number):Observable<Ciudades[]>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: 'ihjqbhwbehbecbcehws',
      channel: 'web-modulos-promocionales',
      type: 'CIUDADES_ESPECIFICASxPROV',
      id_Prov: id_Prov
    }
    return this.http.post<Ciudades[]>(API_MAIN+CITY, body, { headers });
  }

  getCiudadesALLXTariffplanVariant(tariffplanvariant: number): Observable <Ciudades[]> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: 'ihjqbhwbehbecbcehws',
      channel: 'web-modulos-promocionales',
      type: 'CIUDADES_ESPECIFICASxTFV',
      TARIFFPLANVARIANT: tariffplanvariant
    }
    return this.http.post<Ciudades[]>(API_MAIN+CITY, body, { headers });
  }

  getCiudadesALLXTariffplanVariantXProductoId(tariffplanvariant: number, ProductoId: number): Observable <Ciudades[]> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: 'ihjqbhwbehbecbcehws',
      channel: 'web-modulos-promocionales',
      type: 'CIUDADES_ESPECIFICASxTFVxPROD',
      TARIFFPLANVARIANT: tariffplanvariant,
      PRODUCTOID: ProductoId
    }
    return this.http.post<Ciudades[]>(API_MAIN+CITY, body, { headers });
  }

  getCiudadesXTariffplanVariant(id_Prov:number, tariffplanvariant: number):Observable<Ciudades[]>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: 'ihjqbhwbehbecbcehws',
      channel: 'web-modulos-promocionales',
      type: 'CIUDADES_ESPECIFICASxPROVxTFV',
      TARIFFPLANVARIANT: tariffplanvariant,
      id_Prov: id_Prov
    }
    return this.http.post<Ciudades[]>(API_MAIN+CITY, body, { headers });
  }

  getCiudadesMasivasXTariffplanVariant(id_Prov: number[], tariffplanvariant: number): Observable <Ciudades[]> {
    const a_idProv = id_Prov.join(',');
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: 'ihjqbhwbehbecbcehws',
      channel: 'web-modulos-promocionales',
      type: 'CIUDADES_M_ESPECIFICASxPROVxTFV',
      TARIFFPLANVARIANT: tariffplanvariant,
      id_Provs: a_idProv
    }
    return this.http.post<Ciudades[]>(API_MAIN+CITY, body, { headers });
  }
}
