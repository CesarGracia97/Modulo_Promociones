import { Component, OnInit } from '@angular/core';
import { BottonsComponent } from '../bottons/bottons.component';

@Component({
  selector: 'app-side-bar',
  standalone: true,
  imports: [BottonsComponent],
  templateUrl: './side-bar.component.html',
  styleUrl: './side-bar.component.scss'
})
export class SideBarComponent implements OnInit{
  constructor(){

  }
  ngOnInit(): void {
      
  }
}
