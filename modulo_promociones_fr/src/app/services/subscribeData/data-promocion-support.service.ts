import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataPromocionSupportService {
  private idVariant: number[][] = [];
  private idProducto: number[][] = [];
  private Servicio: string[][] = [];

  private dProductoId_Subject = new Subject<number[][]>();
  dProductoId$ = this.dProductoId_Subject.asObservable();

  private dVariantId_Subject = new Subject<number[][]>();
  dVariantId$ = this.dVariantId_Subject.asObservable();

  private dServicio_Subject = new Subject<string[][]>
  dServicio$ = this.dServicio_Subject.asObservable();

  private dMensajeModalView_Subject = new Subject<string>();
  dMensajeModalView$ = this.dMensajeModalView_Subject.asObservable();

  private dDicionarioComprobabled_Subject = new Subject<boolean[]>();
  dDicionarioComprobabled$ = this.dDicionarioComprobabled_Subject.asObservable();

  constructor() {}

  sendDataIdProducto(value: number, index: number){
    this.idProducto[index] = [];
    this.idProducto[index].push(value);
    this.dProductoId_Subject.next(this.idProducto);
  }

  sendDataIdVariant(value: number, index: number){
    this.idVariant[index] = [];
    this.idVariant[index].push(value);
    this.dVariantId_Subject.next(this.idVariant);
  }

  sendDataServicio(value: string, index: number){
    this.Servicio[index] = [];
    this.Servicio[index].push(value);
    this.dServicio_Subject.next(this.Servicio);
  }

  messagge(mensaje: string){
    this.dMensajeModalView_Subject.next(mensaje);
  }

  disableButtonSendDiccionario(data:{ [key: string]: any }, index: number) {

  }
}
