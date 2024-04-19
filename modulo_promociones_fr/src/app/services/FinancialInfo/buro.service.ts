import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/internal/Observable';
import { Buro } from '../../interfaces/buro.interface';

@Injectable({
  providedIn: 'root'
})
export class BuroService {

  private baseUrl ='http://127.0.0.1:5014/api/ra/fina_endpoint';

  constructor(private http:HttpClient) { }

  getTiposBuro():Observable<Buro[]>{
    let params = new HttpParams().set('type', 'ALL_TBUROS');
    return this.http.get<Buro[]>(this.baseUrl, { params: params });
  }
}
