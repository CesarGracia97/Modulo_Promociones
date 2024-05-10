import { Injectable } from '@angular/core';
import { UpgradeService } from '../../requests/DataPromocional/upgrade.service';
import { map, Observable } from 'rxjs';
import { Upgrade } from '../../../interfaces/DataPromocional/upgrade.interface';

@Injectable({
  providedIn: 'root'
})
export class FdUpgradeService {

  constructor(
    private upgr: UpgradeService
  ) { }

  getUpgrade_RETURN(TFPV: number): Observable<Upgrade[]> {
    return this.upgr.getUpgrade(TFPV).pipe(
      map((response: any) => {
        if(response && response.UPGRADE){
          return response.UPGRADE.map((upgrade: any) => {
            return {
              ID: upgrade.ID,
              NAME: upgrade.NAME
            }
          })
        }
      })
    );
  }
}
