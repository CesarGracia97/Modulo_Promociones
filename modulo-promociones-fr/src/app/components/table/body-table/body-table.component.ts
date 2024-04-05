import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { CommunicationService } from '../../../services/complements/communication.service';
import { TipoServicios } from '../../../interfaces/planes/tiposervicios.interface';
import { Tecnologias } from '../../../interfaces/planes/tecnologias.interface';
import { TariffPlanesVariant } from '../../../interfaces/planes/tariffplanes.interface';
import { Provincias } from '../../../interfaces/places/provincias.interface';
import { C_Ciudades, C_Sectores } from '../../../interfaces/planes/combos.interface';


@Component({
  selector: 'app-body-table',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './body-table.component.html',
  styleUrl: './body-table.component.scss'
})
export class BodyTableComponent {
  visibleDivId: string | null = null;
  tiseData: TipoServicios[] = [];
  redtData: Tecnologias[] = [];
  planData: TariffPlanesVariant[] = [];
  provData: Provincias [] = [];
  cityData: C_Ciudades [] = [];
  sectData: C_Sectores [] = [];
  constructor(
    private communicationService: CommunicationService
  ){}
  ngOnInit():void{
    this.communicationService.visbleItemT$.subscribe(operationId =>{
      this.visibleDivId = operationId;
    });
    this.communicationService.dTISE$.subscribe(data => {
      this.tiseData = data;
    });
    this.communicationService.dRed$.subscribe(data => {
      this.redtData = data;
    });
    this.communicationService.dPlan$.subscribe(data => {
      this.planData = data;
    });
    this.communicationService.dProv$.subscribe(data => {
      this.provData = data; 
    });
    this.communicationService.dCity$.subscribe(data => {
      this.cityData = data;
    });
    this.communicationService.dSect$.subscribe(data => {
      this.sectData = data;
    });
  }

}
