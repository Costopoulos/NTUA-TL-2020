import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SessionsPerProviderComponent } from './sessions-per-provider.component';

describe('SessionsPerProviderComponent', () => {
  let component: SessionsPerProviderComponent;
  let fixture: ComponentFixture<SessionsPerProviderComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SessionsPerProviderComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SessionsPerProviderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
