import { Injectable } from '@angular/core';
import { TariffPlanes, TariffPlanesVariant } from '../../interfaces/planes/tariffplanes.interface';
import { CombosService } from '../requests/planes/combos.service';
import { CommunicationDataService } from '../communication/communicationData.service';
import { Productos } from '../../interfaces/planes/productos.interface';

@Injectable({
  providedIn: 'root'
})

export class FdCombosService {
  
  private c_planv: TariffPlanesVariant [] = [];
  private c_plan: TariffPlanes[] = [];
  private c_prod: Productos[] = [];

  constructor(
    private combo: CombosService,
    private dataCommunication: CommunicationDataService
  ) { }
  
  getComboPLAN(SERVICIO: string, index: number) {
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

  getComboPLANVARIANT(Id_Plan: number, index: number){
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

  getComboPROD(Id_TPV: number, index: number){
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
}