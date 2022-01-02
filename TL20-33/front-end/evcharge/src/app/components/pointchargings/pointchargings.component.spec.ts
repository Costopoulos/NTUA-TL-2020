import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PointchargingsComponent } from './pointchargings.component';

describe('PointchargingsComponent', () => {
  let component: PointchargingsComponent;
  let fixture: ComponentFixture<PointchargingsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PointchargingsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PointchargingsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
