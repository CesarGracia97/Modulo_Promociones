import { Injectable } from '@angular/core';
import { ProvinciasService } from '../places/provincias.service';
import { CiudadService } from '../places/ciudad.service';
import { Provincias } from '../../interfaces/places/provincias.interface';
import { Ciudades } from '../../interfaces/places/ciudad.interface';
import { CommunicationDataService } from '../communication/communicationData.service';
import { SectorService } from '../places/sector.service';
import { Sectores } from '../../interfaces/places/sector.interface';

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
    console.log("CiudadData");
    this.city.getCiudadesESP(id_Prov).subscribe((response: any) => {
      console.log(response);
      if(response && response.CITIESxPROV){
        this.ciudadData = response.CITIESxPROV.map((city: any) =>{
          return{
            CIUDAD_ID: city.CIUDAD_ID,
            CIUDAD: city.CIUDAD
          };
        });
        console.log(this.ciudadData);
        this.comData.sendDataCiudades(this.ciudadData);
      }
    });
  }

  fetchDataProvincias(){
    console.log("ProvinciaData");
    this.prov.getProvincias().subscribe((response: any) =>{
      console.log(response); 
      if (response && response.PROVINCIES){
        this.provinciaData = response.PROVINCIES.map((provincia: any) => {
          return {
            PROVINCIA_ID: provincia.PROVINCIA_ID,
            PROVINCIA: provincia.PROVINCIA
          };
        });
        console.log(this.provinciaData); 
        this.comData.sendDataProvincias(this.provinciaData);
      }
    });
  }

  fetchDataProvinciasXTecnologiaXTariffplanVariant(tecnologia: string, tariffplanvariant: number){
    console.log("ProvinciaTTData");
    this.prov.getProvinciasXTecnologiasXTariffplanVariant(tecnologia, tariffplanvariant).subscribe((response: any) =>{
      console.log(response); 
      if (response && response.PROVINCIES){
        this.provinciaData = response.PROVINCIES.map((provincia: any) => {
          return {
            PROVINCIA_ID: provincia.PROVINCIA_ID,
            PROVINCIA: provincia.PROVINCIA
          };
        });
        console.log(this.provinciaData); 
        this.comData.sendDataProvincias(this.provinciaData);
      }
    });
  }

  fetchDataCiudadXTecnologiaXTariffplanVariant(id_Prov: number, tecnologia: string, tariffplanvariant: number){
    console.log("CiudadDataTT");
    this.city.getCiudadesXTecnologiaXTariffplanVariant(id_Prov, tecnologia, tariffplanvariant).subscribe((response: any) => {
      console.log(response);
      if(response && response.CITIESxPROV){
        this.ciudadData = response.CITIESxPROV.map((city: any) =>{
          return{
            CIUDAD_ID: city.CIUDAD_ID,
            CIUDAD: city.CIUDAD
          };
        });
        console.log(this.ciudadData);
        this.comData.sendDataCiudades(this.ciudadData);
      }
    });
  }

  fetchDataSectorXTecnologiaXTariffplanVariant(id_City: number, tecnologia: string, tariffplanvariant: number){
    console.log("SectorDataTT");
    this.sect.getSectoresXTecnologiaXTariffplanVariant(id_City, tecnologia,tariffplanvariant).subscribe((response: any) => {
      console.log(response);
      if(response && response.SECTORSxCITY){
        this.sectorData = response.SECTORSxCITY.map((sect: any) =>{
          return{
            SECTOR_ID: sect.SECTOR_ID,
            SECTOR: sect.SECTOR_ID
          };
        });
        console.log(this.sectorData);
        this.comData.sendDataSectores(this.sectorData);
      }
    });
  }
}
