import { TestBed } from '@angular/core/testing';

import { InjectionDataService } from './injection-data.service';

describe('InjectionDataService', () => {
  let service: InjectionDataService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(InjectionDataService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
