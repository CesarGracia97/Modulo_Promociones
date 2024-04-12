import { Component } from '@angular/core';
import { HeaderTableComponent } from './header-table/header-table.component';
import { BodyTableComponent } from './body-table/body-table.component';

@Component({
  selector: 'app-table-query',
  standalone: true,
  imports: [HeaderTableComponent, BodyTableComponent],
  templateUrl: './table-query.component.html',
  styleUrl: './table-query.component.scss'
})
export class TableQueryComponent {

}
