import { Component } from '@angular/core';
import { HeaderTableComponent } from "./header-table/header-table.component";
import { BodyTableComponent } from "./body-table/body-table.component";

@Component({
    selector: 'app-table',
    standalone: true,
    templateUrl: './table.component.html',
    styleUrls: ['./table.component.scss'],
    imports: [HeaderTableComponent, BodyTableComponent]
})
export class TableComponent {

}
