import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';
import { HeaderCreatorService } from '../../complements/header-creator.service';
import { Itoken } from '../../../interfaces/Login/LoginInterface';

const API_MAIN = environment.MAIN_URL;
const API_POST = environment. API_POST_DATA;

@Injectable({
  providedIn: 'root'
})
export class SendDataPOSTService {
  
  constructor(private http: HttpClient,  private headerCr: HeaderCreatorService) { }

  InjectionData_POST(_diccionarioEncrpt: { data: string }, token: string){
    const headers = this.headerCr.createHeader(token);
    return this.http.post(API_MAIN + API_POST, _diccionarioEncrpt, { headers });
  }
}
