import { Injectable } from '@angular/core';
import { EncryptorService } from '../complements/encryptor.service';
import { SendDataPOSTService } from '../requests/POST/send-data-POST.service';
import { RequiredTokenService } from '../requests/POST/required-token.service';
import { Itoken } from '../../interfaces/Login/LoginInterface';

@Injectable({
  providedIn: 'root'
})
export class InjectionDataService {
  token: Itoken[] = []

  constructor(private Encryptor: EncryptorService, private send: SendDataPOSTService, private gtoken: RequiredTokenService) { }

  injectionData(_diccionario: Record<string, any>){
    const _diccionarioEncrpt = this.Encryptor.encryptData(_diccionario);
    this.gtoken.getToken().subscribe((response: any) => {
      if(response && response.IT){
        this.token = response.IT.map((tk: Itoken) => tk.code)
      }
    });
    this.send.InjectionData_POST({ data: _diccionarioEncrpt }, this.token[0].code);
  }
}
