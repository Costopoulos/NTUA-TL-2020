import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EvpageComponent } from './evpage.component';

describe('EvpageComponent', () => {
  let component: EvpageComponent;
  let fixture: ComponentFixture<EvpageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EvpageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EvpageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
