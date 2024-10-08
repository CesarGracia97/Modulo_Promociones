import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Sectores } from '../../../../interfaces/places/sector.interface';
import { environment } from '../../../../../environments/environment';
import { UuidgeneratorService } from '../../../complements/uuidgenerator.service';

const API_MAIN = environment.MAIN_URL;
const SECT = environment.API_GET_PLACES_SECT;
const CHANNEL = environment.CHANNEL;

@Injectable({
  providedIn: 'root'
})
export class SectorService {

  constructor(private http:HttpClient, private  uuidService: UuidgeneratorService) { }

  getSectoresALL():Observable<Sectores[]>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: this.uuidService.generateUUID(),
      channel: CHANNEL,
      type: 'ALL_SECTORS'
    }
    return this.http.post<Sectores[]>(API_MAIN+SECT, body, { headers });
  }

  getSectoresESP(id_City: number):Observable<Sectores[]>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: this.uuidService.generateUUID(),
      channel: CHANNEL,
      type: 'SECTORES_ESPECIFICOSxCITY',
      id_City: id_City.toString()
    }
    return this.http.post<Sectores[]>(API_MAIN+SECT, body, { headers });
  }

  getSectoresALLXTariffplanVariant(tariffplanvariant: number): Observable<Sectores[]> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: this.uuidService.generateUUID(),
      channel: CHANNEL,
      type: 'SECTORES_ESPECIFICOSxTFV',
      TARIFFPLANVARIANT: tariffplanvariant.toString()
    }
    return this.http.post<Sectores[]>(API_MAIN+SECT, body, { headers });
  }

  getSectoresXTariffplanVariant(id_City: number, tariffplanvariant: number): Observable<Sectores[]> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: this.uuidService.generateUUID(),
      channel: CHANNEL,
      type: 'SECTORES_ESPECIFICOSxCITYxTFV',
      id_City: id_City,
      TARIFFPLANVARIANT: tariffplanvariant.toString()
    }
    return this.http.post<Sectores[]>(API_MAIN+SECT, body, { headers });
  }

  getSectoresMasivosXTariffplanVariant(id_Cities: number[], tariffplanvariant: number): Observable<Sectores[]> {
    const a_idCities = id_Cities.join(',');
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: this.uuidService.generateUUID(),
      channel: CHANNEL,
      type: 'SECTORES_M__ESPECIFICOSxCITYxTFV',
      id_Cities: a_idCities,
      TARIFFPLANVARIANT: tariffplanvariant.toString()
    }
    return this.http.post<Sectores[]>(API_MAIN+SECT, body, { headers });
  }

  getSectoresMasivosXTariffplanVariantXProductoId(id_Cities: number[], tariffplanvariant: number, ProductoId: number): Observable<Sectores[]> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: this.uuidService.generateUUID(),
      channel: CHANNEL,
      type: 'SECTORES_M_ESPECIFICOSxCITYxTFVxPROD',
      id_Cities: id_Cities,
      TARIFFPLANVARIANT: tariffplanvariant,
      PRODUCTOID: ProductoId
    }
    return this.http.post<Sectores[]>(API_MAIN+SECT, body, { headers });
  }
}