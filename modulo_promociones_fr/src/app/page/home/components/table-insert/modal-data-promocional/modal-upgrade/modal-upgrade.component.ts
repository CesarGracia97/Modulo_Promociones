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
  errorM_V16: string[] = []; errorM_V17: string[] = [];

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

  getUpgradeCaducidadMIiMf(Upgrade: number, MesInicio: number, MesFinalizacion: string): void {
    this.validateV16(MesInicio);
    this.validateV17(parseInt(MesFinalizacion));
    if(Upgrade && MesInicio){
      this.diccionario[this.rowId]['UPGRADE'] = [];
      this.diccionario[this.rowId]['UPGRADE']['UPGRADE'] = Upgrade;
      this.diccionario[this.rowId]['UPGRADE']['Mes Inicio UPGRADE'] = MesInicio;
      if(!MesFinalizacion || MesFinalizacion ==''){
        this.diccionario[this.rowId]['UPGRADE']['Mes Fin UPGRADE'] = 'SIEMPRE';
      } else if (MesFinalizacion) {
        this.diccionario[this.rowId]['UPGRADE']['Mes Fin UPGRADE'] = MesFinalizacion;
      }
      this.data_information.sendDataUptadeDiccionario(this.diccionario[this.rowId], this.rowId);
    }
  }

  validateV16(value: number) {
    if (value < 0 || value > 24) {
      this.errorM_V16[this.rowId] = 'LIMITE SUPERADO 0-24';
    } else {
      this.errorM_V16[this.rowId] = '';
    }
  }

  validateV17(value: number) {
    if (value <= this.rowData._V16) {
      this.errorM_V17[this.rowId] = 'EL VALOR NO DEBE SER MENOR AL INICIAL';
    } else {
      this.errorM_V17[this.rowId]= '';
    }
  }
}
