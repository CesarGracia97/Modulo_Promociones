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
import { FdBuroService } from '../../../../services/fetchData/fd-buro.service';
import { SectorService } from '../../../../services/requests/places/sector.service';

@Component({
  selector: 'app-table-insert',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './table-insert.component.html',
  styleUrl: './table-insert.component.scss'
})
export class TableInsertComponent implements OnInit  {  

  _V1: string = ''; _V2: string = ''; _V3: string = ''; _V4: string = '';
  _V5: string = ''; _V8: string = ''; _V9: string = '';
  @Input() rows: any[] = []; // Arreglo para almacenar las filas y sus datos
  //v. Estructura de datos
  serviciosData: Servicios[] = [];
  tiposervicioData: TipoServicios[][] = [];
  redData: Tecnologias[][] = [];
  planData: TariffPlanesVariant[][] = [];
  provinciaData: Provincias[][] = [];
  ciudadData: Ciudades[][] = [];
  sectoresData: Sectores[] = [];
  buroData: Buro[][] = [];
  modoPagosData: ModosPago[][] = [];

  showMDPDD: boolean[] = []; 
  showBDD: boolean[] = [];
  closing: boolean = false;

  modalVisible: boolean = false;
  selectedRowId: number = 0;
 
  constructor(
    private comData: CommunicationDataService,
    private fdpl: FdPlacesService,
    private fdcb: FdCombosService,
    private fdmp: FdModospagosService,
    private fdb: FdBuroService,
    private fdsect: SectorService
  ){}

  ngOnInit(): void {
    this.addRow(); // Añade la primera fila automáticamente al cargar
    this.comData.dServicios$.subscribe(data => {this.serviciosData = data;});
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
      tiposervicioData: [],
      redData: [],
      planData: [],
      provinciaData: [],
      ciudadData: []
    };
    this.rows.push(newRow); // Añade el nuevo objeto al array de filas
    this.tiposervicioData.push([]);
    this.redData.push([]); // Inicializar redData específico para la nueva fila
    this.planData.push([]);
    this.provinciaData.push([]);
    this.ciudadData.push([]);
    this.showMDPDD.push(false); // Agrega un estado inicial para el nuevo dropdown
    this.getModoPagosData(this.rows.length - 1);
    this.getBuroData(this.rows.length - 1)
  }

  getDataTISE(value1: string, index: number): void {
    try{
      if(value1){
        this.fdcb.getComboTISE_RETURN(value1).subscribe((tise: TipoServicios[]) => {
          this.tiposervicioData[index] = tise;
        })
      }
    } catch(error) {
      console.log("Error Detectado: ",error)
    }
  }

  getDataREDT(value1: string, value2: string, index: number): void {
    try{
      if(value1 && value2){
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

  getModoPagosData(index: number): void {
    try{
      this.fdmp.fetchDataModosPago_RETURN().subscribe((modosPago) => {
        this.modoPagosData[index] = modosPago;
      });
    } catch (error) {
      console.log("Error detectado: ",error)
    }
  }

  getBuroData(index: number): void{
    try{
      this.fdb.fetchDataBuro_RETURN().subscribe((buro) => {
        this.buroData[index] = buro;
      });
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
  
  getCiudadesxTT(tecnologia: string, tariffplanvariant: number, id_Prov: number, index: number): void {
    if( id_Prov && tecnologia && tariffplanvariant){
      this.fdpl.fetchDataCiudadXTecnologiaXTariffplanVariant_RETURN(id_Prov, tecnologia, tariffplanvariant).subscribe((ciudades) => {
        this.ciudadData[index] = ciudades;
      });
    }
  }

  buscarSectores() {
    const index = this.selectedRowId - 1;
    const indexRow = this.rows[index];
    const _V3 = indexRow._V3;
    const _V4 = indexRow._V4;
    const ciudades = this.ciudadData[index].filter(city => city.selected).map(city => city.CIUDAD_ID);
    console.log("Tecnologia: "+_V3+" | Ciudades: "+ciudades+" | TFPV: "+_V4);
    this.fdsect.getSectoresMasivosXTecnologiaXTariffplanVariant(ciudades, _V3, _V4)
  }

  buttton_V1_V7(row: any, index: number): boolean {
    const trueSelect = row._V1 && row._V2 && row._V3 && row._V4 && row._V7;
    const trueMP = this.modoPagosData[index] && this.modoPagosData[index].some(mdpg => mdpg.selected);
    const trueB = this.buroData[index] && this.buroData[index].some(buro => buro.selected);
    return trueSelect && trueMP && trueB;
  }

  toggDDMP(index: number) {
    if (this.showMDPDD) {
      this.closing = true;// Si está abierto y se va a cerrar, activa la transición rápida
      setTimeout(() => {
        this.showMDPDD[index] = !this.showMDPDD[index];
        this.closing = false;
      }, 30); // Espera el tiempo de la transición de cierre
    }
  }

  toggDDB(index:number) {
    if (this.showBDD) {
      this.closing = true;// Si está abierto y se va a cerrar, activa la transición rápida
      setTimeout(() => {
        this.showBDD[index] = !this.showBDD[index];
        this.closing = false;
      }, 30); // Espera el tiempo de la transición de cierre
    }
  }
  
  checkSDLoading() {
    return this.serviciosData.length === 0;
  }

  openModal(rowId: number): void {
    this.selectedRowId = rowId;
    this.modalVisible = true;
  }

  closeModal(): void {
    this.modalVisible = false;
  }
}