import { Component, OnInit } from '@angular/core';
import { DataService } from './../../services/data.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  
  test = null;

  constructor(private dataService: DataService) { }

  //sto get request vazw to url pou zitaw.

  ngOnInit() {
    // this.dataService.sendGetRequest().subscribe((data: any) => {
    //   console.log(data);
    //   this.test = data;
    // });
  }

}
