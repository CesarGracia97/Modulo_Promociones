import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CommunicationService {

  private selectedButtonSubject = new Subject<string>();
  selectedButton$ = this.selectedButtonSubject.asObservable();

  constructor() {}

  sendSelectedButton(buttonId: string) {
    this.selectedButtonSubject.next(buttonId);
  }
}
