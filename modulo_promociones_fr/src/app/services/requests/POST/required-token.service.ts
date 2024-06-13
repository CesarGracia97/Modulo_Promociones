import { Injectable } from '@angular/core';
import { HeaderCreatorService } from '../../complements/header-creator.service';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';

const API_MAIN = environment.MAIN_URL;
const KEY_TOKEN = environment.KEY_TOKEN;
const API_TOKEN = environment.API_POST_TOKEN;

@Injectable({
  providedIn: 'root'
})
export class RequiredTokenService {

  constructor(private http: HttpClient, private headerCr: HeaderCreatorService) { }

  getToken() {
    const headers = this.headerCr.createHeader('token');
    const body = {
      channel: "string",
      key: KEY_TOKEN,
      realm: "realm-modulos_promocionales",
      type: "Basic"
    }
    return this.http.post<string>(API_MAIN + API_TOKEN, body, { headers });
  }
}
