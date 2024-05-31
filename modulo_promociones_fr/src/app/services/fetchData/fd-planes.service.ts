import { Injectable } from '@angular/core';
import { ServiciosService } from '../requests/planes/servicios.service';
import { TariffplanesService } from '../requests/planes/tariffplanes.service';
import { Servicios } from '../../interfaces/planes/servicios.interface';
import { TariffPlanesVariant } from '../../interfaces/planes/tariffplanes.interface';
import { CommunicationDataService } from '../communication/communicationData.service';
import { map, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FdPlanesService {

  private serviciosData: Servicios[] = [];
  private planVData: TariffPlanesVariant[] = [];
  
  constructor(
    private serv: ServiciosService,
    private plan: TariffplanesService,
    private comData: CommunicationDataService
  ) { }

  fetchDataServicio(){
    this.serv.getServiciosALL().subscribe((response: any) => {
      if (response && response.SERVICIOS) {
        this.serviciosData = response.SERVICIOS.map((servicio: any) => servicio.SERVICIO);
        this.comData.sendDataServicio(this.serviciosData);
      } else {
        console.error("La respuesta no contiene la propiedad 'SERVICIOS'.");
      }
    });
  }

  fetchDataTariffPlanVariantXProductoAdicional(SERVICIO: string, index: number){
    this.plan.getTariffPlanesVariantXProducto_Adicional(SERVICIO).subscribe((response: any) => {
      if (response && response.PLANES) {
        this.planVData = response.PLANES.map((plan: any) => {
          return {
            TARIFFPLANVARIANTID: plan.TARIFFPLANVARIANTID,
            TARIFFPLANVARIANT: plan.TARIFFPLANVARIANT
          };
        });
        switch(SERVICIO){
          case 'STREAMING':
            this.comData.senDataPaquetesStreaming(this.planVData, index);
            break;
          case 'TELEFONIA':
            this.comData.sendDataPlanesTelefonicos(this.planVData, index);
            break;
          case 'TELEVISION':
            this.comData.sendDataPlanesTelevisivos(this.planVData, index);
            break;
        }
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
