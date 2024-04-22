import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Sectores } from '../../interfaces/places/sector.interface';

@Injectable({
  providedIn: 'root'
})
export class SectorService {

  private baseUrl ='http://127.0.0.1:5012/api/ra/plcsector_endpoint';

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

  getSectoresXTecnologia(id_City: number, tecnologia: string):Observable<Sectores[]>{
    let params = new HttpParams().set('type', 'SECTOR_SPECIFIC')
    .set('id_City', id_City.toString())
    .set('TECNOLOGIA', tecnologia);
    return this.http.get<Sectores[]>(this.baseUrl, { params: params });
  }
}
