import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import { PrecioRegular } from '../../interfaces/DataPromocional/precio-regular.interface';
import { TariffPlanesVariant } from '../../interfaces/planes/tariffplanes.interface';
import { Productos } from '../../interfaces/planes/productos.interface';

@Injectable({
  providedIn: 'root'
})
export class DataProdadicInformationService {

  private planVSData: TariffPlanesVariant[][][] = []; private planVTFData: TariffPlanesVariant[][] = []; private planVTVData: TariffPlanesVariant[][] = [];
  private modeloRTData: Productos[][] = [];
  private precioRegularSTData: PrecioRegular[][][] = []; private precioRegularTFData: PrecioRegular[][] = [];
  private precioRegularTVData: PrecioRegular[][] = []; private precioRegularRTData: PrecioRegular[][] = [];
  private cantidadTF: number[][] = []; private cantidadTV: Number[][] = [];  private cantidadRT: Number[][] = [];
  private mesesST: Number[][][] = []; private mesesTF: Number[][] = []; private mesesTV: Number[][] = []; private mesesRT: Number[][] = [];

  private dPaquetesStreaming_Subject = new Subject<TariffPlanesVariant[][][]>();
  dPaquetesStreaming$ = this.dPaquetesStreaming_Subject.asObservable();

  private dPlanesTelefonicos_Subject = new Subject<TariffPlanesVariant[][]>();
  dPlanesTelefonicos$ = this.dPlanesTelefonicos_Subject.asObservable();

  private dPlanesTelevisivos_Subject = new Subject<TariffPlanesVariant[][]>();
  dPlanesTelevisivos$ = this.dPlanesTelevisivos_Subject.asObservable();

  private dModelosRouter_Subject = new Subject<Productos[][]>();
  dModelosRouter$ = this.dModelosRouter_Subject.asObservable();

  private dPrRegST_Subject = new Subject<PrecioRegular[][][]>();
  dPrRegST$ = this.dPrRegST_Subject.asObservable();

  private dPrRefTF_Subject = new Subject<PrecioRegular[][]>();
  dPrRefTF$ = this.dPrRefTF_Subject.asObservable();

  private dPrRefTV_Subject = new Subject<PrecioRegular[][]>();
  dPrRefTV$ = this.dPrRefTV_Subject.asObservable();

  private dPrRefRT_Subject = new Subject<PrecioRegular[][]>();
  dPrRefRT$ = this.dPrRefRT_Subject.asObservable();

  private dCantTF_Subject = new Subject<Number[][]>();
  dCantTF$  = this.dCantTF_Subject.asObservable();

  private dCantTV_Subject = new Subject<Number[][]>();
  dCantTV$  = this.dCantTV_Subject.asObservable();

  private dCantRT_Subject = new Subject<Number[][]>();
  dCantRT$  = this.dCantRT_Subject.asObservable();

  private dMesST_Subject = new Subject<Number[][][]>();
  dMesST$ = this.dMesST_Subject.asObservable();

  private dMesTF_Subject = new Subject<Number[][]>();
  dMesTF$ = this.dMesTF_Subject.asObservable();

  private dMesTV_Subject = new Subject<Number[][]>();
  dMesTV$ = this.dMesTV_Subject.asObservable();

  private dMesRT_Subject = new Subject<Number[][]>();
  dMesRT$ = this.dMesRT_Subject.asObservable();

  constructor() { }
  
  senDataPaquetesPlanes(data: TariffPlanesVariant[], index: number, table: number, type: string){
    if(type == "TELEFONIA"){
      if(!this.planVTFData[index]){
        this.planVTFData[index] = [];
        this.planVTFData[index].push(...data);
        this.dPlanesTelefonicos_Subject.next(this.planVTFData);
      } else {
        console.log("En esta posicion ya existe un dato");
      }
    }else if(type == "TELEVISION"){
      if(!this.planVTVData[index]){
        this.planVTVData[index] = [];
        this.planVTVData[index].push(...data);
        this.dPlanesTelevisivos_Subject.next(this.planVTVData);
      } else {
        console.log("En esta posicion ya existe un dato");
      }
    }else if(type == "STREAMING"){
      if(!this.planVSData[index][table]){
        this.planVSData[index][table] = [];
        this.planVSData[index][table].push(...data);
        this.dPaquetesStreaming_Subject.next(this.planVSData);
      } else {
        console.log("En esta posicion ya existe un dato");
      }
    }
  }

  sendDataModelosRouter(data: Productos[], index: number){
    if(!this.modeloRTData[index]){
      this.modeloRTData[index] = [];
      this.modeloRTData[index].push(...data);
      this.dModelosRouter_Subject.next(this.modeloRTData);
    } else {
      console.log("En esta posicion ya existe un dato");
    }
  }

  sendDataPreciosPA(data: PrecioRegular[], index: number, tabla: number, type: string){
    if(type == "TELEFONIA"){
      if(!this.precioRegularTFData[index]){
        this.precioRegularTFData[index] = [];
        this.precioRegularTFData[index].push(...data);
        this.dPrRefTF_Subject.next(this.precioRegularTFData);
      }
    }else if(type == "TELEVISION"){
      if(!this.precioRegularTVData[index]){
        this.precioRegularTVData[index] = [];
        this.precioRegularTVData[index].push(...data);
        this.dPrRefTV_Subject.next(this.precioRegularTVData);
      }
    }else if(type == "ROUTER"){
      if(!this.precioRegularRTData[index]){
        this.precioRegularRTData[index] = [];
        this.precioRegularRTData[index].push(...data);
        this.dPrRefRT_Subject.next(this.precioRegularRTData);
      }
    }else if(type == "STREAMING"){
      if(!this.precioRegularSTData[index][tabla]){
        this.precioRegularSTData[index][tabla] = [];
        this.precioRegularSTData[index][tabla].push(...data);
        this.dPrRegST_Subject.next(this.precioRegularSTData);
      }
    }
  }

  sendDataCantidad(data: number, index: number, type: string){
    if(type == "TELEFONIA"){
      if(!this.cantidadTF[index]){
        this.cantidadTF[index] = [];
        this.cantidadTF[index].push(data);
        this.dCantTV_Subject.next(this.cantidadTF);
      }
    }else if (type == "TELEVISION"){
      if(!this.cantidadTV[index]){
        this.cantidadTV[index] = [];
        this.cantidadTV[index].push(data);
        this.dCantTV_Subject.next(this.cantidadTV);
      }
    }else if (type == "ROUTER"){
      if(!this.cantidadRT[index]){
        this.cantidadRT[index] = [];
        this.cantidadRT[index].push(data);
        this.dCantRT_Subject.next(this.cantidadRT);
      }
    }
  }

  sendDataMes(data: number, index: number, tabla: number, type: string){
    if(type == "STREAMING"){
      if(!this.mesesST[index][tabla]){
        this.mesesST[index][tabla] = [];
        this.mesesST[index][tabla].push(data);
        this.dMesST_Subject.next(this.mesesST);
      }
    }else if(type == "TELEFONIA"){
      if(!this.mesesTF[index]){
        this.mesesTF[index] = [];
        this.mesesTF[index].push(data);
        this.dMesTF_Subject.next(this.mesesTF);
      }
    }else if (type == "TELEVISION"){
      if(!this.mesesTV[index]){
        this.mesesTV[index] = [];
        this.mesesTV[index].push(data);
        this.dMesTV_Subject.next(this.mesesTV);
      }
    }else if (type == "ROUTER"){
      if(!this.mesesRT[index]){
        this.mesesRT[index] = [];
        this.mesesRT[index].push(data);
        this.dMesRT_Subject.next(this.mesesRT);
      }
    }
  }
}
