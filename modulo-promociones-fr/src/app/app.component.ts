import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './components/header/header.component';
import { SideBarComponent } from './components/side-bar/side-bar.component';
import { TableComponent } from "./components/table/table.component";
@Component({
    selector: 'app-root',
    standalone: true,
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.scss'],
    imports: [RouterOutlet, CommonModule, HeaderComponent, SideBarComponent, TableComponent ]
})
export class AppComponent{
  title = 'modulo-promociones-fr';
  sidebarActive = false;
}
