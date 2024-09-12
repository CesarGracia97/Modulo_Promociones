import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Provincias } from '../../../../interfaces/places/provincias.interface';
import { environment } from '../../../../../environments/environment';

const API_MAIN = environment.MAIN_URL;
const PROV = environment.API_GET_PLACES_PROV;

@Injectable({
  providedIn: 'root'
})
export class ProvinciasService {

  constructor(private http:HttpClient) { }
  
  getProvincias(): Observable<Provincias[]> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: 'ihjqbhwbehbecbcehws',
      channel: 'web-modulos-promocionales',
      type: 'ALL_PROV'
    }
    return this.http.post<Provincias[]>(API_MAIN+PROV, body, { headers });
  }

  getProvinciasXTariffplanVariant(tariffplanvariant: number):Observable<Provincias[]>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: 'ihjqbhwbehbecbcehws',
      channel: 'web-modulos-promocionales',
      type: 'PROVINCIAS_ESPECIFICASxTFV',
      TARIFFPLANVARIANT: tariffplanvariant
    }
    return this.http.post<Provincias[]>(API_MAIN+PROV, body, { headers });
  }
}
