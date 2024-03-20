import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-bottons',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './bottons.component.html',
  styleUrl: './bottons.component.scss'
})
export class BottonsComponent implements OnInit {
  options = [
    {name: 'Tipo de Servicio', value:'opcion-1'},
    {name: 'Red', value:'opcion-2'},
    {name: 'Plan', value:'opcion-3'},
    {name: 'Provincial', value:'opcion-4'},
    {name: 'Ciudad', value:'opcion-5'},
    {name: 'Sector', value:'opcion-6'}
  ]

  constructor(){ }

  ngOnInit(): void {}
}
