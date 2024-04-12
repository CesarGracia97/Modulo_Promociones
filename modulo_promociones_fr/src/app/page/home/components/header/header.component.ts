import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [],
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss'
})
export class HeaderComponent implements OnInit {
  @Input() sidebarActive = false;
  @Output() toggleSidebar = new EventEmitter();
  
  constructor(){}
  
  ngOnInit(): void {}
}
