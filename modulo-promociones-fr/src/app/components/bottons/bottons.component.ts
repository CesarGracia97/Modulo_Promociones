import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
//import { ProvinciasService } from '../../places/services/provincias.service';
import { Provincias } from '../../places/interfaces/provincias.interface';

@Component({
  selector: 'app-bottons',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './bottons.component.html',
  styleUrl: './bottons.component.scss'
})
export class BottonsComponent implements OnInit {
  provincias: Provincias[] = [];
  
  options = [
    {name: 'Tipo de Servicio', value:'ptc-TIE'},
    {name: 'Red', value:'ptc-RED'},
    {name: 'Plan', value:'ptc-PLAN'},
    {name: 'Provincial', value:'ptc-PROV'},
    {name: 'Ciudad', value:'ptc-CITY'},
    {name: 'Sector', value:'ptc-SECT'}
  ]

  //constructor(private provinciasService: ProvinciasService){ }

  constructor(){}

  ngOnInit(): void {}
  /*
  handleButtonClick(value: string): void {
    try
    {
      if (value =='ptc-TIE')
      {
        this.provinciasService.getProvincias();
      }
      console.log('Peticion de Consulta:', value);
      this.mostrardatos();
    }
    catch (error){
      console.log('Algo Ocurrio: ', error);
    }
  }
  */
  /*
  mostrardatos(){
    this.provinciasService.getProvincias().subscribe(
      (data: Provincias[]) => {
        this.provincias = data;
        console.log('Datos recibidos:', this.provincias);
      },
      (error) => {
        console.error('Error al obtener las provincias:', error);
      }
    );

  }
  */
}
