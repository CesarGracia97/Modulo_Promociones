import { Injectable } from '@angular/core';
import { TariffPlanes, TariffPlanesVariant } from '../../interfaces/planes/tariffplanes.interface';
import { CombosService } from '../requests/GET/planes/combos.service';
import { DataPromocionInformationService } from '../subscribeData/data-promocion-information.service';
import { Productos } from '../../interfaces/planes/productos.interface';
import { map, Observable } from 'rxjs';
import { DataProdadicInformationService } from '../subscribeData/data-prodadic-information.service';

@Injectable({
  providedIn: 'root'
})

export class FdCombosService {
  
  private c_planv: TariffPlanesVariant [] = [];
  private c_plan: TariffPlanes[] = [];
  private c_prod: Productos[] = [];

  constructor(
    private combo: CombosService,
    private dataCommunication: DataPromocionInformationService,
    private dataPromocionalAdicional: DataProdadicInformationService
  ) { }
  
  fetchDataComboPLAN(SERVICIO: string, index: number) {
    this.combo.getCombosPlan(SERVICIO).subscribe((response: any) => {
      if (response && response.COMBO_PLAN){
        this.c_plan = response.COMBO_PLAN.map((plan: any) => {
          return {
            TARIFFPLANID: plan.TARIFFPLANID,
            TARIFFPLAN: plan.TARIFFPLAN
          };
        })
        this.dataCommunication.sendDataPLAN(this.c_plan, index);
      }
    });
  }

  fetchDataComboPLANVARIANT(Id_Plan: number, index: number){
    this.combo.getCombosPlanVariant(Id_Plan).subscribe((response: any) => {
      if (response && response.COMBO_PLANVARIANT) {
        this.c_planv = response.COMBO_PLANVARIANT.map((plan: any) => {
          return {
            TARIFFPLANVARIANTID: plan.TARIFFPLANVARIANTID,
            TARIFFPLANVARIANT: plan.TARIFFPLANVARIANT
          };
        })
        this.dataCommunication.sendDataPLANVARIANT(this.c_planv, index);
      }
    })
  }

  fetchDataComboPROD(Id_TPV: number, index: number){
    this.combo.getCombosProductos(Id_TPV).subscribe((response: any) => {
      if(response && response.COMBO_PRODUCTO) {
        this.c_prod = response.COMBO_PRODUCTO.map((prod: Productos) => {
          return {
            PRODUCTID: prod.PRODUCTID,
            PRODUCTO: prod.PRODUCTO
          }
        })
        this.dataCommunication.sendDataPRODUCTO(this.c_prod, index)
      }
    })
  }

  fetchDataComboPROD_ROUTER(index: number){
    this.combo.getCombosProductos_Router().subscribe((response: any) => {
      if(response && response.COMBO_PRODUCTO) {
        this.c_prod = response.COMBO_PRODUCTO.map((prod: Productos) => {
          return {
            PRODUCTID: prod.PRODUCTID,
            PRODUCTO: prod.PRODUCTO
          }
        })
        console.log(this.c_prod);
        this.dataPromocionalAdicional.sendDataModelosRouter(this.c_prod, index)
      }
    });
  }

  //RETORNO DIRECTO
  
  fetchDataComboPLAN_RETURN(SERVICIO: string): Observable<TariffPlanes[]>{
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

  fetchDataComboPLANVARIANT_RETURN(Id_Plan: number): Observable<TariffPlanesVariant []>{
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

  fetchDataComboPROD_RETURN(Id_TPV: number): Observable<Productos[]>{
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

  fetchDataComboPROD_ROUTER_RETURN(): Observable<Productos[]>{
    return this.combo.getCombosProductos_Router().pipe(
      map((response: any) => {
        if(response && response.COMBO_PRODUCTO){
          return response.COMBO_PRODUCTO.map((pro: any) => {
            return {
              PRODUCTID: pro.PRODUCTID,
              PRODUCTO: pro.PRODUCTO
            }
          }); 
        }
      })
    );
  }
}