import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GslowComponent } from './gslow.component';

describe('GslowComponent', () => {
  let component: GslowComponent;
  let fixture: ComponentFixture<GslowComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GslowComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GslowComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
