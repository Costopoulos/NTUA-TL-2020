import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProviderchargingsComponent } from './providerchargings.component';

describe('ProviderchargingsComponent', () => {
  let component: ProviderchargingsComponent;
  let fixture: ComponentFixture<ProviderchargingsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ProviderchargingsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ProviderchargingsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
