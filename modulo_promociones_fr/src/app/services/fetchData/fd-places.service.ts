import { Injectable } from '@angular/core';
import { ProvinciasService } from '../requests/GET/places/provincias.service';
import { CiudadService } from '../requests/GET/places/ciudad.service';
import { Provincias } from '../../interfaces/places/provincias.interface';
import { Ciudades } from '../../interfaces/places/ciudad.interface';
import { DataPromocionInformationService } from '../subscribeData/data-promocion-information.service';
import { SectorService } from '../requests/GET/places/sector.service';
import { Sectores } from '../../interfaces/places/sector.interface';
import { map, Observable } from 'rxjs';
import { response } from 'express';

@Injectable({
  providedIn: 'root'
})

export class FdPlacesService {

  private provinciaData: Provincias[] = [];
  private ciudadData: Ciudades[] = [];
  private sectorData: Sectores[] = [];

  constructor(
    private prov: ProvinciasService,
    private city: CiudadService,
    private sect: SectorService,
    private comData: DataPromocionInformationService
  ) { }

  //Retorno por Subscripciones

  fetchDataProvincias(index: number){
    this.prov.getProvincias().subscribe((response: any) =>{
      if (response && response.PROVINCIES){
        this.provinciaData = response.PROVINCIES.map((provincia: any) => {
          return {
            PROVINCIA_ID: provincia.PROVINCIA_ID,
            PROVINCIA: provincia.PROVINCIA
          };
        });
        this.comData.sendDataProvincias(this.provinciaData, index);
      }
    });
  }

  fetchDataCiudad(id_Prov: number, index: number){
    this.city.getCiudadesESP(id_Prov).subscribe((response: any) => {
      if(response && response.CITIESxPROV){
        this.ciudadData = response.CITIESxPROV.map((city: any) =>{
          return{
            CIUDAD_ID: city.CIUDAD_ID,
            CIUDAD: city.CIUDAD,
            PROVINCIA: city.PROVINCIA
          };
        });
        this.comData.sendDataCiudades(this.ciudadData, index);
      }
    });
  }

  fetchDataProvinciasXTariffplanVariant(tariffplanvariant: number, index: number){
    this.prov.getProvinciasXTariffplanVariant(tariffplanvariant).subscribe((response: any) =>{
      if (response && response.PROVINCIES){
        this.provinciaData = response.PROVINCIES.map((provincia: any) => {
          return {
            PROVINCIA_ID: provincia.PROVINCIA_ID,
            PROVINCIA: provincia.PROVINCIA,
            selected: false
          };
        });
        this.comData.sendDataProvincias(this.provinciaData, index);
      }
    });
  }

  fetchDataCiudadesALLXTariffplanVariant(IdVariant: number, ProductoId: number, index: number){
    this.city.getCiudadesALLXTariffplanVariantXProductoId(IdVariant, ProductoId).subscribe((response: any) => {
      if (response && response.CITIESxPROV) {
        this.ciudadData = response.CITIESxPROV.map((city: any) => {
          return {
            CIUDAD_ID: city.CIUDAD_ID,
            CIUDAD: city.CIUDAD,
            PROVINCIA: city.PROVINCIA,
            selected: false
          }
        });
        this.comData.sendDataCiudades(this.ciudadData, index);
      }
    });
  }

  fetchDataCiudadXTariffplanVariant(id_Prov: number, tariffplanvariant: number, index: number){
    this.city.getCiudadesXTariffplanVariant(id_Prov, tariffplanvariant).subscribe((response: any) => {
      if (response && response.CITIESxPROV) {
        this.ciudadData = response.CITIESxPROV.map((city: any) => {
          return {
            CIUDAD_ID: city.CIUDAD_ID,
            CIUDAD: city.CIUDAD,
            PROVINCIA: city.PROVINCIA,
            selected: false
          }
        });
        this.comData.sendDataCiudades(this.ciudadData, index);
      }
    });
  }

  fetchDataCiudadesMasivasXTariffplanVariant(id_Provs: number[], tariffplanvariant: number, index: number){
    this.city.getCiudadesMasivasXTariffplanVariant(id_Provs, tariffplanvariant).subscribe((response: any) => {
      if (response && response.CITIESxPROV) {
        this.ciudadData = response.CITIESxPROV.map((city: any) => {
          return {
            CIUDAD_ID: city.CIUDAD_ID,
            CIUDAD: city.CIUDAD,
            PROVINCIA: city.PROVINCIA,
            selected: false
          }
        });
        this.comData.sendDataCiudades(this.ciudadData, index);
      }
    })
  }

  fetchDataSectoresMasivosXTariffplanVariant(id_Cities: number[], tariffplanvariant: number, index: number){
    this.sect.getSectoresMasivosXTariffplanVariant(id_Cities, tariffplanvariant).subscribe((response: any) => {
      if(response && response.SECTORSxCITY){
        this.sectorData = response.SECTORSxCITY.map((sect: any) => {
          return {
            SECTOR_ID: sect.SECTOR_ID,
            SECTOR: sect.SECTOR,
            CIUDAD: sect.CIUDAD,
            selected: false
          };
        });
        this.comData.sendDataSectores(this.sectorData, index);
      }
    })
  }

  fetchDataSectoresMasivosXTariffplanVariantXProducto(id_Cities: number[], tariffplanvariant: number, productoId: number, index: number){
    this.sect.getSectoresMasivosXTariffplanVariantXProductoId(id_Cities, tariffplanvariant, productoId).subscribe((response: any) => {
      if(response && response.SECTORSxCITY){
        this.sectorData = response.SECTORSxCITY.map((sect: any) => {
          return {
            SECTOR_ID: sect.SECTOR_ID,
            SECTOR: sect.SECTOR,
            CIUDAD: sect.CIUDAD,
            selected: false
          };
        });
        console.log("Se envio los datos")
        this.comData.sendDataSectores(this.sectorData, index);
      }
    });
  }

  // RETORNO DIRECTO

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

  fetchDataCiudadesALLXTariffplanVariant_RETURN(tariffplanvariant: number, ProductoId: number):  Observable<Ciudades[]> {
    return this.city.getCiudadesALLXTariffplanVariantXProductoId(tariffplanvariant, ProductoId)
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

  fetchDataCiudadesMasivasXTariffplanVariant_RETURN(id_Provs: number[], tariffplanvariant: number): Observable <Provincias[]> {
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

  fetchDataSectoresMasivosXTariffplanVariantXProducto_RETURN(id_Cities: number[], tariffplanvariant: number, productoId: number):Observable<Sectores[]> {
    return this.sect.getSectoresMasivosXTariffplanVariantXProductoId(id_Cities, tariffplanvariant, productoId)
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