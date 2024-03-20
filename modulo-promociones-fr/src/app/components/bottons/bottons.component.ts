import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProvinciasService } from '../../places/services/provincias.service';

@Component({
  selector: 'app-bottons',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './bottons.component.html',
  styleUrl: './bottons.component.scss'
})
export class BottonsComponent implements OnInit {
  options = [
    {name: 'Tipo de Servicio', value:'ptc-TIE'},
    {name: 'Red', value:'ptc-RED'},
    {name: 'Plan', value:'ptc-PLAN'},
    {name: 'Provincial', value:'ptc-PROV'},
    {name: 'Ciudad', value:'ptc-CITY'},
    {name: 'Sector', value:'ptc-SECT'}
  ]

  constructor(private provinciasService: ProvinciasService){ }

  ngOnInit(): void {}

  handleButtonClick(value: string): void {
    console.log('Peticion de Consulta:', value);
    if (value =='ptc-TIE')
    {
      this.provinciasService.getProvincias();
    }
    // Aquí puedes agregar cualquier otra lógica que quieras realizar al hacer clic en un botón
  }
}
