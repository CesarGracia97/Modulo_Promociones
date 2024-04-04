import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { CommunicationService } from '../../../services/complements/communication.service';
import { TipoServicios } from '../../../interfaces/planes/tiposervicios.interface';


@Component({
  selector: 'app-body-table',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './body-table.component.html',
  styleUrl: './body-table.component.scss'
})
export class BodyTableComponent {
  visibleDivId: string | null = null;
  tiseData: TipoServicios[] = [];
  constructor(
    private communicationService: CommunicationService
  ){}
  ngOnInit():void{
    this.communicationService.visbleItemT$.subscribe(operationId =>{
      this.visibleDivId = operationId
    });
    this.communicationService.dTISE$.subscribe(data => {
      this.tiseData = data;
      console.log("info de TiseData: ",this.tiseData)
    })
  }

}
