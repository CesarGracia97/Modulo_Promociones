import { Injectable } from '@angular/core';
import { BehaviorSubject, Subject } from 'rxjs';
import { Options_PA } from '../../interfaces/Interfaces-View/Options_PA.interface';

@Injectable({
  providedIn: 'root'
})
export class DataViewService {

  optionsData: Options_PA[][] = [];
  //Variables de Comunicacion visual entre componentes de Table Query
  private visibleItemPrincipal_Subject = new Subject<string>();
  visbleItemP$ = this.visibleItemPrincipal_Subject.asObservable(); //de Botones a Contenedor Prima
  private visibleItemSecundario_Subject = new Subject<string>();
  visbleItemS$ = this.visibleItemSecundario_Subject.asObservable(); //de Botones a Elementos de Contenedor Prima
  private visibleItemTercero_Subject = new Subject<string>();
  visibleItemT$ = this.visibleItemTercero_Subject.asObservable(); // entre Componentes de un mismo Contenedor

  private dIndex_Subject = new Subject<number>();
  dIndex$ = this.dIndex_Subject.asObservable();

  private dRows_Subject = new BehaviorSubject<any>(null);
  dRows$ = this.dRows_Subject.asObservable();

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

  private dModalViewUP_Subject = new Subject<boolean>();
  dModalViewUP$ = this.dModalViewUP_Subject.asObservable();

  private dOptionsDataView_Subject = new Subject<Options_PA[][]>();
  dOptionsDataView$ = this.dOptionsDataView_Subject.asObservable();

  private dModalViewMessage_Subject = new Subject<boolean>();
  dModalViewMessage$ = this.dModalViewMessage_Subject.asObservable();

  private dNombrePromocionView_Subject = new Subject<string>();
  dNombrePromocionView$ = this.dNombrePromocionView_Subject.asObservable();

  constructor() { }

  visiblePrincipalComponent(value: string){
    this.visibleItemPrincipal_Subject.next(value);
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

  rowMoment(data: any) {
    this.dRows_Subject.next(data);
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

  stateModalUP(state: boolean){
    this.dModalViewUP_Subject.next(state)
  }

  stateModalMessage(state: boolean){
    this.dModalViewMessage_Subject.next(state)
  }

  nombrePromocionView(name: string){
    this.dNombrePromocionView_Subject.next(name);
  }

  sendOptionsPAView( state: boolean, index: number){
    if(state){
      this.optionsData[index] = [];
      this.optionsData[index].push(...[
        {name: 'NO APLICAR', selected: false},
        {name: 'STREAMING', selected: false},
        {name: 'TELEFONIA', selected: false},
        {name: 'TELEVISION', selected: false},
        {name: 'ROUTER', selected: false }
      ]);
      this.dOptionsDataView_Subject.next(this.optionsData);
    } else {
      this.optionsData[index] = [];
      this.optionsData[index].push(...[
        {name: 'NO APLICAR', selected: false},
        {name: 'STREAMING', selected: false},
        {name: 'TELEFONIA', selected: false},
        {name: 'TELEVISION', selected: false}
      ]);
      this.dOptionsDataView_Subject.next(this.optionsData);
    }
  }
}
