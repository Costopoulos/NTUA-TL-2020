import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EvchargingsComponent } from './evchargings.component';

describe('EvchargingsComponent', () => {
  let component: EvchargingsComponent;
  let fixture: ComponentFixture<EvchargingsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EvchargingsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EvchargingsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
