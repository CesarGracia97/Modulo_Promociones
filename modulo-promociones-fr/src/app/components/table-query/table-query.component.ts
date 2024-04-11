import { Component } from '@angular/core';
import { HeaderTableComponent } from "./header-table/header-table.component";
import { BodyTableComponent } from "./body-table/body-table.component";

@Component({
    selector: 'app-table-query',
    standalone: true,
    templateUrl: './table-query.component.html',
    styleUrls: ['./table-query.component.scss'],
    imports: [HeaderTableComponent, BodyTableComponent]
})
export class TableQueryComponent {

}
