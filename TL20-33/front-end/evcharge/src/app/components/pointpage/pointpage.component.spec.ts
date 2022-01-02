import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PointpageComponent } from './pointpage.component';

describe('PointpageComponent', () => {
  let component: PointpageComponent;
  let fixture: ComponentFixture<PointpageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PointpageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PointpageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
