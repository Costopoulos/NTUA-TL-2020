import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { DataService } from './../../services/data.service';
import {FormGroup, FormControl, Validators} from '@angular/forms';
import { HttpParams } from '@angular/common/http';


@Component({
  selector: 'app-stationpage',
  templateUrl: './stationpage.component.html',
  styleUrls: ['./stationpage.component.css']
})

export class StationpageComponent implements OnInit {

  sessions = null;
  show_transactions = true;
  id: any;

  constructor(private dataService: DataService, private route: ActivatedRoute, private router: Router) { }

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      this.dataService.sendGetRequest("SessionsPerStation/" + params.get('Station_id')).subscribe((data: any) =>{
        console.log(data);
        this.sessions = data;
        this.id = this.sessions[0].Station_id;
      });
    });
  }

  onClickMe():void {
    this.show_transactions = true;
  }

}
