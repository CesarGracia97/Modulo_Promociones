import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, Observable, tap } from 'rxjs';
import { Provincias } from '../interfaces/provincias.interface';

@Injectable({
  providedIn: 'root'
})

export class ProvinciasService {

  private baseUrl ='https://localhost:5001/api/ms/peticionPlaces';
  private _infoProvincias:string[]=[];

  get infoProvincias():string[]{
    return [...this._infoProvincias];
  }

  constructor(private http:HttpClient) { }
  
  getProvincias(): Observable<Provincias[]> {
    const url = `${this.baseUrl}?type=ALL_PROVS`;

    return this.http.get<Provincias[]>(url)
      .pipe(
        tap((response: any) => {
          if (response && response.status === 200 && response.data && response.data.length > 0) {
            console.log('La solicitud se ejecutó exitosamente.');
          }
        }),
        catchError(this.handleError)
      );
  }

  private handleError(error: any): Observable<never> {
    console.error('Hubo un error al obtener las provincias:', error);
    throw error;
  }
}
