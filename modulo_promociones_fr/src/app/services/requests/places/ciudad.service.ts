import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Ciudades } from '../../../interfaces/places/ciudad.interface';

@Injectable({
  providedIn: 'root'
})
export class CiudadService {

  private baseUrl ='http://127.0.0.1:5012/api/ra/plccity_endpoint';

  constructor(private http:HttpClient) { }

  getCiudadesALL(): Observable<Ciudades[]>{
    let params = new HttpParams().set('type', 'ALL_CITIES');
    return this.http.get<Ciudades[]>(this.baseUrl, { params: params });
  }

  getCiudadesESP(id_Prov:number):Observable<Ciudades[]>{
    let params = new HttpParams().set('type', 'CITY_SPECIFIC')
    .set('id_Prov', id_Prov.toString());
    return this.http.get<Ciudades[]>(this.baseUrl, { params: params });
  }

  getCiudadesXTecnologiaXTariffplanVariant(id_Prov:number, tecnologia: string, tariffplanvariant: number):Observable<Ciudades[]>{
    let params = new HttpParams().set('type', 'SPECIFIC_CITYXTT')
    .set('id_Prov', id_Prov.toString())
    .set('TECNOLOGIA', tecnologia)
    .set('TARIFFPLANVARIANT', tariffplanvariant);
    return this.http.get<Ciudades[]>(this.baseUrl, { params: params });
  }
}
