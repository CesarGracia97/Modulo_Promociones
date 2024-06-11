import { Injectable } from '@angular/core';
import { UpgradeService } from '../../requests/GET/DataPromocional/upgrade.service';
import { Upgrade } from '../../../interfaces/DataPromocional/upgrade.interface';
import { CommunicationDataService } from '../../communication/communicationData.service';
import { map, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FdUpgradeService {
  private upgradeData: Upgrade[] = [];

  constructor(
    private upgr: UpgradeService,
    private comData: CommunicationDataService
  ) { }

  fetchDataUpgrade(Tariffplan: number, TFPV: number, index: number){
    this.upgr.getUpgrade(Tariffplan, TFPV).subscribe((response: any) => {
      if(response && response.UPGRADE){
        this.upgradeData = response.UPGRADE.map((upgrade: any) => {
          return {
            ID: upgrade.ID,
            PLAN_UPGRADE: upgrade.PLAN_UPGRADE
          }
        });
        this.comData.sendDataUPGRADE(this.upgradeData, index);
      }
    });
  }

  //RETORNO DIRECTO

  fetchDataUpgrade_RETURN(Tariffplan: number, TFPV: number): Observable<Upgrade[]> {
    return this.upgr.getUpgrade(Tariffplan, TFPV).pipe(
      map((response: any) => {
        if(response && response.UPGRADE){
          return response.UPGRADE.map((upgrade: any) => {
            return {
              ID: upgrade.ID,
              PLAN_UPGRADE: upgrade.PLAN_UPGRADE
            }
          })
        }
      })
    );
  }
}
