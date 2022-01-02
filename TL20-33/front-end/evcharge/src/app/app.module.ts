import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FlexLayoutModule } from '@angular/flex-layout';
import { ChartsModule } from 'ng2-charts';

import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { MatToolbarModule } from '@angular/material/toolbar';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatInputModule } from '@angular/material/input';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatNativeDateModule } from '@angular/material/core';
import { MatSelectModule } from '@angular/material/select';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatTabsModule } from '@angular/material/tabs'; 
import { MatTableModule } from '@angular/material/table';
import { MatListModule } from '@angular/material/list';
import { MatChipsModule } from '@angular/material/chips';
import { MatDialogModule } from '@angular/material/dialog';

import { HomeComponent } from './components/home/home.component';
import { SessionsPerEvComponent } from './components/sessions-per-ev/sessions-per-ev.component';
import { SessionsPerStationComponent } from './components/sessions-per-station/sessions-per-station.component';
import { StationpageComponent } from './components/stationpage/stationpage.component';
import { ChargingsComponent } from './components/chargings/chargings.component';
import { LoginComponent } from './components/login/login.component';
import { SessionsPerPointComponent } from './components/sessions-per-point/sessions-per-point.component';
import { SessionsPerProviderComponent } from './components/sessions-per-provider/sessions-per-provider.component';
import { EvpageComponent } from './components/evpage/evpage.component';
import { ProviderpageComponent } from './components/providerpage/providerpage.component';
import { PointpageComponent } from './components/pointpage/pointpage.component';
import { PointchargingsComponent } from './components/pointchargings/pointchargings.component';
import { EvchargingsComponent } from './components/evchargings/evchargings.component';
import { ProviderchargingsComponent } from './components/providerchargings/providerchargings.component';
import { ChargeComponent } from './components/charge/charge.component';
import { MiscComponent } from './misc/misc.component';
import { LogoutComponent } from './components/logout/logout.component';
import { GslowComponent } from './components/gslow/gslow.component';
import { PaymentComponent } from './components/payment/payment.component';
import { NewpayComponent } from './components/newpay/newpay.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    SessionsPerEvComponent,
    SessionsPerStationComponent,
    StationpageComponent,
    ChargingsComponent,
    LoginComponent,
    SessionsPerPointComponent,
    SessionsPerProviderComponent,
    EvpageComponent,
    ProviderpageComponent,
    PointpageComponent,
    PointchargingsComponent,
    EvchargingsComponent,
    ProviderchargingsComponent,
    ChargeComponent,
    MiscComponent,
    LogoutComponent,
    GslowComponent,
    PaymentComponent,
    NewpayComponent
  ],

  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatFormFieldModule,
    MatSelectModule,
    MatDatepickerModule,
    MatInputModule,
    MatNativeDateModule,
    FormsModule, 
    ReactiveFormsModule,
    MatIconModule,
    MatButtonModule,
    MatCardModule,
    MatProgressSpinnerModule,
    MatGridListModule,
    MatTabsModule,
    MatTableModule,
    MatListModule,
    MatChipsModule,
    MatDialogModule,
    FlexLayoutModule,
    ChartsModule,
  ],

  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
