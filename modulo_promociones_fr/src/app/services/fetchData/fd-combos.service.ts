import { Injectable } from '@angular/core';
import { TipoServicios } from '../../interfaces/planes/tiposervicios.interface';
import { Tecnologias } from '../../interfaces/planes/tecnologias.interface';
import { TariffPlanes, TariffPlanesVariant } from '../../interfaces/planes/tariffplanes.interface';
import { Provincias } from '../../interfaces/places/provincias.interface';
import { C_Ciudades, C_Sectores } from '../../interfaces/planes/combos.interface';
import { CombosService } from '../requests/planes/combos.service';
import { CommunicationDataService } from '../communication/communicationData.service';
import { CommunicationVisibleService } from '../communication/communicationVisible.service';
import { map, Observable } from 'rxjs';
import { Productos } from '../../interfaces/planes/productos.interface';

@Injectable({
  providedIn: 'root'
})
export class FdCombosService {

  c_tise: TipoServicios[] = [];
  c_redt: Tecnologias [] = [];
  c_plan: TariffPlanesVariant [] = [];
  c_planv: TariffPlanes[] = [];
  c_prov: Provincias [] = [];
  c_city: C_Ciudades [] = [];
  c_sect: C_Sectores [] = [];

  
  constructor(
    private combo: CombosService,
  ) { }

  // Retornar informacion Directamente

  getComboPLAN_RETURN(SERVICIO: string): Observable<TariffPlanes[]>{
     return this.combo.getCombosPlan(SERVICIO).pipe(
      map((response: any) => {
        if (response && response.COMBO_PLAN){
          return response.COMBO_PLAN.map((plan: any) => {
            return {
              TARIFFPLANID: plan.TARIFFPLANID,
              TARIFFPLAN: plan.TARIFFPLAN
            };
          });
        }
      })
     );
  }

  getComboPLANVARIANT_RETURN(Id_Plan: number): Observable<TariffPlanesVariant []>{
    return this.combo.getCombosPlanVariant(Id_Plan).pipe(
     map((response: any) => {
       if (response && response.COMBO_PLANVARIANT){
         return response.COMBO_PLANVARIANT.map((plan: any) => {
           return {
             TARIFFPLANVARIANTID: plan.TARIFFPLANVARIANTID,
             TARIFFPLANVARIANT: plan.TARIFFPLANVARIANT
           };
         });
       }
     })
    );
 }

  getComboPROD_RETURN(Id_TPV: number): Observable<Productos[]>{
    return this.combo.getCombosProductos(Id_TPV).pipe(
      map((response: any) => {
        if(response && response.COMBO_PRODUCTO){
          return response.COMBO_PRODUCTO.map((pro: any) => {
            return {
              PRODUCTID: pro.PRODUCTID,
              PRODUCTO: pro.PRODUCTO
            }
          }); 
        } else {
          return [];
        }
      })
    );
  }

  getComboTISE_RETURN(Id_TPV: number): Observable<TipoServicios[]> {
    return this.combo.getCombosTipoServicios(Id_TPV).pipe(
      map((response: any) => {
        if(response && response.COMBO_TIPO_SERVICIO){
          return this.c_tise = response.COMBO_TIPO_SERVICIO.map((tise: any) => tise.TIPO_SERVICIO);
        }
      })
    );
  }
}