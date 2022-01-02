import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router'
import { DataService } from './../../services/data.service';
import { HttpParams } from '@angular/common/http'

@Component({
  selector: 'app-sessions-per-ev',
  templateUrl: './sessions-per-ev.component.html',
  styleUrls: ['./sessions-per-ev.component.css']
})

export class SessionsPerEvComponent implements OnInit {

  constructor(private dataService:DataService) { }

  cars = new Array(100);

  ngOnInit(): void {
  }

  

  

}



