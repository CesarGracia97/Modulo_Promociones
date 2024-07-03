import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../../../environments/environment';

const API_MAIN = environment.MAIN_URL;
const API_POST = environment. API_POST_DATA;

@Injectable({
  providedIn: 'root'
})
export class SendDataPOSTService {
  
  constructor(private http: HttpClient) { }

  InjectionData_POST(data:{ [key: string]: any }){
    return this.http.post(API_MAIN + API_POST, data);
  }
}
