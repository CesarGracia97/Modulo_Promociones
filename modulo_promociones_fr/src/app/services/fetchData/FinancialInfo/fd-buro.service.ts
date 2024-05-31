import { Injectable } from '@angular/core';
import { CommunicationDataService } from '../../communication/communicationData.service';
import { Buro } from '../../../interfaces/financial/buro.interface';
import { BuroService } from '../../requests/FinancialInfo/buro.service';
import { map, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FdBuroService {
  buroData: Buro[] = []

  constructor(
    private comData: CommunicationDataService,
    private buro: BuroService
  ) { }

  fetchDataBuro(index: number){
    this.buro.getTiposBuro().subscribe((response: any) => {
      if(response && response.BURO){
        this.buroData = response.BURO.map((bur: any) => {
          return {
            ID: bur.ID,
            NAME: bur.NAME
          }
        });
        this.comData.sendDataBuro(this.buroData, index);
      }
    });
  }

  // RETORNO DIRECTO

  fetchDataBuro_RETURN(): Observable <Buro[]>{
    return this.buro.getTiposBuro().pipe(
      map((response: any) => {
        if(response && response.BURO){
          return response.BURO.map((bur: any) => {
            return {
              ID: bur.ID,
              NAME: bur.NAME
            }
          });
        }
      }
    ));
  }
}
