import { Component, OnInit } from '@angular/core';
import { DataViewService } from '../../../../../services/subscribeData/data-view.service';
import { DataPromocionSupportService } from '../../../../../services/subscribeData/data-promocion-support.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-modal-informacion',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './modal-informacion.component.html',
  styleUrl: './modal-informacion.component.scss'
})
export class ModalInformacionComponent  implements OnInit {
  state: boolean = false; rowId: number = 0;
  mensaje: string= '';

  constructor(
    private data_views: DataViewService,
    private data_support: DataPromocionSupportService
  ){}

  ngOnInit(): void {
    this.data_views.dIndex$.subscribe( data => {this.rowId = data;});
    this.data_views.dModalViewMessage$.subscribe( data => {this.state = data;})
    this.data_support.dMensajeModalView$.subscribe( data => {this.mensaje = data;})
  }
  
  closeModalMensaje(): void {
    this.data_views.stateModalMessage(false);
  }
}
