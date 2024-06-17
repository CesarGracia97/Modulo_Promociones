import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ModalCiudadesysectoresComponent } from './modal-ciudadesysectores.component';

describe('ModalCiudadesysectoresComponent', () => {
  let component: ModalCiudadesysectoresComponent;
  let fixture: ComponentFixture<ModalCiudadesysectoresComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ModalCiudadesysectoresComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ModalCiudadesysectoresComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
