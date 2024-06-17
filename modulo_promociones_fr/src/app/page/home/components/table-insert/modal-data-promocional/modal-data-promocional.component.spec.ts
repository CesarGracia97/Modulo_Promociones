import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ModalDataPromocionalComponent } from './modal-data-promocional.component';

describe('ModalDataPromocionalComponent', () => {
  let component: ModalDataPromocionalComponent;
  let fixture: ComponentFixture<ModalDataPromocionalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ModalDataPromocionalComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ModalDataPromocionalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
