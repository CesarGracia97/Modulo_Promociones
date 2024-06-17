import { Injectable } from '@angular/core';
import { SendDataPOSTService } from '../requests/POST/send-data-POST.service';
import { RequiredTokenService } from '../requests/POST/required-token.service';

@Injectable({
  providedIn: 'root'
})
export class InjectionDataService {

  constructor(private send: SendDataPOSTService, private gtoken: RequiredTokenService) { }

  injectionData(_diccionario: Record<string, any>){
    this.send.InjectionData_POST(_diccionario);
  }
}
