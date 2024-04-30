import { Injectable } from '@angular/core';
import { TipoServicios } from '../../interfaces/planes/tiposervicios.interface';
import { Tecnologias } from '../../interfaces/planes/tecnologias.interface';
import { TariffPlanesVariant } from '../../interfaces/planes/tariffplanes.interface';
import { Provincias } from '../../interfaces/places/provincias.interface';
import { C_Ciudades, C_Sectores } from '../../interfaces/planes/combos.interface';
import { CombosService } from '../requests/planes/combos.service';
import { CommunicationDataService } from '../communication/communicationData.service';
import { CommunicationVisibleService } from '../communication/communicationVisible.service';
import { map, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FdCombosService {

  c_tise: TipoServicios[] = [];
  c_redt: Tecnologias [] = [];
  c_plan: TariffPlanesVariant [] = [];
  c_prov: Provincias [] = [];
  c_city: C_Ciudades [] = [];
  c_sect: C_Sectores [] = [];

  
  constructor(
    private combo: CombosService,
    private comData: CommunicationDataService,
    private comVisible: CommunicationVisibleService
  ) { }

  getComboTISE(diccionario:{[key: string]: any}){
    const id = diccionario['id'];
    let _V1;
    _V1 = diccionario['_V1'];
    this.combo.getCombosTipoServicios(_V1).subscribe((response: any) => {
      if(response && response.C_TIPO_SERVICIOS){
        this.c_tise = response.C_TIPO_SERVICIOS.map((tise: any) => tise.TIPO_SERVICIO);
        this.comData.sendDataTISE(this.c_tise);
        this.comVisible.visibleTerceriaComponent(id);
      } else {
        console.error("La respuesta no contiene la propiedad 'TIPO_SERVICIO'.");
      }
    });
  }

  getComboRED(diccionario:{[key: string]: any}){
    const id = diccionario['id'];
    let _V1, _V2;
    _V1 = diccionario['_V1'];
    _V2 = diccionario['_V2'];
    this.combo.getCombosRedTecnologia(_V1,_V2).subscribe((response: any) => {
      if(response && response.C_TECNOLOGIA){
        this.c_redt = response.C_TECNOLOGIA.map((red: any) => red.TECNOLOGIA);
        this.comData.sendDataRED(this.c_redt);
        this.comVisible.visibleTerceriaComponent(id);
      } else {
        console.error("La respuesta no presenta la propiedad 'TECNOLOGIA'.")
      }
    });
  }

  getComboPLAN(diccionario:{[key: string]: any}){
    const id = diccionario['id'];
    let _V1, _V2, _V3;
    _V1 = diccionario['_V1'];
    _V2 = diccionario['_V2'];
    _V3 = diccionario['_V3'];
    this.combo.getCombosPlanes(_V1, _V2, _V3).subscribe((response: any) => {
      if (response && response.C_PLANES){
        this.c_plan = response.C_PLANES.map((plan: any) => {
          return {
            TARIFFPLANVARIANTID: plan.TARIFFPLANVARIANTID,
            TARIFFPLANVARIANT: plan.TARIFFPLANVARIANT
          };
        });
        console.log("Info de c_plan",this.c_plan); 
        this.comData.sendDataPLAN(this.c_plan);
        this.comVisible.visibleTerceriaComponent(id);
      } else {
        console.error("La respuesta no presenta la propiedad 'TECNOLOGIA'.")
      } 
    });
  }

  getComboPROV(diccionario:{[key: string]: any}){
    const id = diccionario['id'];
    let _V1, _V2, _V3, _V4;
    _V1 = diccionario['_V1'];
    _V2 = diccionario['_V2'];
    _V3 = diccionario['_V3'];
    _V4 = diccionario['_V4'];
    this.combo.getCombosProvincia(_V1, _V2, _V3, parseInt(_V4)).subscribe((response: any) => {
      if (response && response.C_PROVINCIA){
        this.c_prov= response.C_PROVINCIA.map((prov: any) => {
          return {
            PROVINCIA_ID: prov.PROVINCIA_ID,
            PROVINCIA: prov.PROVINCIA
          };
        });
        this.comData.sendDataPROV(this.c_prov);
        this.comVisible.visibleTerceriaComponent(id);
      } else {
        console.error("la consutla no posee la propiedad 'C_PROVINCIA'");
      }
    });
  }

  getComboCITY(diccionario:{[key: string]: any}){
    const id = diccionario['id'];
    let _V1, _V2, _V3, _V4, _V5;
    _V1 = diccionario['_V1'];
    _V2 = diccionario['_V2'];
    _V3 = diccionario['_V3'];
    _V4 = diccionario['_V4'];
    _V5 = diccionario['_V5'];
    this.combo.getCombosCiudad(_V1, _V2, _V3, parseInt(_V4), parseInt(_V5)).subscribe((response: any) => {
      if (response && response.C_CIUDAD){
        this.c_city= response.C_CIUDAD.map((city: any) => {
          return {
            PROVINCIA: city.PROVINCIA,
            CIUDAD_ID: city.CIUDAD_ID,
            CIUDAD: city.CIUDAD
          };
        });
        this.comData.sendDataCITY(this.c_city);
        this.comVisible.visibleTerceriaComponent(id); 
      } else {
        console.error("la consutla no posee la propiedad 'C_CIUDAD'");
      }
    });
  }

  getComboSECT(diccionario:{[key: string]: any}){
    const id = diccionario['id'];
    let _V1, _V2, _V3, _V4, _V5, _V6;
    _V1 = diccionario['_V1'];
    _V2 = diccionario['_V2'];
    _V3 = diccionario['_V3'];
    _V4 = diccionario['_V4'];
    _V5 = diccionario['_V5'];
    _V6 = diccionario['_V6'];
    this.combo.getCombosSectores(_V1, _V2, _V3, parseInt(_V4), parseInt(_V5), parseInt(_V6)).subscribe((response: any) => {

      if (response && response.C_SECTOR){
        this.c_sect= response.C_SECTOR.map((sect: any) => {
          return {
            CIUDAD: sect.CIUDAD,
            SECTOR_ID: sect.SECTOR_ID,
            SECTOR: sect.SECTOR
          };
        });
        this.comData.sendDataSECT(this.c_sect);
        this.comVisible.visibleTerceriaComponent(id);  
      } else {
        console.error("la consutla no posee la propiedad 'C_SECTOR'");
      }
    });
  }

  // Retornar informacion Directamente

  getComboRED_RETURN(SERVICIO: string, TIPO_SERVICIOS:string): Observable<Tecnologias []>{
    
    return this.combo.getCombosRedTecnologia(SERVICIO, TIPO_SERVICIOS).pipe(
      map((response: any) => {
        if(response && response.C_TECNOLOGIA){
          return response.C_TECNOLOGIA.map((red: any) => red.TECNOLOGIA); 
        } else {
          return [];
        }
      })
    );
  }

  getComboPLAN_RETURN(SERVICIO: string, TIPO_SERVICIOS:string, TECNOLOGIA: string): Observable<TariffPlanesVariant []>{
     return this.combo.getCombosPlanes(SERVICIO, TIPO_SERVICIOS, TECNOLOGIA).pipe(
      map((response: any) => {
        if (response && response.C_PLANES){
          return response.C_PLANES.map((plan: any) => {
            return {
              TARIFFPLANVARIANTID: plan.TARIFFPLANVARIANTID,
              TARIFFPLANVARIANT: plan.TARIFFPLANVARIANT
            };
          });
        }
      })
     );
  }

  getComboTISE_RETURN(SERVICIO: string): Observable<TipoServicios[]> {
    return this.combo.getCombosTipoServicios(SERVICIO).pipe(
      map((response: any) => {
        if(response && response.C_TIPO_SERVICIOS){
          return this.c_tise = response.C_TIPO_SERVICIOS.map((tise: any) => tise.TIPO_SERVICIO);
        }
      })
    );
  }
}