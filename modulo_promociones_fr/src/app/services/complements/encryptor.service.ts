import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';

const A = environment.KEY;

@Injectable({
  providedIn: 'root'
})
export class EncryptorService {

  constructor() { }

  /*encryptData(data: Record<string, any>): string {
    const secretKey = A; // Define tu clave secreta para encriptación
    const encrypted = CryptoJS.AES.encrypt(JSON.stringify(data), secretKey).toString();
    return encrypted;
  }*/
}
