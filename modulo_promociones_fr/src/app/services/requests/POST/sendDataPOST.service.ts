import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import * as cryptoJS from 'crypto-js';
import { Itoken } from '../../../interfaces/Login/LoginInterface';
import { response } from 'express';

const API_MAIN = environment.MAIN_URL;
const KEY_TOKEN = environment.KEY_TOKEN;
const API_TOKEN = environment.API_POST_TOKEN;

@Injectable({
  providedIn: 'root'
})
export class SendDataPOSTService {
  
  constructor(private http: HttpClient) { }

  createHeader(token: string) {
    let headers: HttpHeaders;
    headers = new HttpHeaders()
    .set('Content-Type', 'application/json; charset=utf-8')
    .set('Accept', 'application/json; charset=utf-8')
    .set('Access-Control-Allow-Origin', '*')
    .set('Authorization', 'Bearer '+token);
    return headers;
  }

  getToken(): Observable<Itoken> {
    const headers = this.createHeader('token');
    const body = {
      channel: "string",
      key: KEY_TOKEN,
      realm: "realm-modulos_promocionales",
      type: "Basic"
    }
    return this.http.post<Itoken>(API_MAIN + API_TOKEN, body, { headers });
  }

  sendData(_diccionario: Record<string, any>, token: string){
    const headers = this.createHeader(token)
    const encryptedData = this.encryptData(_diccionario); // Encriptar datos

    return this.http.post(API_MAIN, { data: encryptedData }, {headers});
  }

  private encryptData(data: Record<string, any>): string {
    const secretKey = 'your-secret-key'; // Define tu clave secreta para encriptación
    const encrypted = CryptoJS.AES.encrypt(JSON.stringify(data), secretKey).toString();
    return encrypted;
  }
}
