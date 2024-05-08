import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Sectores } from '../../../interfaces/places/sector.interface';

@Injectable({
  providedIn: 'root'
})
export class SectorService {

  private baseUrl ='http://127.0.0.1:5012/api/ra/plcsector_endpoint';
  private baseUrlIM = 'http://127.0.0.1:5012/api/ra/plcinfomasiva_endpoint';

  constructor(private http:HttpClient) { }

  getSectoresALL():Observable<Sectores[]>{
    let params = new HttpParams().set('type', 'ALL_SECTORS');
    return this.http.get<Sectores[]>(this.baseUrl, { params: params });
  }

  getSectoresESP(id_City: number):Observable<Sectores[]>{
    let params = new HttpParams().set('type', 'SECTOR_SPECIFIC')
    .set('id_City', id_City.toString());
    return this.http.get<Sectores[]>(this.baseUrl, { params: params });
  }

  getSectoresXTariffplanVariant(id_City: number,tariffplanvariant: number):Observable<Sectores[]>{
    let params = new HttpParams().set('type', 'SPECIFIC_SECTXTT')
                                  .set('id_City', id_City)
                                  .set('TARIFFPLANVARIANT', tariffplanvariant);
    return this.http.get<Sectores[]>(this.baseUrl, { params: params });
  }

  getSectoresMasivosXTariffplanVariant(id_Cities: number[], tariffplanvariant: number):Observable<Sectores[]>{
    const a_idCities = id_Cities.join(',');
    let params = new HttpParams().set('type', 'SECTMXTT')
                                .set('id_Cities', a_idCities)
                                .set('TARIFFPLANVARIANT', tariffplanvariant.toString());
    return this.http.get<Sectores[]>(this.baseUrlIM, { params: params });
  }
}