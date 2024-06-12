import { HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class HeaderCreatorService {

  constructor() { }

  createHeader(token: string) {
    let headers: HttpHeaders;
    headers = new HttpHeaders()
    .set('Content-Type', 'application/json; charset=utf-8')
    .set('Accept', 'application/json; charset=utf-8')
    .set('Access-Control-Allow-Origin', '*')
    .set('Authorization', 'Bearer '+token);
    return headers;
  }
}
