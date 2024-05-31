import { Injectable } from '@angular/core';
import { map, Observable } from 'rxjs';
import { DiasGozados } from '../../../interfaces/DataPromocional/dias-gozados.interface';
import { DiasGozadosService } from '../../requests/DataPromocional/dias-gozados.service';
import { CommunicationDataService } from '../../communication/communicationData.service';

@Injectable({
  providedIn: 'root'
})
export class FdDiasGozadosService {

  diasData: DiasGozados[] = [];

  constructor(
    private diasgo: DiasGozadosService,
    private comData: CommunicationDataService
  ) { }

  fetchDiasGozados(index: number) {
    this.diasgo.getDiasGozados().subscribe((response: any) => {
      if(response && response.DIAS_GOZADOS){
        this.diasData = response.DIAS_GOZADOS.map((dgoza: any) => {
          return {
            ID: dgoza.ID,
            NAME: dgoza.NAME,
            selected: false
          }
        });
        this.comData.sendDataDiasGozados(this.diasData, index);
      }
    });
  }

  // RETORNO DIRECTO

  fetchDiasGozados_RETURN(): Observable<DiasGozados[]> {
    return this.diasgo.getDiasGozados().pipe(
      map((response: any) => {
        if(response && response.DIAS_GOZADOS){
          return response.DIAS_GOZADOS.map((dgoza: any) => {
            return {
              ID: dgoza.ID,
              NAME: dgoza.NAME,
              selected: false
            }
          })
        }
      })
    );
  }
}
