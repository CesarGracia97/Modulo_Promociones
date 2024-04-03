import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CommunicationService {

  private selectedButtonSubject = new Subject<string>();
  selectedButton$ = this.selectedButtonSubject.asObservable();

  constructor() {}

  sendSelectedButton(buttonId: string) {
    console.log("CommunicationService - Activo | Valor:", buttonId)
    this.selectedButtonSubject.next(buttonId);
  }

  sendDataHeaderTable(diccionario:{[key: string]: any}){
    const id = diccionario['id'];
    let _V1, _V2, _V3, _V4, _V5, _V6
    switch (id){
      case 'TISE':
        _V1 = diccionario['_V1'];
        break;
      case 'RED':
        _V1 = diccionario['_V1'];
        _V2 = diccionario['_V2'];
        break;
      case 'PLAN':
        _V1 = diccionario['_V1'];
        _V2 = diccionario['_V2'];
        _V3 = diccionario['_V3'];
        break;
      case 'PROV':
        _V1 = diccionario['_V1'];
        _V2 = diccionario['_V2'];
        _V3 = diccionario['_V3'];
        _V4 = diccionario['_V4'];
        break;
      case 'CITY':
        _V1 = diccionario['_V1'];
        _V2 = diccionario['_V2'];
        _V3 = diccionario['_V3'];
        _V4 = diccionario['_V4'];
        _V5 = diccionario['_V5'];
        break;
      case 'SECT':
        _V1 = diccionario['_V1'];
        _V2 = diccionario['_V2'];
        _V3 = diccionario['_V3'];
        _V4 = diccionario['_V4'];
        _V5 = diccionario['_V5'];
        _V6 = diccionario['_V6'];
        break;
      default:
        console.log("Combo no registrado contactase con soporte")
    }
  }
}
