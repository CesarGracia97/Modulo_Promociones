import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import { TipoServicios } from '../../interfaces/planes/tiposervicios.interface';
import { Tecnologias } from '../../interfaces/planes/tecnologias.interface';
import { TariffPlanes, TariffPlanesVariant } from '../../interfaces/planes/tariffplanes.interface';
import { Provincias } from '../../interfaces/places/provincias.interface';
import { C_Ciudades, C_Sectores } from '../../interfaces/planes/combos.interface';
import { Servicios } from '../../interfaces/planes/servicios.interface';
import { Ciudades } from '../../interfaces/places/ciudad.interface';
import { Sectores } from '../../interfaces/places/sector.interface';
import { Buro } from '../../interfaces/financial/buro.interface';
import { ModosPago } from '../../interfaces/financial/modos-pago.interface';
import { DiasGozados } from '../../interfaces/DataPromocional/dias-gozados.interface';
import { Productos } from '../../interfaces/planes/productos.interface';
import { PrecioRegular } from '../../interfaces/DataPromocional/precio-regular.interface';
import { Upgrade } from '../../interfaces/DataPromocional/upgrade.interface';

@Injectable({
  providedIn: 'root'
})
export class CommunicationDataService {
  private planData: TariffPlanes[][] = [];
  private planVData: TariffPlanesVariant[][] = [];
  private prodData: Productos[][] = [];
  private mdpgData: ModosPago[][] = [];
  private buroData: Buro[][] = [];
  private provinciaData: Provincias[][] = [];
  private ciudadData: Ciudades[][] = [];
  private sectoresData: Sectores[][] = [];
  private diasGozadosData: DiasGozados[][] = [];
  private precioRegularData: PrecioRegular[][] = [];
  private upgradeData: Upgrade [][] = [];


  private dServicios_Subject = new Subject<Servicios[]>();
  dServicios$ = this.dServicios_Subject.asObservable();

  private dPLAN_Subject = new Subject<TariffPlanes[][]>();
  dPlan$ = this.dPLAN_Subject.asObservable();

  private dPLANVARIANT_Subject = new Subject<TariffPlanesVariant[][]>();
  dPlanV$ = this.dPLANVARIANT_Subject.asObservable();

  private dPRODUCTO_Subject = new Subject<Productos[][]>();
  dProductos$ = this.dPRODUCTO_Subject.asObservable();

  private dBuro_Subject = new Subject<Buro[][]>();
  dBuro$ = this.dBuro_Subject.asObservable();

  private dModoPago_Subject = new Subject<ModosPago[][]>();
  dModoPago$ = this.dModoPago_Subject.asObservable();

  private dProvincias_Subject = new Subject<Provincias[][]>();
  dProvincias$ = this.dProvincias_Subject.asObservable();

  private dCiudades_Subject = new Subject<Ciudades[][]>();
  dCiudades$ = this.dCiudades_Subject.asObservable();

  private dSectores_Subject = new Subject<Sectores[][]>();
  dSectores$ = this.dSectores_Subject.asObservable();

  private dPrecioRegular_Subject = new Subject<PrecioRegular[][]>();
  dPrecioRegular$ = this.dPrecioRegular_Subject.asObservable();

  private dDiasGozados_Subject = new Subject<DiasGozados[][]>();
  dDiasGozados$ = this.dDiasGozados_Subject.asObservable();

  private dUpgrade_Subject = new Subject<Upgrade[][]>();
  dUpgrade$ = this.dUpgrade_Subject.asObservable();

  private dPaquetesStreaming_Subject = new Subject<TariffPlanesVariant[][]>();
  dPaquetesStreaming$ = this.dPaquetesStreaming_Subject.asObservable();

  private dPlanesTelefonicos_Subject = new Subject<TariffPlanesVariant[][]>();
  dPlanesTelefonicos$ = this.dPlanesTelefonicos_Subject.asObservable();

  private dPlanesTelevisivos_Subject = new Subject<TariffPlanesVariant[][]>();
  dPlanesTelevisivos$ = this.dPlanesTelevisivos_Subject.asObservable();

  constructor() { }

  sendDataServicio(data: Servicios[]){
    this.dServicios_Subject.next(data);
  }

  sendDataPLAN(data: TariffPlanes[], index: number){
    this.planData[index] = data;
    this.dPLAN_Subject.next(this.planData);
  }

  sendDataPLANVARIANT(data: TariffPlanesVariant[], index: number){
    this.planVData[index] = data;
    this.dPLANVARIANT_Subject.next(this.planVData);
  }

  sendDataPRODUCTO(data: Productos[], index: number){
    this.prodData[index] = data;
    this.dPRODUCTO_Subject.next(this.prodData)
  }

  sendDataBuro(data: Buro[], index: number){
    this.buroData[index] = data;
    this.dBuro_Subject.next(this.buroData);
  }

  sendDataModosPago(data: ModosPago[], index: number){
    this.mdpgData[index] = data;
    this.dModoPago_Subject.next(this.mdpgData);
  }

  sendDataProvincias(data: Provincias[], index: number){
    this.provinciaData[index] = data;
    this.dProvincias_Subject.next(this.provinciaData);
  }

  sendDataCiudades(data: Ciudades[], index: number){
    this.ciudadData[index] = data;
    this.dCiudades_Subject.next(this.ciudadData);
  }
  
  sendDataSectores(data: Sectores[], index: number){
    this.sectoresData[index] = data;
    this.dSectores_Subject.next(this.sectoresData);
  }

  sendDataPrecioRegular(data: PrecioRegular[], index: number){
    this.precioRegularData[index] = data;
    this.dPrecioRegular_Subject.next(this.precioRegularData)
  }

  sendDataDiasGozados(data: DiasGozados[], index: number){
    this.diasGozadosData[index] = data;
    this.dDiasGozados_Subject.next(this.diasGozadosData);
  }

  sendDataUPGRADE(data: Upgrade[], index: number){
    this.upgradeData[index] = data;
    this.dUpgrade_Subject.next(this.upgradeData);
  }

  senDataPaquetesStreaming(data: TariffPlanesVariant[], index: number){
    this.planVData[index] = data;
    this.dPaquetesStreaming_Subject.next(this.planVData);
  }

  sendDataPlanesTelefonicos(data: TariffPlanesVariant[], index: number){
    this.planVData[index] = data;
    this.dPlanesTelefonicos_Subject.next(this.planVData);
  }

  sendDataPlanesTelevisivos(data: TariffPlanesVariant[], index: number){
    this.planVData[index] = data;
    this.dPlanesTelevisivos_Subject.next(this.planVData);
  }
}
