import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { DataViewService } from '../../../../../services/subscribeData/data-view.service';

@Component({
  selector: 'app-modal-error',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './modal-error.component.html',
  styleUrl: './modal-error.component.scss'
})
export class ModalErrorComponent implements OnInit {

  er_state: boolean = false; rowId: number = 0;
  mensaje: string= '';

  constructor(
    private data_views: DataViewService
  ){}

  ngOnInit(): void {
    this.data_views.dIndex$.subscribe( data => {this.rowId = data;});
    this.data_views.dModalViewER$.subscribe( data => {this.er_state = data;})
    this.data_views.dMensajeViewER$.subscribe( data => {this.mensaje = data;})
  }
  
  closeModalError(): void {
    this.data_views.stateModalER(false);
  }
}
