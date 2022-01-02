import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SessionsPerPointComponent } from './sessions-per-point.component';

describe('SessionsPerPointComponent', () => {
  let component: SessionsPerPointComponent;
  let fixture: ComponentFixture<SessionsPerPointComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SessionsPerPointComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SessionsPerPointComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
