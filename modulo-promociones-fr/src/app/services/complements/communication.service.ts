import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import { CombosService } from '../planes/combos.service';
import { TipoServicios } from '../../interfaces/planes/tiposervicios.interface';
import { Tecnologias } from '../../interfaces/planes/tecnologias.interface';
import {  TariffPlanesVariant } from '../../interfaces/planes/tariffplanes.interface';
import { Provincias } from '../../interfaces/places/provincias.interface';
import { C_Ciudades, C_Sectores } from '../../interfaces/planes/combos.interface';


@Injectable({
  providedIn: 'root'
})
export class CommunicationService {

  //Visibilidad de Componentes
  private visibleItemSSubject = new Subject<string>();
  visbleItemS$ = this.visibleItemSSubject.asObservable();
  private visibleItemTSubject = new Subject<string>();
  visbleItemT$ = this.visibleItemTSubject.asObservable();

  //Datos entre componentes
  private dTISE_Subject = new Subject<TipoServicios[]>();
  dTISE$ = this.dTISE_Subject.asObservable();
  private dRED_Subject = new Subject<Tecnologias[]>();
  dRed$ = this.dRED_Subject.asObservable();


  c_tise: TipoServicios [] = [];
  c_redt: Tecnologias [] = [];
  c_plan: TariffPlanesVariant [] = [];
  c_prov: Provincias [] = [];
  c_city: C_Ciudades [] = [];
  c_sect: C_Sectores [] = [];

  constructor(
    private combo: CombosService
  ) {}

  sendSelectedButton(buttonId: string) {
    this.visibleItemSSubject.next(buttonId);
  }

  sendDataHeaderTable(diccionario:{[key: string]: any}){
    const id = diccionario['id'];
    let _V1, _V2, _V3, _V4, _V5, _V6;
    switch (id){
      case 'TISE':
        _V1 = diccionario['_V1'];
        this.combo.getCombosTipoServicios(_V1).subscribe((response: any) => {
          if(response && response.C_TIPO_SERVICIOS){
            this.c_tise = response.C_TIPO_SERVICIOS.map((tise: any) => tise.TIPO_SERVICIO);
            this.dTISE_Subject.next(this.c_tise);
          } else {
            console.error("La respuesta no contiene la propiedad 'TIPO_SERVICIO'.");
          }
        });
        this.visibleItemTSubject.next(id);
        break;
      case 'RED':
        _V1 = diccionario['_V1'];
        _V2 = diccionario['_V2'];
        this.combo.getCombosRedTecnologia(_V1,_V2).subscribe((response: any) => {
          console.log(response);
        });
        this.visibleItemTSubject.next(id);
        break;
      case 'PLAN':
        _V1 = diccionario['_V1'];
        _V2 = diccionario['_V2'];
        _V3 = diccionario['_V3'];
        this.combo.getCombosPlanes(_V1, _V2, _V3).subscribe((response: any) => {
          console.log(response);
        });
        this.visibleItemTSubject.next(id);
        break;
      case 'PROV':
        _V1 = diccionario['_V1'];
        _V2 = diccionario['_V2'];
        _V3 = diccionario['_V3'];
        _V4 = diccionario['_V4'];
        this.combo.getCombosProvincia(_V1, _V2, _V3, parseInt(_V4)).subscribe((response: any) => {
          console.log(response);
        });
        this.visibleItemTSubject.next(id);
        break;
      case 'CITY':
        _V1 = diccionario['_V1'];
        _V2 = diccionario['_V2'];
        _V3 = diccionario['_V3'];
        _V4 = diccionario['_V4'];
        _V5 = diccionario['_V5'];
        this.combo.getCombosCiudad(_V1, _V2, _V3, parseInt(_V4), parseInt(_V5)).subscribe((response: any) => {
          console.log(response);
        });
        this.visibleItemTSubject.next(id);
        break;
      case 'SECT':
        _V1 = diccionario['_V1'];
        _V2 = diccionario['_V2'];
        _V3 = diccionario['_V3'];
        _V4 = diccionario['_V4'];
        _V5 = diccionario['_V5'];
        _V6 = diccionario['_V6'];
        this.combo.getCombosSectores(_V1, _V2, _V3, parseInt(_V4), parseInt(_V5), parseInt(_V6)).subscribe((response: any) => {
          console.log(response);
        });
        this.visibleItemTSubject.next(id);
        break;
      default:
        console.log("Combo no registrado contactase con soporte")
    }
  }
}
