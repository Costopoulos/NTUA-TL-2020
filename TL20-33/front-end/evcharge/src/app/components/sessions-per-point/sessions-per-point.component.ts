import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router'
import { DataService } from './../../services/data.service';
import { HttpParams } from '@angular/common/http'

@Component({
  selector: 'app-sessions-per-point',
  templateUrl: './sessions-per-point.component.html',
  styleUrls: ['./sessions-per-point.component.css']
})
export class SessionsPerPointComponent implements OnInit {

  constructor(private dataService:DataService) { }

  seslist: any=[];
  points = new Array(100);

  ngOnInit(): void {
  }

  

}
