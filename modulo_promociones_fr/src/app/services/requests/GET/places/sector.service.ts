import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Sectores } from '../../../../interfaces/places/sector.interface';
import { environment } from '../../../../../environments/environment';

const API_MAIN = environment.MAIN_URL;
const GET_PLACES = environment.API_GET_PLACES;
const SECT = environment.API_GET_PLACES_SECT;
const MASV = environment.API_GET_PLACES_MASIVE;

@Injectable({
  providedIn: 'root'
})
export class SectorService {

  constructor(private http:HttpClient) { }

  getSectoresALL():Observable<Sectores[]>{
    let params = new HttpParams().set('type', 'ALL_SECTORS');
    return this.http.get<Sectores[]>(API_MAIN+GET_PLACES+SECT, { params: params });
  }

  getSectoresESP(id_City: number):Observable<Sectores[]>{
    let params = new HttpParams().set('type', 'SECTORES_ESPECIFICOSxCITY')
    .set('id_City', id_City.toString());
    return this.http.get<Sectores[]>(API_MAIN+GET_PLACES+SECT, { params: params });
  }

  getSectoresALLXTariffplanVariant(tariffplanvariant: number): Observable<Sectores[]> {
    let params = new HttpParams().set('type', 'SECTORES_ESPECIFICOSxTFV')
    .set('TARIFFPLANVARIANT', tariffplanvariant);
    return this.http.get<Sectores[]>(API_MAIN+GET_PLACES+SECT, { params: params });
  }

  getSectoresXTariffplanVariant(id_City: number, tariffplanvariant: number): Observable<Sectores[]> {
    let params = new HttpParams().set('type', 'SECTORES_ESPECIFICOSxCITYxTFV')
    .set('id_City', id_City)
    .set('TARIFFPLANVARIANT', tariffplanvariant);
    return this.http.get<Sectores[]>(API_MAIN+GET_PLACES+SECT, { params: params });
  }

  getSectoresMasivosXTariffplanVariant(id_Cities: number[], tariffplanvariant: number): Observable<Sectores[]> {
    const a_idCities = id_Cities.join(',');
    let params = new HttpParams().set('type', 'SECTORES_ESPECIFICOSxCITYxTFV')
    .set('id_Cities', a_idCities)
    .set('TARIFFPLANVARIANT', tariffplanvariant.toString());
    return this.http.get<Sectores[]>(API_MAIN+GET_PLACES+MASV, { params: params });
  }

  getSectoresMasivosXTariffplanVariantXProductoId(id_Cities: number[], tariffplanvariant: number, ProductoId: number): Observable<Sectores[]> {
    const a_idCities = id_Cities.join(',');
    let params = new HttpParams().set('type', 'SECTORES_ESPECIFICOSxCITYxTFVxPROD')
    .set('id_Cities', a_idCities)
    .set('TARIFFPLANVARIANT', tariffplanvariant.toString())
    .set('PRODUCTOID', ProductoId.toString());
    return this.http.get<Sectores[]>(API_MAIN+GET_PLACES+MASV, { params: params });
  }
}