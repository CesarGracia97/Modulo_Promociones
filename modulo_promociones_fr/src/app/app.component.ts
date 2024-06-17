import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './page/home/components/header/header.component';
import { SideBarComponent } from './page/home/components/side-bar/side-bar.component';
import { TableInsertComponent } from './page/home/components/table-insert/table-insert.component';
import { CommunicationVisibleService } from './services/subscribeData/communicationVisible.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule, HeaderComponent, SideBarComponent, TableInsertComponent ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'modulo_promociones_fr';
  sidebarActive = false;
  visibleDivId: string | null = null;
  constructor(
    private comVisible: CommunicationVisibleService
  ){}

  ngOnInit():void{
    this.comVisible.visbleItemP$.subscribe(Id =>{
      this.visibleDivId = Id
    });
  }
}
