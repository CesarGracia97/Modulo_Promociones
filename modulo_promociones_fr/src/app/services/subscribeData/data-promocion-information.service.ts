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
import { Entidades } from '../../interfaces/financial/entidades.interface';
import { Tarjetas } from '../../interfaces/financial/tarjetas.interface';

@Injectable({
  providedIn: 'root'
})

export class DataPromocionInformationService {
  private NombrePromocion: string[][] = [];
  private FechaInicioPromocion: Date[][] = []; private FechaFinPromocion: Date[][] = [];
  private planData: TariffPlanes[][] = []; private planVData: TariffPlanesVariant[][] = [];
  private canalData: Number[][] = [];
  private entidadesData: Entidades[][] = []; private tarjetasData: Tarjetas[][] = [];
  private prodData: Productos[][] = [];
  private mdpgData: ModosPago[][] = [];
  private buroData: Buro[][] = [];
  private provinciaData: Provincias[][] = []; private ciudadData: Ciudades[][] = []; private sectoresData: Sectores[][] = [];
  private diasGozadosData: DiasGozados[][] = [];
  private precioRegularData: PrecioRegular[][] = []; private precioPromocional: Number [][] = [];
  private upgradeData: Upgrade [][] = [];
  private mesInicioPromo: Number [][] = [];
  private mesFinPromo: Number [][] = [];

  private dNombrePromocion_Subject = new Subject<String[][]>();
  dNombrePromocion$ = this.dNombrePromocion_Subject.asObservable();

  private dFechaInicioPromocion_Subject  = new Subject<Date[][]>();
  dFechaInicioPromocion$ = this.dFechaInicioPromocion_Subject.asObservable();

  private dFechaFinPromocion_Subject  = new Subject<Date[][]>();
  dFechaFinPromocion$ = this.dFechaFinPromocion_Subject.asObservable();
  
  private dServicios_Subject = new Subject<Servicios[]>();
  dServicios$ = this.dServicios_Subject.asObservable();

  private dCanal_Subject = new Subject<Number[][]>();
  dCanal$ = this.dCanal_Subject.asObservable();

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

  private dEntidades_Subject = new Subject<Entidades[][]>();
  dEntidades$ = this.dEntidades_Subject.asObservable();

  private dTarjetas_Subject = new Subject<Tarjetas[][]>();
  dTarjetas$ = this.dTarjetas_Subject.asObservable();

  private dProvincias_Subject = new Subject<Provincias[][]>();
  dProvincias$ = this.dProvincias_Subject.asObservable();

  private dCiudades_Subject = new Subject<Ciudades[][]>();
  dCiudades$ = this.dCiudades_Subject.asObservable();

  private dSectores_Subject = new Subject<Sectores[][]>();
  dSectores$ = this.dSectores_Subject.asObservable();

  private dPrecioRegular_Subject = new Subject<PrecioRegular[][]>();
  dPrecioRegular$ = this.dPrecioRegular_Subject.asObservable();

  private dPrecioPromo_Subject = new Subject<Number[][]>();
  dPrecioPromo$ = this.dPrecioPromo_Subject.asObservable();

  private dDiasGozados_Subject = new Subject<DiasGozados[][]>();
  dDiasGozados$ = this.dDiasGozados_Subject.asObservable();

  private dUpgrade_Subject = new Subject<Upgrade[][]>();
  dUpgrade$ = this.dUpgrade_Subject.asObservable();

  private dMesInicioPromo_Subject = new Subject<Number[][]>();
  dMesInicioPromo$ = this.dMesInicioPromo_Subject.asObservable();

  private dMesFinPromo_Subject = new Subject<Number[][]>();
  dMesFinPromo$ = this.dMesFinPromo_Subject.asObservable();

  constructor() { }

  sendDataNombrePromo(data: string, index: number){
    if(!this.NombrePromocion[index]){
      this.NombrePromocion[index] = [];
      this.NombrePromocion[index].push(data);
      this.dNombrePromocion_Subject.next(this.NombrePromocion);
    }else{
      console.log("En esta posicion ya existe un dato");
    }
  }

  sendDataFechas(data: Date, index: number, type: string){
    if(type == "INICIO"){
      if(!this.FechaInicioPromocion[index]){
        this.FechaInicioPromocion[index] = [];
        this.FechaInicioPromocion[index].push(data);
        this.dFechaInicioPromocion_Subject.next(this.FechaInicioPromocion);
      }
    }else if(type == "FIN"){
      if(!this.FechaFinPromocion[index]){
        this.FechaFinPromocion[index] = [];
        this.FechaFinPromocion[index].push(data);
        this.dFechaFinPromocion_Subject.next(this.FechaFinPromocion);
      }else{
        console.log("En esta posicion ya existe un dato");
      }
    }
  }

  sendDataServicio(data: Servicios[]){
    this.dServicios_Subject.next(data);
  }

  sendDataPLAN(data: TariffPlanes[], index: number){
    if (!this.planData[index]) {
      this.planData[index] = [];
      this.planData[index].push(...data);
      this.dPLAN_Subject.next(this.planData);
    } else {
      console.log("En esta posicion ya existe un dato");
    }
  }

  sendDataPLANVARIANT(data: TariffPlanesVariant[], index: number){
    if(!this.planVData[index]){
      this.planVData[index] = [];
      this.planVData[index].push(...data);
      this.dPLANVARIANT_Subject.next(this.planVData);
    } else {
      console.log("En esta posicion ya existe un dato");
    }
  }

  sendDataCanal(data: number, index: number){
    if(!this.canalData[index]){
      this.canalData[index] = [];
      this.canalData[index].push(data);
      this.dCanal_Subject.next(this.canalData);
    } else {
      console.log("En esta posicion ya existe un dato");
    }
  }

  sendDataPRODUCTO(data: Productos[], index: number){
    if(!this.prodData[index]){
      this.prodData[index] = [];
      this.prodData[index].push(...data);
      this.dPRODUCTO_Subject.next(this.prodData)
    } else {
      console.log("En esta posicion ya existe un dato");
    }
  }

  sendDataBuro(data: Buro[], index: number){
    if(!this.buroData[index]){
      this.buroData[index] = [];
      this.buroData[index].push(...data);
      this.dBuro_Subject.next(this.buroData);
    } else {
      console.log("En esta posicion ya existe un dato");
    }
  }

  sendDataModosPago(data: ModosPago[], index: number){
    if(!this.mdpgData[index]){
      this.mdpgData[index] = [];
      this.mdpgData[index].push(...data);
      this.dModoPago_Subject.next(this.mdpgData);
    } else {
      console.log("En esta posicion ya existe un dato");
    }
  }

  sendDataEntidades(data: Entidades[], index: number){
    if(!this.entidadesData[index]){
      this.entidadesData[index] = [];
      this.entidadesData[index].push(...data);
      this.dTarjetas_Subject.next(this.entidadesData);
    } else {
      console.log("En esta posicion ya existe un dato");
    }
  }

  sendDataTarjetas(data: Tarjetas[], index: number){
    if(!this.tarjetasData[index]){
      this.tarjetasData[index] = [];
      this.tarjetasData[index].push(...data);
    } else {
      console.log("En esta posicion ya existe un dato");
    }
  }

  sendDataProvincias(data: Provincias[], index: number){
    if(!this.provinciaData[index]){
      this.provinciaData[index] = [];
      this.provinciaData[index].push(...data);
      this.dProvincias_Subject.next(this.provinciaData);
    } else {
      console.log("En esta posicion ya existe un dato");
    }
  }

  sendDataCiudades(data: Ciudades[], index: number){
    if(!this.ciudadData[index]){
      this.ciudadData[index] = [];
      this.ciudadData[index].push(...data);
      this.dCiudades_Subject.next(this.ciudadData);
    } else {
      console.log("En esta posicion ya existe un dato");
    }
  }
  
  sendDataSectores(data: Sectores[], index: number){
    if(!this.sectoresData[index]){
      this.sectoresData[index] = [];
      this.sectoresData[index].push(...data);
      this.dSectores_Subject.next(this.sectoresData);
    } else {
      console.log("En esta posicion ya existe un dato");
    }
  }

  sendDataPrecioRegular(data: PrecioRegular[],index: number){
    if(!this.precioRegularData[index]){
      this.precioRegularData[index] = [];
      this.precioRegularData[index].push(...data);
      this.dPrecioRegular_Subject.next(this.precioRegularData)
    } else {
      console.log("En esta posicion ya existe un dato");
    }
  }

  sendDataPrecioPromo(data: number, index: number){
    if(!this.precioPromocional[index]){
      this.precioPromocional[index] = [];
      this.precioPromocional[index].push(data);
      this.dPrecioPromo_Subject.next(this.precioPromocional);
    } else {
      console.log("En esta posicion ya existe un dato");
    }
  }

  sendDataDiasGozados(data: DiasGozados[], index: number){
    if(!this.diasGozadosData[index]){
      this.diasGozadosData[index] = [];
      this.diasGozadosData[index].push(...data);
      this.dDiasGozados_Subject.next(this.diasGozadosData);
    } else {
      console.log("En esta posicion ya existe un dato");
    }
  }

  sendDataUPGRADE(data: Upgrade[], index: number){
    if(!this.upgradeData[index]) {
      this.upgradeData[index] = [];
      this.upgradeData[index].push(...data);
      this.dUpgrade_Subject.next(this.upgradeData);
    } else {
      console.log("En esta posicion ya existe un dato");
    }
  }

  sendDataMesPromocion(data: number, index: number, type: string){
    if(type == "INICIO"){
      if(!this.mesInicioPromo[index]){
        this.mesInicioPromo[index] = [];
        this.mesInicioPromo[index].push(data);
        this.dMesInicioPromo_Subject.next(this.mesInicioPromo);
      } else {
        console.log("En esta posicion ya existe un dato");
      }
    } else if (type == "FIN"){
      if(!this.mesFinPromo[index]){
        this.mesFinPromo[index] = [];
        this.mesFinPromo[index].push(data);
        this.dMesFinPromo_Subject.next(this.mesFinPromo);
      } else {
        console.log("En esta posicion ya existe un dato");
      }
    }
  }
}
