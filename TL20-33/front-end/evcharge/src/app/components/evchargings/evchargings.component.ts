import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DataService } from 'src/app/services/data.service';
import * as moment from 'moment';

@Component({
  selector: 'app-evchargings',
  templateUrl: './evchargings.component.html',
  styleUrls: ['./evchargings.component.css']
})
export class EvchargingsComponent implements OnInit {

  chargings = null;
  minDate: Date;
  maxDate: Date;
  carID: any;
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
      this.carID = params.get('Car_id');
    });
    this.dataService.sendGetRequest("SessionsPerEV/" + this.carID).subscribe((data: any) => {
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
    this.dataService.sendGetRequest("SessionsPerEV/" + this.carID + this.url).subscribe(
      (response) => {
        console.log('response received')
        console.log(response);
        this.chargings = response;
        console.log('kai to url einai: ')
        console.log(this.url)
      },
      (error) => {
        console.log('error caught in componkas')
        console.log(error)
        this.errorMessage = error;
        this.loading = false;

        throw error;
      }
    )
  }

}