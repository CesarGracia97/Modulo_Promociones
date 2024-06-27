import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ModalUpgradeComponent } from './modal-upgrade.component';

describe('ModalUpgradeComponent', () => {
  let component: ModalUpgradeComponent;
  let fixture: ComponentFixture<ModalUpgradeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ModalUpgradeComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ModalUpgradeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
