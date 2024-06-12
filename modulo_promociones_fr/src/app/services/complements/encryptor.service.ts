import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class EncryptorService {

  constructor() { }

  encryptData(data: Record<string, any>): string {
    const secretKey = 'your-secret-key'; // Define tu clave secreta para encriptación
    const encrypted = CryptoJS.AES.encrypt(JSON.stringify(data), secretKey).toString();
    return encrypted;
  }
}
