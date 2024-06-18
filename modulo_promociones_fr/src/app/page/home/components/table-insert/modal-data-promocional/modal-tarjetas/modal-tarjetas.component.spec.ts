import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ModalTarjetasComponent } from './modal-tarjetas.component';

describe('ModalTarjetasComponent', () => {
  let component: ModalTarjetasComponent;
  let fixture: ComponentFixture<ModalTarjetasComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ModalTarjetasComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ModalTarjetasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
