import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router'
import { DataService } from './../../services/data.service';
import { HttpParams } from '@angular/common/http'

@Component({
  selector: 'app-sessions-per-station',
  templateUrl: './sessions-per-station.component.html',
  styleUrls: ['./sessions-per-station.component.css']
})
export class SessionsPerStationComponent implements OnInit {

  constructor(private dataService:DataService) { }

  seslist: any=[];
  stations = new Array(20);

  ngOnInit(): void {
  }

  

}
