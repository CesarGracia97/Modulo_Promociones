import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CommunicationVisibleService {
  //Variables de Comunicacion visual entre componentes de Table Query
  private visibleItemPrincipal_Subject = new Subject<string>();
  visbleItemP$ = this.visibleItemPrincipal_Subject.asObservable(); //de Botones a Contenedor Prima
  private visibleItemSecundario_Subject = new Subject<string>();
  visbleItemS$ = this.visibleItemSecundario_Subject.asObservable(); //de Botones a Elementos de Contenedor Prima
  private visibleItemTercero_Subject = new Subject<string>();
  visibleItemT$ = this.visibleItemTercero_Subject.asObservable(); // entre Componentes de un mismo Contenedor
  
  constructor() { }
  
  visiblePrincipalComponent(value: string){
    this.visibleItemPrincipal_Subject .next(value);
  }

  visibleSecundarioComponent(value:string){
    this.visibleItemSecundario_Subject.next(value);
  }

  visibleTerceriaComponent(id: string ){
    this.visibleItemTercero_Subject.next(id);
  }
}
