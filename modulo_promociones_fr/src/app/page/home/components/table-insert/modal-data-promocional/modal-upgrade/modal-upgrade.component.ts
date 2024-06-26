import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { DataPromocionInformationService } from '../../../../../../services/subscribeData/data-promocion-information.service';
import { DataViewService } from '../../../../../../services/subscribeData/data-view.service';
import { Upgrade } from '../../../../../../interfaces/DataPromocional/upgrade.interface';

@Component({
  selector: 'app-modal-upgrade',
  standalone: true,
  imports: [CommonModule, FormsModule,],
  templateUrl: './modal-upgrade.component.html',
  styleUrl: './modal-upgrade.component.scss'
})
export class ModalUpgradeComponent implements OnInit {

  rowId: number = 0;   rowData: any = {};
  up_state: boolean = false;
  upgradeData: Upgrade [][] = [];

  //Dicionario de datos
  diccionario: { [key: string]: any }[] = [];
  
  constructor(
    private data_views: DataViewService,
    private data_information: DataPromocionInformationService,
  ){}

  ngOnInit(): void {
    this.data_views.dIndex$.subscribe( data => {this.rowId = data});
    this.data_views.dRows$.subscribe( data => {if(data)this.rowData = data});
    this.data_views.dModalViewUP$.subscribe( data => {this.up_state = data});
    this.data_information.dUpgrade$.subscribe( data => {this.upgradeData = data});
    this.data_information.dDiccionario$.subscribe( data => {this.diccionario = data});
    
  }

  closeModalDatosPromocionales(): void {
    this.data_views.stateModalUP(false);
  }

  getUpgradeCaducidadMIiMf(Upgrade: number, FechaCaducidad: Date, MesInicio: string, MesFinalizacion: string): void {
    if(Upgrade && FechaCaducidad && MesInicio && (!MesFinalizacion || MesFinalizacion =='')){
      this.diccionario[this.rowId]['UPGRADE'] = Upgrade;
      this.diccionario[this.rowId]['Fecha de Caducidad UPGRADE'] = FechaCaducidad.toString();
      this.diccionario[this.rowId]['Mes Inicio UPGRADE'] = MesInicio;
      this.diccionario[this.rowId]['Mes Fin UPGRADE'] = 'SIEMPRE';
      this.data_information.sendDataUptadeDiccionario(this.diccionario[this.rowId], this.rowId);
    } else if (Upgrade && FechaCaducidad && MesInicio && MesFinalizacion){
      this.diccionario[this.rowId]['UPGRADE'] = Upgrade;
      this.diccionario[this.rowId]['Fecha de Caducidad UPGRADE'] = FechaCaducidad.toString();
      this.diccionario[this.rowId]['Mes Inicio UPGRADE'] = MesInicio;
      this.diccionario[this.rowId]['Mes Fin UPGRADE'] = MesFinalizacion;
      this.data_information.sendDataUptadeDiccionario(this.diccionario[this.rowId], this.rowId);
    }
  }
}
