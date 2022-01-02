import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SessionsPerEvComponent } from './sessions-per-ev.component';

describe('SessionsPerEvComponent', () => {
  let component: SessionsPerEvComponent;
  let fixture: ComponentFixture<SessionsPerEvComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SessionsPerEvComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SessionsPerEvComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
