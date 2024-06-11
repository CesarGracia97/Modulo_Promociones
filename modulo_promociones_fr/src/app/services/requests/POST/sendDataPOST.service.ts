import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import * as cryptoJS from 'crypto-js';

const API_MAIN = environment.MAIN_URL;
const API_POST_DATA = environment.API_POST_DATA;

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
    
    return this.http.post(this.API_MAIN, { data: encryptedData }, httpOptions);
  }

  private encryptData(data: Record<string, any>): string {
    const secretKey = 'your-secret-key'; // Define tu clave secreta para encriptación
    const encrypted = CryptoJS.AES.encrypt(JSON.stringify(data), secretKey).toString();
    return encrypted;
  }

  private getToken(): string {
    // Suponiendo que el token está almacenado en localStorage
    // Puedes ajustar esto según cómo obtengas el token en tu aplicación
    return localStorage.getItem('access_token') || '';
  }
}