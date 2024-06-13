import { Injectable } from '@angular/core';
import { SendDataPOSTService } from '../requests/POST/send-data-POST.service';
import { RequiredTokenService } from '../requests/POST/required-token.service';
import { Itoken } from '../../interfaces/Login/LoginInterface';

@Injectable({
  providedIn: 'root'
})
export class InjectionDataService {
  private token: Itoken[] = []

  constructor(private send: SendDataPOSTService, private gtoken: RequiredTokenService) { }

  injectionData(_diccionario: Record<string, any>){
    let tkn = '';
    this.gtoken.getToken().subscribe((response: any) => {
      if(response){
        console.log(response )
          tkn = response
        console.log("Token contenido", tkn);
      }
    });
    this.send.InjectionData_POST(_diccionario, tkn);
  }

  private genToken(){
    this.gtoken.getToken().subscribe((response: any) => {
      if(response){
        console.log("Se recibio el Token")
        console.log(response);
        if(response && response.IT){
          this.token = response.IT.map((tk: Itoken) => tk.code)
        }
      }
    });
  }
}
