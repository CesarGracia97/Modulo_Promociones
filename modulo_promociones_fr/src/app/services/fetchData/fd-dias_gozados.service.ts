import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { DiasGozados } from '../../interfaces/DataPromocional/dias-gozados.interface';
import { DiasGozadosService } from '../requests/DataPromocional/dias-gozados.service';
import { response } from 'express';

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
        if(response)
      })
    );
  }
}
