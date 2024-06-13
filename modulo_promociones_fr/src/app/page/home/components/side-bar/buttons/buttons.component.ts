import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { CommunicationVisibleService } from '../../../../../services/communication/communicationVisible.service';
import { CommonModule } from '@angular/common';
import { FdPlanesService } from '../../../../../services/fetchData/fd-planes.service';
import { InjectionDataService } from '../../../../../services/injection/injection-data.service';

@Component({
  selector: 'app-buttons',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './buttons.component.html',
  styleUrl: './buttons.component.scss'
})
export class ButtonsComponent implements OnInit {

  showDropDown: boolean = false;
  closing: boolean = false; // Controla si el dropdown está en proceso de cierre
  visibleValueDiv: string | null = null;

  constructor(
    private comVisual: CommunicationVisibleService,
    private fdplan: FdPlanesService,
    private getTo: InjectionDataService
  ){}

  ngOnInit(): void {
    this.comVisual.visibleItemT$.subscribe( value => {this.visibleValueDiv = value});
  }

  toggleDropDown() {
    if (this.showDropDown) {
      // Si está abierto y se va a cerrar, activa la transición rápida
      this.closing = true;
      setTimeout(() => {
        this.showDropDown = false;
        this.closing = false; // Restablece el estado después de cerrar
      }, 30); // Espera el tiempo de la transición de cierre
    } else {
      // Si está cerrado y se va a abrir
      this.showDropDown = true;
    }
  }

  @Output() subButtonClick = new EventEmitter<string>();
  
  handleSubButtonClick(value: string): void {
    try
    {
      const valoresPermitidos = ['TISE', 'RED', 'PLAN', 'PROV', 'CITY', 'SECT'];
      if(valoresPermitidos.includes(value)){
        this.comVisual.visiblePrincipalComponent('TQ');
        this.comVisual.visibleSecundarioComponent(value)
      } else if(value = 'TI'){
        this.fdplan.fetchDataServicio();
        this.comVisual.visiblePrincipalComponent(value);
      }
    }
    catch (error)
    {
      console.log("---------------------------------------------------------------")
      console.log("botton.componets - handleSubButtonClick | Error detectado: ")
      console.log(error)
      console.log("---------------------------------------------------------------")
    }
  }

  changeValueVisible(){
    if(this.visibleValueDiv !== ''){
      this.comVisual.visibleTerceriaComponent('');
    }
  }
}
