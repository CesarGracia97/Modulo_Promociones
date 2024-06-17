import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Ciudades } from '../../../../interfaces/places/ciudad.interface';
import { environment } from '../../../../../environments/environment';

const API_MAIN = environment.MAIN_URL;
const GET_PLACES = environment.API_GET_PLACES;
const CITY = environment.API_GET_PLACES_CITY;
const MASV = environment.API_GET_PLACES_MASIVE;

@Injectable({
  providedIn: 'root'
})
export class CiudadService {

  constructor(private http:HttpClient) { }

  getCiudadesALL(): Observable<Ciudades[]>{
    let params = new HttpParams().set('type', 'ALL_CITIES');
    return this.http.get<Ciudades[]>(API_MAIN+GET_PLACES+CITY, { params: params });
  }

  getCiudadesESP(id_Prov:number):Observable<Ciudades[]>{
    let params = new HttpParams().set('type', 'CIUDADES_ESPECIFICASxPROV')
    .set('id_Prov', id_Prov.toString());
    return this.http.get<Ciudades[]>(API_MAIN+GET_PLACES+CITY, { params: params });
  }

  getCiudadesALLXTariffplanVariant(tariffplanvariant: number): Observable <Ciudades[]> {
    let params = new HttpParams().set('type', 'CIUDADES_ESPECIFICASxTFV')
    .set('TARIFFPLANVARIANT', tariffplanvariant.toString());
    return this.http.get<Ciudades[]>(API_MAIN+GET_PLACES+CITY, { params: params });
  }

  getCiudadesALLXTariffplanVariantXProductoId(tariffplanvariant: number, ProductoId: number): Observable <Ciudades[]> {
    let params = new HttpParams().set('type', 'CIUDADES_ESPECIFICASxTFVxPROD')
    .set('TARIFFPLANVARIANT', tariffplanvariant.toString())
    .set('PRODUCTOID', ProductoId.toString());
    return this.http.get<Ciudades[]>(API_MAIN+GET_PLACES+CITY, { params: params });
  }

  getCiudadesXTariffplanVariant(id_Prov:number, tariffplanvariant: number):Observable<Ciudades[]>{
    let params = new HttpParams().set('type', 'CIUDADES_ESPECIFICASxPROVxTFV')
    .set('id_Prov', id_Prov.toString())
    .set('TARIFFPLANVARIANT', tariffplanvariant);
    return this.http.get<Ciudades[]>(API_MAIN+GET_PLACES+CITY, { params: params });
  }

  getCiudadesMasivasXTariffplanVariant(id_Prov: number[], tariffplanvariant: number): Observable <Ciudades[]> {
    const a_idProv = id_Prov.join(',');
    let params = new HttpParams().set('type', 'CIUDADES_ESPECIFICASxPROVxTFV')
    .set('id_Provs', a_idProv)
    .set('TARIFFPLANVARIANT', tariffplanvariant.toString());
    return this.http.get<Ciudades[]>(API_MAIN+GET_PLACES+MASV, { params: params });
  }
}
