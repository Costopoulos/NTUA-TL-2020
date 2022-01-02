import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './../app/components/home/home.component';
import { SessionsPerEvComponent } from './../app/components/sessions-per-ev/sessions-per-ev.component';
import { SessionsPerStationComponent } from './../app/components/sessions-per-station/sessions-per-station.component';
import { SessionsPerPointComponent } from './../app/components/sessions-per-point/sessions-per-point.component';
import { SessionsPerProviderComponent } from './../app/components/sessions-per-provider/sessions-per-provider.component';

import { EvpageComponent } from './../app/components/evpage/evpage.component';
import { StationpageComponent } from './../app/components/stationpage/stationpage.component';
import { PointpageComponent } from './../app/components/pointpage/pointpage.component';
import { ProviderpageComponent } from './../app/components/providerpage/providerpage.component';

import { LoginComponent } from './components/login/login.component';
import { LogoutComponent } from './components/logout/logout.component';
import { ChargeComponent } from './/components/charge/charge.component';
import { MiscComponent } from './../app/misc/misc.component';
import { GslowComponent } from './components/gslow/gslow.component';
import { PaymentComponent } from './components/payment/payment.component';

const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full'},
  { path: 'home', component: HomeComponent },
  { path: 'login', component: LoginComponent },
  { path: 'logout', component: LogoutComponent },
  { path: 'sessions-per-ev', component: SessionsPerEvComponent },
  { path: 'sessions-per-ev/:Car_id', component: EvpageComponent },
  { path: 'sessions-per-station', component: SessionsPerStationComponent },
  { path: 'sessions-per-station/:Station_id', component: StationpageComponent },
  { path: 'sessions-per-point', component: SessionsPerPointComponent },
  { path: 'sessions-per-point/:Point_id', component: PointpageComponent },
  { path: 'sessions-per-provider', component: SessionsPerProviderComponent },
  { path: 'sessions-per-provider/:Energy_Provider_id', component: ProviderpageComponent },
  { path: 'charge', component: ChargeComponent },
  { path: 'charge/details/:selectedValue', component: MiscComponent },
  { path: 'gslow', component: GslowComponent},
  { path: 'payment', component: PaymentComponent},
  

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
