import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class TimeService {

  constructor() { }

  obtenerHoraActual(): string {
    const fechaActual: Date = new Date();
    const hora: number = fechaActual.getHours();
    const minutos: number = fechaActual.getMinutes();
    const segundos: number = fechaActual.getSeconds();

    const horaFormateada: string = hora < 10 ? `0${hora}` : `${hora}`;
    const minutosFormateados: string = minutos < 10 ? `0${minutos}` : `${minutos}`;
    const segundosFormateados: string = segundos < 10 ? `0${segundos}` : `${segundos}`;

    return `${horaFormateada}:${minutosFormateados}:${segundosFormateados}`;
  }
}
