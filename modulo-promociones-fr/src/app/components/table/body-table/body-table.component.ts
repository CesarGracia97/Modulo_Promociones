import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';


@Component({
  selector: 'app-body-table',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './body-table.component.html',
  styleUrl: './body-table.component.scss'
})
export class BodyTableComponent {
  cities = [
    { name: 'Quito', temperature: 18, description: 'Mayormente soleado' },
    { name: 'Guayaquil', temperature: 28, description: 'Parcialmente nublado' },
    { name: 'Cuenca', temperature: 15, description: 'Lluvias dispersas' },
    { name: 'Manta', temperature: 25, description: 'Nublado con posibilidad de lluvias' }
  ];
}
