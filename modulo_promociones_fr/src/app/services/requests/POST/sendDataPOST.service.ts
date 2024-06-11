import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import * as cryptoJS from 'crypto-js';

const API_MAIN = environment.MAIN_URL;

@Injectable({
  providedIn: 'root'
})
export class SendDataPOSTService {
  
  constructor(private http: HttpClient) { }

  sendData(data: Record<string, any>): Observable<any> {
    const encryptedData = this.encryptData(data); // Encriptar datos
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN' // Si usas token de acceso, reemplaza YOUR_ACCESS_TOKEN
      })
    };
    return this.http.post(API_MAIN, { data: encryptedData }, httpOptions);
  }

  private encryptData(data: Record<string, any>): string {
    const secretKey = 'your-secret-key'; // Define tu clave secreta para encriptación
    const encrypted = CryptoJS.AES.encrypt(JSON.stringify(data), secretKey).toString();
    return encrypted;
  }

  /*

  createHeader(token: string) {
    let headers: HttpHeaders;
    headers = new HttpHeaders()
    .set('Content-Type', 'application/json; charset=utf-8')
    .set('Accept', 'application/json; charset=utf-8')
    .set('Access-Control-Allow-Origin', '*')
    .set('Authorization', 'Bearer '+token);
    return headers;
  }

  getToken(){
    const headers = this.createHeader('token');
    const body = {
      channel: "string",
      key: KEY_TOKEN,
      realm: "realm-bankdebits",
      type: "Basic"
    }
    return this.http.post<Itoken>(API_MAIN + API_TOKEN, body, { headers });
  }

  postLogin(user: string, pass: string, token: string) {
    const headers = this.createHeader(token);
    const body = {
      channel: CHANNEL,
      externalTransactionId: IdTrasaction,
      username: user,
      password: pass
    }
    return this.http.post<any>(API_MAIN+API_LOGIN, body, { headers });
  }

  */
}
