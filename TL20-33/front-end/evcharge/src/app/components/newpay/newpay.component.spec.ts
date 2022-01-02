import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NewpayComponent } from './newpay.component';

describe('NewpayComponent', () => {
  let component: NewpayComponent;
  let fixture: ComponentFixture<NewpayComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NewpayComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NewpayComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
