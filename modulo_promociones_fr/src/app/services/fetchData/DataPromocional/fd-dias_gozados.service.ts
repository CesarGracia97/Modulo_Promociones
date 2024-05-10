import { Injectable } from '@angular/core';
import { map, Observable } from 'rxjs';
import { DiasGozados } from '../../../interfaces/DataPromocional/dias-gozados.interface';
import { DiasGozadosService } from '../../requests/DataPromocional/dias-gozados.service';

@Injectable({
  providedIn: 'root'
})
export class FdDiasGozadosService {

  constructor(
    private diasgo: DiasGozadosService
  ) { }

  getDiasGozados_RETURN(): Observable<DiasGozados[]> {
    return this.diasgo.getDiasGozados().pipe(
      map((response: any) => {
        if(response && response.DIAS_GOZADOS){
          return response.DIAS_GOZADOS.map((dgoza: any) => {
            return {
              ID: dgoza.ID,
              NAME: dgoza.NAME
            }
          })
        }
      })
    );
  }
}
