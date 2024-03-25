import { Component } from '@angular/core';
import { CombosService } from '../../../planes/services/combos.service';
import { ProvinciasService } from '../../../places/services/provincias.service';
import { CiudadService } from '../../../places/services/ciudad.service';
import { SectorService } from '../../../places/services/sector.service';
import { ServiciosService } from '../../../planes/services/servicios.service';
import { TiposerviciosService } from '../../../planes/services/tiposervicios.service';
import { TecnologiasService } from '../../../planes/services/tecnologias.service';
import { TariffPlanesVariant } from '../../../planes/interfaces/tariffplanes.interface';

@Component({
  selector: 'app-header-table',
  standalone: true,
  imports: [],
  templateUrl: './header-table.component.html',
  styleUrl: './header-table.component.scss'
})
export class HeaderTableComponent {
  constructor(
    private combos: CombosService,
    private provincias: ProvinciasService,
    private ciudades: CiudadService,
    private sectores: SectorService,
    private servicio: ServiciosService,
    private tiposervicio: TiposerviciosService,
    private tecnologia: TecnologiasService//,
    //private TariffPlanesVariant: TariffPlanesVariant
    ){}

  ngOnInit():void{}

  darth_NihilusFuncion(comboElejido: string ){
    try
    {
      switch(comboElejido)
      {
        case 'TISE':
          //this.combos.getCombosTipoServicios();
          break;
        case 'RED':
          break;
        case 'PLAN':
          break;
        case 'PROV':
          break;
        case 'CITY':
          break;
        case 'SECT':
          break;
        default:
          console.log("--------------------------------------------")
          console.log("darth_NihilusFuncion - Opcion Incorrecta")
          console.log("--------------------------------------------")
      }
    }
    catch(error)
    {
      console.log("---------------------------------------------------------------")
      console.log("header-table.compo - darth_NihilusFuncion | Error detectado: ")
      console.log("Opcion: "+comboElejido+" | "+error)
      console.log("---------------------------------------------------------------")
    }

  }
}