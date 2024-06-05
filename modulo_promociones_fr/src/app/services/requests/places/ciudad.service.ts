import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Ciudades } from '../../../interfaces/places/ciudad.interface';

@Injectable({
  providedIn: 'root'
})
export class CiudadService {

  private URLSimple = 'http://127.0.0.1:5012/api/ra/plccity_endpoint';
  private URLMasive = 'http://127.0.0.1:5012/api/ra/plcinfomasiva_endpoint';

  constructor(private http:HttpClient) { }

  getCiudadesALL(): Observable<Ciudades[]>{
    let params = new HttpParams().set('type', 'ALL_CITIES');
    return this.http.get<Ciudades[]>(this.URLSimple, { params: params });
  }

  getCiudadesESP(id_Prov:number):Observable<Ciudades[]>{
    let params = new HttpParams().set('type', 'CIUDADES_ESPECIFICASxPROV')
    .set('id_Prov', id_Prov.toString());
    return this.http.get<Ciudades[]>(this.URLSimple, { params: params });
  }

  getCiudadesALLXTariffplanVariant(tariffplanvariant: number): Observable <Ciudades[]> {
    let params = new HttpParams().set('type', 'CIUDADES_ESPECIFICASxTFV')
    .set('TARIFFPLANVARIANT', tariffplanvariant.toString());
    return this.http.get<Ciudades[]>(this.URLSimple, { params: params });
  }

  getCiudadesALLXTariffplanVariantXProductoId(tariffplanvariant: number, ProductoId: number): Observable <Ciudades[]> {
    let params = new HttpParams().set('type', 'CIUDADES_ESPECIFICASxTFVxPROD')
    .set('TARIFFPLANVARIANT', tariffplanvariant.toString())
    .set('PRODUCTOID', ProductoId.toString());
    return this.http.get<Ciudades[]>(this.URLSimple, { params: params });
  }

  getCiudadesXTariffplanVariant(id_Prov:number, tariffplanvariant: number):Observable<Ciudades[]>{
    let params = new HttpParams().set('type', 'CIUDADES_ESPECIFICASxPROVxTFV')
    .set('id_Prov', id_Prov.toString())
    .set('TARIFFPLANVARIANT', tariffplanvariant);
    return this.http.get<Ciudades[]>(this.URLSimple, { params: params });
  }

  getCiudadesMasivasXTariffplanVariant(id_Prov: number[], tariffplanvariant: number): Observable <Ciudades[]> {
    const a_idProv = id_Prov.join(',');
    let params = new HttpParams().set('type', 'CIUDADES_ESPECIFICASxPROVxTFV')
    .set('id_Provs', a_idProv)
    .set('TARIFFPLANVARIANT', tariffplanvariant.toString());
    return this.http.get<Ciudades[]>(this.URLMasive, { params: params });
  }
}
