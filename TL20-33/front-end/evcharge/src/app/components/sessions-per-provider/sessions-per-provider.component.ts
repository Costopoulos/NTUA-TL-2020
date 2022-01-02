import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router'
import { DataService } from './../../services/data.service';
import { HttpParams } from '@angular/common/http'

@Component({
  selector: 'app-sessions-per-provider',
  templateUrl: './sessions-per-provider.component.html',
  styleUrls: ['./sessions-per-provider.component.css']
})
export class SessionsPerProviderComponent implements OnInit {

  constructor(private dataService:DataService) { }

  seslist: any=[];
  providers = new Array(5);

  ngOnInit(): void {
  }


}
