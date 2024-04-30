import { Injectable } from '@angular/core';
import { ProvinciasService } from '../requests/places/provincias.service';
import { CiudadService } from '../requests/places/ciudad.service';
import { Provincias } from '../../interfaces/places/provincias.interface';
import { Ciudades } from '../../interfaces/places/ciudad.interface';
import { CommunicationDataService } from '../communication/communicationData.service';
import { SectorService } from '../requests/places/sector.service';
import { Sectores } from '../../interfaces/places/sector.interface';
import { map, Observable } from 'rxjs';
import { response } from 'express';

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

  fetchDataCiudad(id_Prov: number){
    this.city.getCiudadesESP(id_Prov).subscribe((response: any) => {
      if(response && response.CITIESxPROV){
        this.ciudadData = response.CITIESxPROV.map((city: any) =>{
          return{
            CIUDAD_ID: city.CIUDAD_ID,
            CIUDAD: city.CIUDAD
          };
        });
        this.comData.sendDataCiudades(this.ciudadData);
      }
    });
  }

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

  fetchDataProvinciasXTecnologiaXTariffplanVariant(tecnologia: string, tariffplanvariant: number){
    console.log("ProvinciaTTData");
    this.prov.getProvinciasXTecnologiasXTariffplanVariant(tecnologia, tariffplanvariant).subscribe((response: any) =>{
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

  fetchDataCiudadXTecnologiaXTariffplanVariant(id_Prov: number, tecnologia: string, tariffplanvariant: number){
    this.city.getCiudadesXTecnologiaXTariffplanVariant(id_Prov, tecnologia, tariffplanvariant).subscribe((response: any) => {
      if(response && response.CITIESxPROV){
        this.ciudadData = response.CITIESxPROV.map((city: any) =>{
          return{
            CIUDAD_ID: city.CIUDAD_ID,
            CIUDAD: city.CIUDAD
          };
        });
        this.comData.sendDataCiudades(this.ciudadData);
      }
    });
  }

  fetchDataSectorXTecnologiaXTariffplanVariant(id_City: number, tecnologia: string, tariffplanvariant: number){
    this.sect.getSectoresXTecnologiaXTariffplanVariant(id_City, tecnologia,tariffplanvariant).subscribe((response: any) => {
      if(response && response.SECTORSxCITY){
        this.sectorData = response.SECTORSxCITY.map((sect: any) =>{
          return{
            SECTOR_ID: sect.SECTOR_ID,
            SECTOR: sect.SECTOR_ID
          };
        });
        this.comData.sendDataSectores(this.sectorData);
      }
    });
  }

  //Retornar directamente

  fetchDataProvinciasXTecnologiaXTariffplanVariant_RETURN(tecnologia: string, tariffplanvariant: number): Observable<Provincias[]> {
    return this.prov.getProvinciasXTecnologiasXTariffplanVariant(tecnologia, tariffplanvariant).pipe(
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
  fetchDataCiudadXTecnologiaXTariffplanVariant_RETURN(id_Prov: number, tecnologia: string, tariffplanvariant: number): Observable<Ciudades[]>{
    return this.city.getCiudadesXTecnologiaXTariffplanVariant(id_Prov, tecnologia, tariffplanvariant)
    .pipe(map((response:any) =>{
      if (response && response.CITIESxPROV){
        return response.CITIESxPROV.map((city: any) => {
          return {
            CIUDAD_ID: city.CIUDAD_ID,
            CIUDAD: city.CIUDAD,
            selected: false
          }
        })
      }
    }));
  }
}