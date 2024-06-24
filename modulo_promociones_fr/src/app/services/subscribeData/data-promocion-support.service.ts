import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataPromocionSupportService {
  private idVariant: number[][] = [];
  private idProducto: number[][] = [];

  private dProductoId_Subject = new Subject<number[][]>();
  dProductoId$ = this.dProductoId_Subject.asObservable();

  private dVariantId_Subject = new Subject<number[][]>();
  dVariantId$ = this.dVariantId_Subject.asObservable();

  constructor() { }

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
}
