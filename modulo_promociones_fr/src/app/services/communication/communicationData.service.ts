import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import { TipoServicios } from '../../interfaces/planes/tiposervicios.interface';
import { Tecnologias } from '../../interfaces/planes/tecnologias.interface';
import { TariffPlanesVariant } from '../../interfaces/planes/tariffplanes.interface';
import { Provincias } from '../../interfaces/places/provincias.interface';
import { C_Ciudades, C_Sectores } from '../../interfaces/planes/combos.interface';
import { Servicios } from '../../interfaces/planes/servicios.interface';
import { Ciudades } from '../../interfaces/places/ciudad.interface';
import { Sectores } from '../../interfaces/places/sector.interface';
import { Buro } from '../../interfaces/financial/buro.interface';
import { ModosPago } from '../../interfaces/financial/modos-pago.interface';

@Injectable({
  providedIn: 'root'
})
export class CommunicationDataService {

  //Variables de Comunicacion de datos entre componentes de Table Query
  //Variables de Comunicacion de datos Tipo Combo
  private dTISE_Subject = new Subject<TipoServicios[]>();
  dTISE$ = this.dTISE_Subject.asObservable();
  private dRED_Subject = new Subject<Tecnologias[]>();
  dRed$ = this.dRED_Subject.asObservable();
  private dPLAN_Subject = new Subject<TariffPlanesVariant[]>();
  dPlan$ = this.dPLAN_Subject.asObservable();
  private dPROV_Subject = new Subject<Provincias[]>();
  dProv$ = this.dPROV_Subject.asObservable();
  private dCITY_Subject = new Subject<C_Ciudades[]>();
  dCity$ = this.dCITY_Subject.asObservable();
  private dSECT_Subject = new Subject<C_Sectores[]>();
  dSect$ = this.dSECT_Subject.asObservable();

  //Variables de Comunicacion de datos Tipo Informacion.
  private dServicios_Subject = new Subject<Servicios[]>();
  dServicios$ = this.dServicios_Subject.asObservable();
  private dTipoServicios_Subject = new Subject<TipoServicios[]>();
  dTipoServicios$ = this.dTipoServicios_Subject.asObservable();
  private dTecnologias_Subject = new Subject<Tecnologias[]>();
  dTecnologias$ = this.dTecnologias_Subject.asObservable();
  private dPlanes_Subject = new Subject<TariffPlanesVariant[]>();
  dPlanes$ = this.dPlanes_Subject.asObservable();
  private dProvincias_Subject = new Subject<Provincias[]>();
  dProvincia$ = this.dProvincias_Subject.asObservable();
  private dCiudades_Subject = new Subject<Ciudades[]>();
  dCiudades$ = this.dCiudades_Subject.asObservable();
  private dSectores_Subject = new Subject<Sectores[]>();
  dSectores$ = this.dSectores_Subject.asObservable();

  //Variables de Comunicacion de datos Tipo Complemento
  private dBuro_Subject = new Subject<Buro[]>();
  dBuro$ = this.dBuro_Subject.asObservable();
  private dModoPago_Subject = new Subject<ModosPago[]>();
  dModoPago$ = this.dModoPago_Subject.asObservable();
  
  constructor() { }
  
  sendDataTISE(data: TipoServicios[]){
    this.dTISE_Subject.next(data);
  }

  sendDataRED(data: Tecnologias[]){
    this.dRED_Subject.next(data);
  }

  sendDataPLAN(data: TariffPlanesVariant[]){
    this.dPLAN_Subject.next(data);
  }

  sendDataPROV(data: Provincias[]){
    this.dPROV_Subject.next(data);
  }

  sendDataCITY(data: C_Ciudades[]){
    this.dCITY_Subject.next(data);
  }

  sendDataSECT(data: C_Sectores[]){
    this.dSECT_Subject.next(data);
  }

  sendDataServicio(data: Servicios[]){
    this.dServicios_Subject.next(data);
  }

  sendDataTipoServicios(data: TipoServicios[]){
    this.dTipoServicios_Subject.next(data);
  }

  sendDataTecnologias(data: Tecnologias[]){
    this.dTecnologias_Subject.next(data);
  }
  
  sendDataPlanes(data:TariffPlanesVariant[]){
    this.dPlanes_Subject.next(data);
  }

  sendDataProvincias(data: Provincias[]){
    this.dProvincias_Subject.next(data);
  }

  sendDataCiudades(data: Ciudades[]){
    this.dCiudades_Subject.next(data);
  }
  
  sendDataSectores(data: Sectores[]){
    this.dSectores_Subject.next(data);
  }

  sendDataBuro(data: Buro[]){
    this.dBuro_Subject.next(data);
  }

  sendDataModosPago(data: ModosPago[]){
    this.dModoPago_Subject.next(data);
  }
}
