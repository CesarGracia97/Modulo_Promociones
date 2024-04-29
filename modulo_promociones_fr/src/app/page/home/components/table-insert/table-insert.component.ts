import { CommonModule } from '@angular/common';
import { Component, Input, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Servicios } from '../../../../interfaces/planes/servicios.interface';
import { TipoServicios } from '../../../../interfaces/planes/tiposervicios.interface';
import { Tecnologias } from '../../../../interfaces/planes/tecnologias.interface';
import { Ciudades } from '../../../../interfaces/places/ciudad.interface';
import { Provincias } from '../../../../interfaces/places/provincias.interface';
import { TariffPlanesVariant } from '../../../../interfaces/planes/tariffplanes.interface';
import { CommunicationDataService } from '../../../../services/communication/communicationData.service';
import { Buro } from '../../../../interfaces/financial/buro.interface';
import { ModosPago } from '../../../../interfaces/financial/modos-pago.interface';
import { Sectores } from '../../../../interfaces/places/sector.interface';
import { FdCombosService } from '../../../../services/fetchData/fd-combos.service';
import { FdPlacesService } from '../../../../services/fetchData/fd-places.service';
import { FdModospagosService } from '../../../../services/fetchData/fd-modospagos.service';

@Component({
  selector: 'app-table-insert',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './table-insert.component.html',
  styleUrl: './table-insert.component.scss'
})
export class TableInsertComponent implements OnInit  {  

  _V1: string = ''; _V2: string = ''; _V3: string = ''; _V4: string = ''; _V5: string = ''; _V6: string = '';
  _V7: string = ''; _V8: string = ''; _V9: string = '';
  @Input() rows: any[] = []; // Arreglo para almacenar las filas y sus datos
  //v. Estructura de datos
  serviciosData: Servicios[] = [];
  tiposervicioData: TipoServicios[] = [];
  redData: Tecnologias[][] = [];
  planData: TariffPlanesVariant[][] = [];
  provinciaData: Provincias[][] = [];
  ciudadData: Ciudades[][] = [];
  sectoresData: Sectores[] = [];
  buroData: Buro[] = [];
  modoPagosData: ModosPago[][] = [];

  showDropDown: boolean[] = []; 
  closing: boolean = false;

  modalVisible: boolean = false;
  selectedRowId: number = 0;
 
  constructor(
    private comData: CommunicationDataService,
    private fdpl: FdPlacesService,
    private fdcb: FdCombosService,
    private fdmp: FdModospagosService,
  ){}

  ngOnInit(): void {
    this.addRow(); // Añade la primera fila automáticamente al cargar
    this.comData.dServicios$.subscribe(data => {this.serviciosData = data;});
    this.comData.dTipoServicios$.subscribe(data => {this.tiposervicioData = data;});
    this.comData.dBuro$.subscribe(data => {this.buroData = data;});
  }

  addRow(): void {
    const newRow = {
      id: this.rows.length + 1,
      _V1: '',
      _V2: '',
      _V3: '',
      _V4: '',
      _V5: '',
      _V6: '',
      _V7: '',
      redData: [],
      planData: [],
      provinciaData: [],
      ciudadData: []
    };
    this.rows.push(newRow); // Añade el nuevo objeto al array de filas
    this.redData.push([]); // Inicializar redData específico para la nueva fila
    this.planData.push([]);
    this.provinciaData.push([]);
    this.ciudadData.push([]);
    this.showDropDown.push(false); // Agrega un estado inicial para el nuevo dropdown
    this.getModoPagosData(this.rows.length - 1);
  }

  getDataREDT(value1: string, value2: string, index: number): void {
    try{
      if(value1 && value2){
        console.log("Todos los selectores RED han sido seleccionados. Enviando los datos...");
        this.fdcb.getComboRED_RETURN(value1, value2).subscribe((red: Tecnologias[]) => {
          this.redData[index] = red;
        });
      }
    } catch(error){
      console.log("Error Detectado: ",error)
    }
  }

  getDataPLAN(value1: string, value2:string, value3: string, index: number): void {
    try{
      if(value1 && value2 && value3){
        this.fdcb.getComboPLAN_RETURN(value1, value2, value3).subscribe((plan: TariffPlanesVariant[]) => {
          this.planData[index] = plan;
        })
      }
    } catch (error) {
      console.log("Error detectado: ",error)
    }
  }

  getDataProvincias(tecnologias: string, tariffPlanesVariantID: string, index: number): void {
    try{
      if(tecnologias && tariffPlanesVariantID){
        if(tecnologias && tariffPlanesVariantID){
          this.fdpl.fetchDataProvinciasXTecnologiaXTariffplanVariant_RETURN(tecnologias, parseInt(tariffPlanesVariantID))
          .subscribe((prv: Provincias[]) => {
            this.provinciaData[index] = prv;
          });
        }
      }
    }  catch (error) {
      console.log("Error detectado: ",error)
    }
  }

  getModoPagosData(index: number): void {
    this.fdmp.fetchDataModosPago_RETURN().subscribe((modosPago) => {
      this.modoPagosData[index] = modosPago;
    });
  }
  
  getCiudadesxTT(tecnologia: string, tariffplanvariant: number, id_Prov: number, index: number): void {
    console.log("Tecn: ",tecnologia);
    console.log("tarf: ",tariffplanvariant);
    console.log("IdProv: ",id_Prov);
    if( id_Prov && tecnologia && tariffplanvariant){
      this.fdpl.fetchDataCiudadXTecnologiaXTariffplanVariant_RETURN(id_Prov, tecnologia, tariffplanvariant).subscribe((ciudades) => {
        this.ciudadData[index] = ciudades;
      });
    }
  }

  buttton_V1_V7(row: any, index: number): boolean {
    const hasBasicFields = row._V1 && row._V2 && row._V3 && row._V4 && row._V6 && row._V7;
    const hasSelectedPaymentMethod = this.modoPagosData[index] && this.modoPagosData[index].some(mdpg => mdpg.selected);
    return hasBasicFields && hasSelectedPaymentMethod;
  }

  toggleDropDown(index: number) {
    if (this.showDropDown) {
      this.closing = true;// Si está abierto y se va a cerrar, activa la transición rápida
      setTimeout(() => {
        this.showDropDown[index] = !this.showDropDown[index];
        this.closing = false;
      }, 30); // Espera el tiempo de la transición de cierre
    }
  }
  
  checkSDLoading() {
    return this.serviciosData.length === 0;
  }
  
  checkTSDLoading() {
    return this.tiposervicioData.length === 0;
  }

  checkPDLoading() {
    return this.provinciaData.length === 0;
  }

  checkBDLoading(){
    return this.buroData.length === 0;
  }

  checkMPDLoading(){
    return this.modoPagosData.length === 0;
  }

  openModal(rowId: number): void {
    this.selectedRowId = rowId;
    this.modalVisible = true;
}

closeModal(): void {
    this.modalVisible = false;
}
}