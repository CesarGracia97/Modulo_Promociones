import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Provincias } from '../interfaces/provincias.interface';

@Injectable({
  providedIn: 'root'
})

export class ProvinciasService {

  private baseUrl ='http://127.0.0.1:5012/api/ra/plcprov_endpoint';
  private _infoProvincias:string[]=[];

  get infoProvincias():string[]{
    return [...this._infoProvincias];
  }

  constructor(private http:HttpClient) { }
  
  getProvincias(): Observable<Provincias[]> {
    // Construir los parámetros de consulta
    let params = new HttpParams().set('type', 'ALL_PROVS');
    
    // Realizar la solicitud GET con los parámetros de consulta
    return this.http.get<Provincias[]>(this.baseUrl, { params: params });
  }
}
