import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProviderpageComponent } from './providerpage.component';

describe('ProviderpageComponent', () => {
  let component: ProviderpageComponent;
  let fixture: ComponentFixture<ProviderpageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ProviderpageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ProviderpageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
