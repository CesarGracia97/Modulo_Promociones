import { Injectable } from '@angular/core';
import { ServiciosService } from '../requests/GET/planes/servicios.service';
import { TariffplanesService } from '../requests/GET/planes/tariffplanes.service';
import { Servicios } from '../../interfaces/planes/servicios.interface';
import { TariffPlanesVariant } from '../../interfaces/planes/tariffplanes.interface';
import { DataPromocionInformationService } from '../subscribeData/data-promocion-information.service';
import { map, Observable } from 'rxjs';
import { DataProdadicInformationService } from '../subscribeData/data-prodadic-information.service';

@Injectable({
  providedIn: 'root'
})
export class FdPlanesService {

  private serviciosData: Servicios[] = [];
  private planVData: TariffPlanesVariant[] = [];
  
  constructor(
    private serv: ServiciosService,
    private plan: TariffplanesService,
    private comDataPromocion: DataPromocionInformationService,
    private comDataDataPromocionAdicional: DataProdadicInformationService
  ) { }

  fetchDataServicio(){
    this.serv.getServiciosALL().subscribe((response: any) => {
      if (response && response.SERVICIOS) {
        this.serviciosData = response.SERVICIOS.map((servicio: any) => servicio.SERVICIO);
        this.comDataPromocion.sendDataServicio(this.serviciosData);
      } else {
        console.error("La respuesta no contiene la propiedad 'SERVICIOS'.");
      }
    });
  }

  fetchDataTariffPlanVariantXProductoAdicional(SERVICIO: string, index: number, tabla: number){
    this.plan.getTariffPlanesVariantXProducto_Adicional(SERVICIO).subscribe((response: any) => {
      if (response && response.PLANES) {
        this.planVData = response.PLANES.map((plan: any) => {
          return {
            TARIFFPLANVARIANTID: plan.TARIFFPLANVARIANTID,
            TARIFFPLANVARIANT: plan.TARIFFPLANVARIANT
          };
        });
        this.comDataDataPromocionAdicional.senDataPaquetesPlanes(this.planVData, index, tabla, SERVICIO);
      }
    })
  }
  //RETORNO DIRECTO

  fetchDataTariffPlanVariantXProductoAdicional_RETURN(SERVICIO: string): Observable<TariffPlanesVariant[]> {
    return this.plan.getTariffPlanesVariantXProducto_Adicional(SERVICIO).pipe(
      map((response: any) => {
        if (response && response.PLANES){
          return response.PLANES.map((plan: any ) => {
            return {
              TARIFFPLANVARIANTID: plan.TARIFFPLANVARIANTID,
              TARIFFPLANVARIANT: plan.TARIFFPLANVARIANT
            };
          });
        } else {
          return [];
        }
      })
    );
  }
}
