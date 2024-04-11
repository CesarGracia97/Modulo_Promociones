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
  private dPLAN_Subject = new Subject<TariffPlanesVariant[]>();
  dPlan$ = this.dPLAN_Subject.asObservable();
  private dPROV_Subject = new Subject<Provincias[]>();
  dProv$ = this.dPROV_Subject.asObservable();
  private dCITY_Subject = new Subject<C_Ciudades[]>();
  dCity$ = this.dCITY_Subject.asObservable();
  private dSECT_Subject = new Subject<C_Sectores[]>();
  dSect$ = this.dSECT_Subject.asObservable();


  c_tise: TipoServicios[] = [];
  c_redt: Tecnologias [] = [];
  c_plan: TariffPlanesVariant [] = [];
  c_prov: Provincias [] = [];
  c_city: C_Ciudades [] = [];
  c_sect: C_Sectores [] = [];

  constructor(
    private combo: CombosService
  ) {}

  visibleHeaderTable(buttonId: string) {
    this.visibleItemSSubject.next(buttonId);
  }

  visibleBodyTable(id:string) {
    this.visibleItemTSubject.next(id);
  }

  sendDataHeaderTable(diccionario:{[key: string]: any}) {
    const id = diccionario['id'];
    let _V1, _V2, _V3, _V4, _V5, _V6;
    switch (id){
      case 'TISE':
        _V1 = diccionario['_V1'];
        this.combo.getCombosTipoServicios(_V1).subscribe((response: any) => {
          if(response && response.C_TIPO_SERVICIOS){
            this.c_tise = response.C_TIPO_SERVICIOS.map((tise: any) => tise.TIPO_SERVICIO);
            this.dTISE_Subject.next(this.c_tise);
            this.visibleItemTSubject.next(id);
          } else {
            console.error("La respuesta no contiene la propiedad 'TIPO_SERVICIO'.");
          }
        });
        break;
      case 'RED':
        _V1 = diccionario['_V1'];
        _V2 = diccionario['_V2'];
        this.combo.getCombosRedTecnologia(_V1,_V2).subscribe((response: any) => {
          if(response && response.C_TECNOLOGIA){
            this.c_redt = response.C_TECNOLOGIA.map((red: any) => red.TECNOLOGIA);
            this.dRED_Subject.next(this.c_redt);
            this.visibleItemTSubject.next(id);
          } else {
            console.error("La respuesta no presenta la propiedad 'TECNOLOGIA'.")
          }
        });
        break;
      case 'PLAN':
        _V1 = diccionario['_V1'];
        _V2 = diccionario['_V2'];
        _V3 = diccionario['_V3'];
        this.combo.getCombosPlanes(_V1, _V2, _V3).subscribe((response: any) => {
          console.log(response);
          if (response && response.C_PLANES){
            this.c_plan = response.C_PLANES.map((plan: any) => {
              return {
                TARIFFPLANVARIANTID: plan.TARIFFPLANVARIANTID,
                TARIFFPLANVARIANT: plan.TARIFFPLANVARIANT
              };
            });
            console.log("Info de c_plan",this.c_plan); 
            this.dPLAN_Subject.next(this.c_plan);
            this.visibleItemTSubject.next(id);
          } else {
            console.error("La respuesta no presenta la propiedad 'TECNOLOGIA'.")
          } 
        });
        break;
      case 'PROV':
        _V1 = diccionario['_V1'];
        _V2 = diccionario['_V2'];
        _V3 = diccionario['_V3'];
        _V4 = diccionario['_V4'];
        this.combo.getCombosProvincia(_V1, _V2, _V3, parseInt(_V4)).subscribe((response: any) => {
          console.log(response);
          if (response && response.C_PROVINCIA){
            this.c_prov= response.C_PROVINCIA.map((prov: any) => {
              return {
                PROVINCIA_ID: prov.PROVINCIA_ID,
                PROVINCIA: prov.PROVINCIA
              };
            });
            console.log(this.c_prov);
            this.dPROV_Subject.next(this.c_prov);
            this.visibleItemTSubject.next(id); 
          } else {
            console.error("la consutla no posee la propiedad 'C_PROVINCIA'");
          }
        });
        break;
      case 'CITY':
        _V1 = diccionario['_V1'];
        _V2 = diccionario['_V2'];
        _V3 = diccionario['_V3'];
        _V4 = diccionario['_V4'];
        _V5 = diccionario['_V5'];
        this.combo.getCombosCiudad(_V1, _V2, _V3, parseInt(_V4), parseInt(_V5)).subscribe((response: any) => {
          console.log(response);
          if (response && response.C_CIUDAD){
            this.c_city= response.C_CIUDAD.map((city: any) => {
              return {
                PROVINCIA: city.PROVINCIA,
                CIUDAD_ID: city.CIUDAD_ID,
                CIUDAD: city.CIUDAD
              };
            });
            console.log(this.c_city);
            this.dCITY_Subject.next(this.c_city);
            this.visibleItemTSubject.next(id); 
          } else {
            console.error("la consutla no posee la propiedad 'C_CIUDAD'");
          }
        });
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
          if (response && response.C_SECTOR){
            this.c_sect= response.C_SECTOR.map((sect: any) => {
              return {
                CIUDAD: sect.CIUDAD,
                SECTOR_ID: sect.SECTOR_ID,
                SECTOR: sect.SECTOR
              };
            });
            console.log(this.c_sect);
            this.dSECT_Subject.next(this.c_sect);
            this.visibleItemTSubject.next(id); 
          } else {
            console.error("la consutla no posee la propiedad 'C_SECTOR'");
          }
        });
        break;
      default:
        console.log("Combo no registrado contactase con soporte")
    }
  }
}
