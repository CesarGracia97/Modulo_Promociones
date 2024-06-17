import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ModalPromocionesAdicionalesComponent } from './modal-promociones-adicionales.component';

describe('ModalPromocionesAdicionalesComponent', () => {
  let component: ModalPromocionesAdicionalesComponent;
  let fixture: ComponentFixture<ModalPromocionesAdicionalesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ModalPromocionesAdicionalesComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ModalPromocionesAdicionalesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
