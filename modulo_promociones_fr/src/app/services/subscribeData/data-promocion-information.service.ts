import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import { TariffPlanes, TariffPlanesVariant } from '../../interfaces/planes/tariffplanes.interface';
import { Provincias } from '../../interfaces/places/provincias.interface';
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
import { Canales } from '../../interfaces/financial/canales.interface';

@Injectable({
  providedIn: 'root'
})

export class DataPromocionInformationService {
  private NombrePromocion: string[][] = [];
  private FechaInicioPromocion: Date[][] = []; private FechaFinPromocion: Date[][] = [];
  private planData: TariffPlanes[][] = []; private planVData: TariffPlanesVariant[][] = [];
  private canalData: Canales[][] = [];
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
  /*------------------DICCIONARIO DE DATOS----------------------*/
  private diccionario: { [key: string]: any }[] = [];
  /*------------------DICCIONARIO DE DATOS----------------------*/


  private dNombrePromocion_Subject = new Subject<String[][]>();
  dNombrePromocion$ = this.dNombrePromocion_Subject.asObservable();

  private dFechaInicioPromocion_Subject  = new Subject<Date[][]>();
  dFechaInicioPromocion$ = this.dFechaInicioPromocion_Subject.asObservable();

  private dFechaFinPromocion_Subject  = new Subject<Date[][]>();
  dFechaFinPromocion$ = this.dFechaFinPromocion_Subject.asObservable();
  
  private dServicios_Subject = new Subject<Servicios[]>();
  dServicios$ = this.dServicios_Subject.asObservable();

  private dCanal_Subject = new Subject<Canales[][]>();
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

  /*----------------------------DICCIONARIO DE DATOS--------------------------------*/
  private dDiccionario_Subject = new Subject<{ [key: string]: any }[]>();
  dDiccionario$ = this.dDiccionario_Subject.asObservable();

  /*----------------------------DICCIONARIO DE DATOS--------------------------------*/

  constructor() { }

  sendDataNombrePromo(data: string, index: number){
    this.NombrePromocion[index] = [];
    this.NombrePromocion[index].push(data);
    this.dNombrePromocion_Subject.next(this.NombrePromocion);
  }

  sendDataFechas(data: Date, index: number, type: string){
    if(type == "INICIO"){
      this.FechaInicioPromocion[index] = [];
      this.FechaInicioPromocion[index].push(data);
      this.dFechaInicioPromocion_Subject.next(this.FechaInicioPromocion);
    }else if(type == "FIN"){
      this.FechaFinPromocion[index] = [];
      this.FechaFinPromocion[index].push(data);
      this.dFechaFinPromocion_Subject.next(this.FechaFinPromocion);
    }
  }

  sendDataServicio(data: Servicios[]){
    this.dServicios_Subject.next(data);
  }

  sendDataPLAN(data: TariffPlanes[], index: number){
    this.planData[index] = [];
    this.planData[index].push(...data);
    this.dPLAN_Subject.next(this.planData);
  }

  sendDataPLANVARIANT(data: TariffPlanesVariant[], index: number){
    this.planVData[index] = [];
    this.planVData[index].push(...data);
    this.dPLANVARIANT_Subject.next(this.planVData);
  }

  sendDataCanal(index: number){
    if(!this.canalData[index]){
      this.canalData[index] = [];
      this.canalData[index].push(...[
        {ID: 3, NAME: 'Comercial'},
        {ID: 4, NAME: 'Ecommerce'},
        {ID: 5, NAME: 'Migración'},
        {ID: 6, NAME: 'Retención'}
      ]);
      this.dCanal_Subject.next(this.canalData);
    }
  }

  sendDataPRODUCTO(data: Productos[], index: number){
    this.prodData[index] = [];
    this.prodData[index].push(...data);
    this.dPRODUCTO_Subject.next(this.prodData)
  }

  sendDataBuro(data: Buro[], index: number){
    if(!this.buroData[index]){
      this.buroData[index] = [];
      this.buroData[index].push(...data);
      this.dBuro_Subject.next(this.buroData);
    }
  }

  sendDataModosPago(data: ModosPago[], index: number){
    if(!this.mdpgData[index]){
      this.mdpgData[index] = [];
      this.mdpgData[index].push(...data);
      this.dModoPago_Subject.next(this.mdpgData);
    }
  }

  sendDataEntidades(data: Entidades[], index: number){
    if(!this.entidadesData[index]){
      this.entidadesData[index] = [];
      this.entidadesData[index].push(...data);
      this.dTarjetas_Subject.next(this.entidadesData);
    }
  }

  sendDataTarjetas(data: Tarjetas[], index: number){
    if(!this.tarjetasData[index]){
      this.tarjetasData[index] = [];
      this.tarjetasData[index].push(...data);
      this.dTarjetas_Subject.next(this.tarjetasData)
    }
  }

  sendDataProvincias(data: Provincias[], index: number){
    this.provinciaData[index] = [];
    this.provinciaData[index].push(...data);
    this.dProvincias_Subject.next(this.provinciaData);
  }

  sendDataCiudades(data: Ciudades[], index: number){
    this.ciudadData[index] = [];
    this.ciudadData[index].push(...data);
    this.dCiudades_Subject.next(this.ciudadData);
  }
  
  sendDataSectores(data: Sectores[], index: number){
    this.sectoresData[index] = [];
    this.sectoresData[index].push(...data);
    this.dSectores_Subject.next(this.sectoresData);
  }

  sendDataPrecioRegular(data: PrecioRegular[],index: number){
    this.precioRegularData[index] = [];
    this.precioRegularData[index].push(...data);
    this.dPrecioRegular_Subject.next(this.precioRegularData)
  }

  sendDataPrecioPromo(data: number, index: number){
    this.precioPromocional[index] = [];
    this.precioPromocional[index].push(data);
    this.dPrecioPromo_Subject.next(this.precioPromocional);
  }

  sendDataDiasGozados(data: DiasGozados[], index: number){
    if(!this.diasGozadosData[index]){
      this.diasGozadosData[index] = [];
      this.diasGozadosData[index].push(...data);
      this.dDiasGozados_Subject.next(this.diasGozadosData);
    }
  }

  sendDataUPGRADE(data: Upgrade[], index: number){
    this.upgradeData[index] = [];
    this.upgradeData[index].push(...data);
    this.dUpgrade_Subject.next(this.upgradeData);
  }

  sendDataMesPromocion(data: number, index: number, type: string){
    if(type == "INICIO"){
      this.mesInicioPromo[index] = [];
      this.mesInicioPromo[index].push(data);
      this.dMesInicioPromo_Subject.next(this.mesInicioPromo);
    } else if (type == "FIN"){
      this.mesFinPromo[index] = [];
      this.mesFinPromo[index].push(data);
      this.dMesFinPromo_Subject.next(this.mesFinPromo);
    }
  }

  /*----------------------------DICCIONARIO DE DATOS--------------------------------*/
  sendDataNewDiccionario(index:number){
    this.diccionario[index] = {}; 
    this.dDiccionario_Subject.next(this.diccionario);
    console.log("Diccionario creado index: "+index);
    console.log(this.diccionario);
  }

  sendDataUptadeDiccionario(data:{ [key: string]: any }, index: number){
    Object.keys(data).forEach(key => {this.diccionario[index][key] = data[key];});
    this.dDiccionario_Subject.next(this.diccionario);
  }
  /*----------------------------DICCIONARIO DE DATOS--------------------------------*/
}
