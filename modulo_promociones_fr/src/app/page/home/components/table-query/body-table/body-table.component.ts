import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { TipoServicios } from '../../../../../interfaces/planes/tiposervicios.interface';
import { Tecnologias } from '../../../../../interfaces/planes/tecnologias.interface';
import { Provincias } from '../../../../../interfaces/places/provincias.interface';
import { TariffPlanesVariant } from '../../../../../interfaces/planes/tariffplanes.interface';
import { C_Ciudades, C_Sectores } from '../../../../../interfaces/planes/combos.interface';
import { CommunicationDataService } from '../../../../../services/communication/communicationData.service';
import { CommunicationVisibleService } from '../../../../../services/communication/communicationVisible.service';

@Component({
  selector: 'app-body-table',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './body-table.component.html',
  styleUrl: './body-table.component.scss'
})
export class BodyTableComponent implements OnInit{
  visibleDivId: string | null = null;
  tiseData: TipoServicios[] = [];
  redtData: Tecnologias[] = [];
  planData: TariffPlanesVariant[] = [];
  provData: Provincias [] = [];
  cityData: C_Ciudades [] = [];
  sectData: C_Sectores [] = [];

  constructor(
    private comData: CommunicationDataService,
    private visible: CommunicationVisibleService
  ){}
  ngOnInit():void{
    this.visible.visibleItemT$.subscribe(operationId =>{
      this.visibleDivId = operationId;
    });
    this.comData.dTISE$.subscribe(data => {
      this.tiseData = data;
    });
    this.comData.dRed$.subscribe(data => {
      this.redtData = data;
    });
    this.comData.dPlan$.subscribe(data => {
      this.planData = data;
    });
    this.comData.dProv$.subscribe(data => {
      this.provData = data; 
    });
    this.comData.dCity$.subscribe(data => {
      this.cityData = data;
    });
    this.comData.dSect$.subscribe(data => {
      this.sectData = data;
    });
  }

}
