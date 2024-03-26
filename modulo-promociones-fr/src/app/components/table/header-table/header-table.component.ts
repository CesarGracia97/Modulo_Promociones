import { Component, OnInit } from '@angular/core';
import { CombosService } from '../../../services/planes/combos.service';
import { ProvinciasService } from '../../../services/places/provincias.service';
import { CiudadService } from '../../../services/places/ciudad.service';
import { SectorService } from '../../../services/places/sector.service';
import { ServiciosService } from '../../../services/planes/servicios.service';
import { TiposerviciosService } from '../../../services/planes/tiposervicios.service';
import { TecnologiasService } from '../../../services/planes/tecnologias.service';
import { TariffplanesService } from '../../../services/planes/tariffplanes.service';
import { CommonModule } from '@angular/common';
import { Servicios } from '../../../interfaces/planes/servicios.interface';
import { TipoServicios } from '../../../interfaces/planes/tiposervicios.interface';
import { Tecnologias } from '../../../interfaces/planes/tecnologias.interface';
import { TariffPlanesVariant } from '../../../interfaces/planes/tariffplanes.interface';
import { Provincias } from '../../../interfaces/places/provincias.interface';
import { Ciudades } from '../../../interfaces/places/ciudad.interface';

@Component({
  selector: 'app-header-table',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './header-table.component.html',
  styleUrl: './header-table.component.scss'
})
export class HeaderTableComponent implements OnInit{
  _servicio: Servicios[] = [];
  _tiposervicio: TipoServicios[] = [];
  _tecnologia: Tecnologias[] = [];
  _tariffplanvariant: TariffPlanesVariant[] = [];
  _provincias: Provincias[] = [];
  _ciudades: Ciudades[] = [];

  constructor(
    private combos: CombosService,
    private provincias: ProvinciasService,
    private ciudades: CiudadService,
    private sectores: SectorService,
    private servicio: ServiciosService,
    private tiposervicio: TiposerviciosService,
    private tecnologia: TecnologiasService,
    private tariffPlanesVariant: TariffplanesService){}

  ngOnInit():void
  {
    this.darth_NihilusFuncion();
  }

  darth_NihilusFuncion()
  {
    try
    {
      this.servicio.getServiciosALL().subscribe((_V1: Servicios[]) => {console.log(_V1);this._servicio = _V1;});
      // this.tiposervicio.getTipoServicioALL().subscribe((_V2: TipoServicios[]) => {console.log(_V2);this._tiposervicio = _V2;});
      // this.tecnologia.getTecnologiasALL().subscribe((_V3: Tecnologias[]) => {console.log(_V3);this._tecnologia = _V3;});
      // this.tariffPlanesVariant.getTariffPlanesVariantALL().subscribe((_V4: TariffPlanesVariant[]) => {console.log(_V4);this._tariffplanvariant = _V4;});
      // this.provincias.getProvincias().subscribe((_V5: Provincias[]) => {console.log(_V5);this._provincias = _V5;});
    }
    catch(error)
    {
      console.log("---------------------------------------------------------------")
      console.log("header-table.compo - darth_NihilusFuncion | Error detectado: ")
      console.log(error)
      console.log("---------------------------------------------------------------")
    }
  }
}