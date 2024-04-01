import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { BottonsComponent } from './bottons/bottons.component';

@Component({
  selector: 'app-side-bar',
  standalone: true,
  imports: [BottonsComponent],
  templateUrl: './side-bar.component.html',
  styleUrls: ['./side-bar.component.scss']
})
export class SideBarComponent implements OnInit{

  @Output() sidebarButtonClick = new EventEmitter<string>();

  constructor(){}

  ngOnInit(): void {}
  
}
