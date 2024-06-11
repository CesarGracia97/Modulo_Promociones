import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Provincias } from '../../../../interfaces/places/provincias.interface';
import { environment } from '../../../../environments/environment';

const API_MAIN = environment.MAIN_URL;
const GET_PLACES = environment.API_GET_PLACES;
const PROV = environment.API_GET_PLACES_PROV;

@Injectable({
  providedIn: 'root'
})
export class ProvinciasService {

  constructor(private http:HttpClient) { }
  
  getProvincias(): Observable<Provincias[]> {
    // Construir los parámetros de consulta
    let params = new HttpParams().set('type', 'ALL_PROV');
    return this.http.get<Provincias[]>(API_MAIN+GET_PLACES+PROV, { params: params });
  }

  getProvinciasXTariffplanVariant(tariffplanvariant: number):Observable<Provincias[]>{
    let params = new HttpParams().set('type', 'PROVINCIAS_ESPECIFICASxTFV')
                                  .set('TARIFFPLANVARIANT', tariffplanvariant);
    return this.http.get<Provincias[]>(API_MAIN+GET_PLACES+PROV, { params: params });
  }
}
