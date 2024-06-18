import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataViewService {

  //Variables de Comunicacion visual entre componentes de Table Query
  private visibleItemPrincipal_Subject = new Subject<string>();
  visbleItemP$ = this.visibleItemPrincipal_Subject.asObservable(); //de Botones a Contenedor Prima
  private visibleItemSecundario_Subject = new Subject<string>();
  visbleItemS$ = this.visibleItemSecundario_Subject.asObservable(); //de Botones a Elementos de Contenedor Prima
  private visibleItemTercero_Subject = new Subject<string>();
  visibleItemT$ = this.visibleItemTercero_Subject.asObservable(); // entre Componentes de un mismo Contenedor

  private dIndex_Subject = new Subject<number>();
  dIndex$ = this.dIndex_Subject.asObservable();

  private dModalViewDP_Subject = new Subject<boolean>();
  dModalViewDP$ = this.dModalViewDP_Subject.asObservable();

  private dModalViewCS_Subject = new Subject<boolean>();
  dModalViewCS$ = this.dModalViewCS_Subject.asObservable();

  private dModalViewEN_Subject = new Subject<boolean>();
  dModalViewENP$ = this.dModalViewEN_Subject.asObservable();

  private dModalViewTA_Subject = new Subject<boolean>();
  dModalViewTA$ = this.dModalViewTA_Subject.asObservable();

  private dModalViewPA_Subject = new Subject<boolean>();
  dModalViewPA$ = this.dModalViewPA_Subject.asObservable();

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

  indexMoment(index: number){
    this.dIndex_Subject.next(index);
  }

  stateModalDP(state: boolean){
    this.dModalViewDP_Subject.next(state)
  }

  stateModalCS(state: boolean){
    this.dModalViewCS_Subject.next(state)
  }

  stateModalEN(state: boolean){
    this.dModalViewEN_Subject.next(state)
  }

  stateModalTA(state: boolean){
    this.dModalViewTA_Subject.next(state)
  }

  stateModalPA(state: boolean){
    this.dModalViewPA_Subject.next(state)
  }
}
