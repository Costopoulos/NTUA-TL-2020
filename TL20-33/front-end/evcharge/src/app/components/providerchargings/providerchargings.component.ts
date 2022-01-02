import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DataService } from 'src/app/services/data.service';
import * as moment from 'moment';

@Component({
  selector: 'app-providerchargings',
  templateUrl: './providerchargings.component.html',
  styleUrls: ['./providerchargings.component.css']
})
export class ProviderchargingsComponent implements OnInit {

  chargings = null;
  minDate: Date;
  maxDate: Date;
  providerID: any;
  startingDate: any;
  endingDate: any;
  errorMessage: string;
  loading: boolean;
  enabledate = false;

  url = "/null/null";
  

  constructor( private dataService: DataService, private route: ActivatedRoute) {
    const currentYear = new Date();
    this.minDate = new Date(currentYear.getFullYear() - 23, 0, 0);
    this.maxDate = new Date(currentYear);
  }


  ngOnInit(): void {
    this.route.paramMap.subscribe(params =>{
      this.providerID = params.get('Energy_Provider_id');
    });
    this.dataService.sendGetRequest("SessionsPerProvider/" + this.providerID).subscribe((data: any) => {
      console.log(data);
      this.chargings = data;
    })
  }

  returnAny(p:string):string {
    if (p=== null) return 'any';
    else return p;
  }

  startingDateChange(newdate: string): void {
    if (newdate === null) this.startingDate = null;
    else this.startingDate = moment(newdate).format('yyyyMMDD');
    console.log("Starting Date changed" + this.startingDate);
    this.enabledate = true;
    this.sendRequest();
  }

  endingDateChange(newdate: string): void {
    if (newdate === null) this.endingDate = null;
    else this.endingDate = moment(newdate).format('yyyyMMDD');
    console.log("Ending Change changed: " + this.endingDate);
    this.sendRequest();
  }


  sendRequest():void {
    this.loading = true;
    this.errorMessage = "";

    //this.url = "/" + this.startingDate + "/" + this.endingDate;
    this.url = (this.startingDate != undefined) ? ('/' + this.startingDate) : '' ;
    this.url += (this.endingDate != undefined) ? ('/' + this.endingDate) : '' ;
    this.chargings = null;
    this.dataService.sendGetRequest("SessionsPerProvider/" + this.providerID + this.url).subscribe(
      (response) => {
        console.log('response received')
        console.log(response);
        this.chargings = response;
        console.log(this.url)
      },
      (error) => {
        console.log('error caught in component')
        console.log(error)
        this.errorMessage = error;
        this.loading = false;

        throw error;
      }
    )
  }

}
