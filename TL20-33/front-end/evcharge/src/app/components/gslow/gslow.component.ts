import { Component, OnInit, SkipSelf } from '@angular/core';
import { monkeyPatchChartJsLegend } from 'ng2-charts';
import { DataService } from './../../services/data.service';

@Component({
  selector: 'app-gslow',
  templateUrl: './gslow.component.html',
  styleUrls: ['./gslow.component.css']
})
export class GslowComponent implements OnInit {

  seslist = null
  type1: number;
  type2: number;
  type3: number;

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
    this.dataService.sendGetRequest("SessionsPerStation/").subscribe((data: any) =>{
      console.log(data);
      this.seslist = data;
      this.type1 = this.seslist[0];
      this.type2 = this.seslist[1];
      this.type3 = this.seslist[2];

      console.log(this.type1)
    })
  }

  
}
