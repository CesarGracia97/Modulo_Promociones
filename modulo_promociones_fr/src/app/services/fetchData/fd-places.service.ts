import { Injectable } from '@angular/core';
import { ProvinciasService } from '../requests/places/provincias.service';
import { CiudadService } from '../requests/places/ciudad.service';
import { Provincias } from '../../interfaces/places/provincias.interface';
import { Ciudades } from '../../interfaces/places/ciudad.interface';
import { CommunicationDataService } from '../communication/communicationData.service';
import { SectorService } from '../requests/places/sector.service';
import { Sectores } from '../../interfaces/places/sector.interface';
import { map, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class FdPlacesService {

  provinciaData: Provincias[] = [];
  ciudadData: Ciudades[] = [];
  sectorData: Sectores[] = [];

  constructor(
    private prov: ProvinciasService,
    private city: CiudadService,
    private sect: SectorService,
    private comData: CommunicationDataService
  ) { }

  //Retorno por Subscripciones

  fetchDataProvincias(){
    this.prov.getProvincias().subscribe((response: any) =>{
      if (response && response.PROVINCIES){
        this.provinciaData = response.PROVINCIES.map((provincia: any) => {
          return {
            PROVINCIA_ID: provincia.PROVINCIA_ID,
            PROVINCIA: provincia.PROVINCIA
          };
        });
        this.comData.sendDataProvincias(this.provinciaData);
      }
    });
  }

  fetchDataProvinciasXTecnologiaXTariffplanVariant(tariffplanvariant: number){
    this.prov.getProvinciasXTariffplanVariant(tariffplanvariant).subscribe((response: any) =>{
      if (response && response.PROVINCIES){
        this.provinciaData = response.PROVINCIES.map((provincia: any) => {
          return {
            PROVINCIA_ID: provincia.PROVINCIA_ID,
            PROVINCIA: provincia.PROVINCIA,
            selected: false
          };
        });
        this.comData.sendDataProvincias(this.provinciaData);
      }
    });
  }

  fetchDataCiudad(id_Prov: number){
    this.city.getCiudadesESP(id_Prov).subscribe((response: any) => {
      if(response && response.CITIESxPROV){
        this.ciudadData = response.CITIESxPROV.map((city: any) =>{
          return{
            CIUDAD_ID: city.CIUDAD_ID,
            CIUDAD: city.CIUDAD,
            PROVINCIA: city.PROVINCIA
          };
        });
        this.comData.sendDataCiudades(this.ciudadData);
      }
    });
  }
  
  //Retornar directamente

  fetchDataProvinciasXTariffplanVariant_RETURN(tariffplanvariant: number): Observable<Provincias[]> {
    return this.prov.getProvinciasXTariffplanVariant(tariffplanvariant).pipe(
      map((response: any) => {
        if (response && response.PROVINCIES){
          return response.PROVINCIES.map((provincia: any) => {
            return {
              PROVINCIA_ID: provincia.PROVINCIA_ID,
              PROVINCIA: provincia.PROVINCIA
            };
          });
        } else {
          return [];
        }
      })
    );
  }

  fetchDataCiudadesALLXTariffplanVariant_RETURN(tariffplanvariant: number):  Observable<Ciudades[]> {
    return this.city.getCiudadesALLXTariffplanVariant(tariffplanvariant)
    .pipe(map((response: any) => {
      if (response && response.CITIESxPROV){
        return response.CITIESxPROV.map((city: any) => {
          return {
            CIUDAD_ID: city.CIUDAD_ID,
            CIUDAD: city.CIUDAD,
            PROVINCIA: city.PROVINCIA,
            selected: false
          }
        })
      }
    }));
  }

  fetchDataCiudadXTariffplanVariant_RETURN(id_Prov: number, tariffplanvariant: number): Observable<Ciudades[]> {
    return this.city.getCiudadesXTariffplanVariant(id_Prov, tariffplanvariant)
    .pipe(map((response: any) => {
      if (response && response.CITIESxPROV){
        return response.CITIESxPROV.map((city: any) => {
          return {
            CIUDAD_ID: city.CIUDAD_ID,
            CIUDAD: city.CIUDAD,
            PROVINCIA: city.PROVINCIA,
            selected: false
          }
        })
      }
    }));
  }

  fetchDataCiudadesMasivasXTariffplanVariant(id_Provs: number[], tariffplanvariant: number): Observable <Provincias[]> {
    return this.city.getCiudadesMasivasXTariffplanVariant(id_Provs, tariffplanvariant)
    .pipe(map((response: any) => {
      if(response && response.CITIESxPROV) {
        return response.CITIESxPROV.map((city: any) => {
          return {
            CIUDAD_ID: city.CIUDAD_ID,
            CIUDAD: city.CIUDAD,
            PROVINCIA: city.PROVINCIA,
            selected: false
          };
        })
      }
    }));
  }

  fetchDataSectoresMasivosXTariffplanVariant_RETURN(id_Cities: number[], tariffplanvariant: number):Observable<Sectores[]> {
    return this.sect.getSectoresMasivosXTariffplanVariant(id_Cities, tariffplanvariant)
    .pipe(map((response: any) => {
      if(response && response.SECTORSxCITY){
        return response.SECTORSxCITY.map((sect: any) => {
          return {
            SECTOR_ID: sect.SECTOR_ID,
            SECTOR: sect.SECTOR,
            CIUDAD: sect.CIUDAD,
            selected: false
          };
        })
      }
    }));
  }
}