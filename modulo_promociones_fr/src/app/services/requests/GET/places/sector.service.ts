import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Sectores } from '../../../../interfaces/places/sector.interface';
import { environment } from '../../../../../environments/environment';

const API_MAIN = environment.MAIN_URL;
const SECT = environment.API_GET_PLACES_SECT;

@Injectable({
  providedIn: 'root'
})
export class SectorService {

  constructor(private http:HttpClient) { }

  getSectoresALL():Observable<Sectores[]>{
    let params = new HttpParams().set('type', 'ALL_SECTORS');
    return this.http.get<Sectores[]>(API_MAIN+SECT, { params: params });
  }

  getSectoresESP(id_City: number):Observable<Sectores[]>{
    let params = new HttpParams().set('type', 'SECTORES_ESPECIFICOSxCITY')
    .set('id_City', id_City.toString());
    return this.http.get<Sectores[]>(API_MAIN+SECT, { params: params });
  }

  getSectoresALLXTariffplanVariant(tariffplanvariant: number): Observable<Sectores[]> {
    let params = new HttpParams().set('type', 'SECTORES_ESPECIFICOSxTFV')
    .set('TARIFFPLANVARIANT', tariffplanvariant);
    return this.http.get<Sectores[]>(API_MAIN+SECT, { params: params });
  }

  getSectoresXTariffplanVariant(id_City: number, tariffplanvariant: number): Observable<Sectores[]> {
    let params = new HttpParams().set('type', 'SECTORES_ESPECIFICOSxCITYxTFV')
    .set('id_City', id_City)
    .set('TARIFFPLANVARIANT', tariffplanvariant);
    return this.http.get<Sectores[]>(API_MAIN+SECT, { params: params });
  }

  getSectoresMasivosXTariffplanVariant(id_Cities: number[], tariffplanvariant: number): Observable<Sectores[]> {
    const a_idCities = id_Cities.join(',');
    let params = new HttpParams().set('type', 'SECTORES_M__ESPECIFICOSxCITYxTFV')
    .set('id_Cities', a_idCities)
    .set('TARIFFPLANVARIANT', tariffplanvariant.toString());
    return this.http.get<Sectores[]>(API_MAIN+SECT, { params: params });
  }

  getSectoresMasivosXTariffplanVariantXProductoId(id_Cities: number[], tariffplanvariant: number, ProductoId: number): Observable<Sectores[]> {
    const a_idCities = id_Cities.join(',');
    let params = new HttpParams().set('type', 'SECTORES_M_ESPECIFICOSxCITYxTFVxPROD')
    .set('id_Cities', a_idCities)
    .set('TARIFFPLANVARIANT', tariffplanvariant.toString())
    .set('PRODUCTOID', ProductoId.toString());
    return this.http.get<Sectores[]>(API_MAIN+SECT, { params: params });
  }
}