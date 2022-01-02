import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SessionsPerStationComponent } from './sessions-per-station.component';

describe('SessionsPerStationComponent', () => {
  let component: SessionsPerStationComponent;
  let fixture: ComponentFixture<SessionsPerStationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SessionsPerStationComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SessionsPerStationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
