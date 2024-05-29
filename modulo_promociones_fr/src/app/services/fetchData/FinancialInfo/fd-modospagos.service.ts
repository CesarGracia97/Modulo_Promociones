import { Injectable } from '@angular/core';
import { ModosPago } from '../../../interfaces/financial/modos-pago.interface';
import { FormaspagoService } from '../../requests/FinancialInfo/formaspago.service';
import { CommunicationDataService } from '../../communication/communicationData.service';
import { map, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FdModospagosService {
  modoPagoData: ModosPago[] = [];

  constructor(
    private modp : FormaspagoService,
    private comData: CommunicationDataService
  ) { }

  fetchDataModosPago(index: number){
    this.modp.getModosPago().subscribe((response: any) => {
      if(response && response.MPAGOS){
        this.modoPagoData = response.MPAGOS.map((mdpg: any) => {
          return {
            ID: mdpg.ID,
            NAME: mdpg.NAME,
            selected: false
          }
        });
        this.comData.sendDataModosPago(this.modoPagoData, index);
      }
    });
  }

  fetchDataModosPago_RETURN(): Observable<ModosPago[]> {
    return this.modp.getModosPago().pipe(
      map((response: any) =>{
        if(response && response.MPAGOS){
          return response.MPAGOS.map((mdpg: any) => {
            return {
              ID: mdpg.ID,
              NAME: mdpg.NAME,
              selected: false
            }
          });
        }
      })
    );
  }
}
