import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { PrecioRegular } from '../../../../interfaces/DataPromocional/precio-regular.interface';
import { environment } from '../../../../../environments/environment';
import { UuidgeneratorService } from '../../../complements/uuidgenerator.service';

const MAIN_URL = environment.MAIN_URL;
const PRECIO_REGULAR = environment.API_GET_PRECIO_REGULAR;
const CHANNEL = environment.CHANNEL;

@Injectable({
  providedIn: 'root'
})
export class PrecioRegularService {

  constructor(private http:HttpClient, private  uuidService: UuidgeneratorService) { }

  getPrecioRegular(id_Producto: number, TFPV: number):Observable<PrecioRegular[]>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = {
      externalTransactionId: this.uuidService.generateUUID(),
      channel: CHANNEL,
      type: 'PRECIO_REGULAR',
      id_Prod: id_Producto,
      TARIFFPLANVARIANT: TFPV
    }
    return this.http.post<PrecioRegular[]>(MAIN_URL+PRECIO_REGULAR, body, { headers });
  }

}
