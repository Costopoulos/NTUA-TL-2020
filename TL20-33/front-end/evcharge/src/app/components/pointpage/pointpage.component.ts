import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { DataService } from './../../services/data.service';

@Component({
  selector: 'app-pointpage',
  templateUrl: './pointpage.component.html',
  styleUrls: ['./pointpage.component.css']
})
export class PointpageComponent implements OnInit {

  points = null;
  show_transactions = true;
  id: any;

  constructor(private dataService: DataService, private route: ActivatedRoute, private router: Router) { }

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      this.dataService.sendGetRequest("SessionsPerPoint/" + params.get('Point_id')).subscribe((data: any) =>{
        console.log(data);
        this.points = data;
        this.id = this.points[0].Point_id;
      });
    });
  }

  onClickMe():void {
    this.show_transactions = true;
  }

}
