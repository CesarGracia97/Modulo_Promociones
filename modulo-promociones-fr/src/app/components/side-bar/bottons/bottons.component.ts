import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CommunicationService } from '../../../services/complements/communication.service';

@Component({
  selector: 'app-bottons',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './bottons.component.html',
  styleUrl: './bottons.component.scss'
})
export class BottonsComponent implements OnInit {

  options = [
    {name: 'Tipo de Servicio', value:'TISE'},
    {name: 'Red', value:'RED'},
    {name: 'Plan', value:'PLAN'},
    {name: 'Provincial', value:'PROV'},
    {name: 'Ciudad', value:'CITY'},
    {name: 'Sector', value:'SECT'}
  ]

  constructor(private communicationService: CommunicationService){}

  ngOnInit(): void {}

  @Output() subButtonClick = new EventEmitter<string>();

  handleSubButtonClick(value: string): void {
    try
    {
      this.communicationService.sendSelectedButton(value);
    }
    catch (error)
    {
      console.log("---------------------------------------------------------------")
      console.log("botton.componets - handleSubButtonClick | Error detectado: ")
      console.log(error)
      console.log("---------------------------------------------------------------")
    }
  }
}
