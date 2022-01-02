import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { DataService } from './../../services/data.service';

@Component({
  selector: 'app-evpage',
  templateUrl: './evpage.component.html',
  styleUrls: ['./evpage.component.css']
})
export class EvpageComponent implements OnInit {

  sessions = null;
  show_transactions = true;
  id: number;

  constructor(private dataService: DataService, private route: ActivatedRoute, private router: Router) { }

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      this.dataService.sendGetRequest("SessionsPerEV/" + params.get('Car_id')).subscribe((data: any) =>{
        console.log(data);
        this.sessions = data;
        this.id = this.sessions[0].Car_id;
      });
    });
  }

  onClickMe():void {
    this.show_transactions = true;
  }

}
