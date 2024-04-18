import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-table-insert',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './table-insert.component.html',
  styleUrl: './table-insert.component.scss'
})
export class TableInsertComponent implements OnInit  {  

  rows: any[] = [];

  ngOnInit(): void {
    this.addRow(); // Añade la primera fila automáticamente al cargar
  }

  addRow(): void {
    const newRow = {
      id: this.rows.length + 1, // El ID será el contador de filas
      servicio: '',
      tipoServicio: '',
      red: '',
      plan: '',
      formaPago: '',
      buro: '',
      provincia: '',
      ciudad: '',
      sector: ''
    };
    this.rows.push(newRow); // Añade el nuevo objeto al array de filas
  }
}
