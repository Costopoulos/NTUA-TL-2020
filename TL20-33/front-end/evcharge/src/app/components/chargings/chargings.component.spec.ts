import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChargingsComponent } from './chargings.component';

describe('ChargingsComponent', () => {
  let component: ChargingsComponent;
  let fixture: ComponentFixture<ChargingsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ChargingsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ChargingsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
