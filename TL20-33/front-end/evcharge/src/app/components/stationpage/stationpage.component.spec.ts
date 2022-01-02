import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StationpageComponent } from './stationpage.component';

describe('StationpageComponent', () => {
  let component: StationpageComponent;
  let fixture: ComponentFixture<StationpageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StationpageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(StationpageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
