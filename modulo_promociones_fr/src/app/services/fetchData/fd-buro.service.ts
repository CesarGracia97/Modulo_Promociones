import { Injectable } from '@angular/core';
import { CommunicationDataService } from '../communication/communicationData.service';
import { Buro } from '../../interfaces/financial/buro.interface';
import { BuroService } from '../requests/FinancialInfo/buro.service';

@Injectable({
  providedIn: 'root'
})
export class FdBuroService {
  buroData: Buro[] = []

  constructor(
    private comData: CommunicationDataService,
    private buro: BuroService
  ) { }

  fetchDataBuro(){
    console.log("BuroData");
    this.buro.getTiposBuro().subscribe((response: any) => {
      console.log(response);
      if(response && response.BURO){
        this.buroData = response.BURO.map((bur: any) => {
          return {
            ID: bur.ID,
            NAME: bur.NAME
          }
        });
        this.comData.sendDataBuro(this.buroData);
      }
    });
  }
}
