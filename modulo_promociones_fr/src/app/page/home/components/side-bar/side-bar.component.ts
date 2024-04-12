import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { ButtonsComponent } from './buttons/buttons.component';

@Component({
  selector: 'app-side-bar',
  standalone: true,
  imports: [ButtonsComponent],
  templateUrl: './side-bar.component.html',
  styleUrl: './side-bar.component.scss'
})
export class SideBarComponent implements OnInit{

  @Output() sidebarButtonClick = new EventEmitter<string>();

  constructor(){}

  ngOnInit(): void {}
  
}
