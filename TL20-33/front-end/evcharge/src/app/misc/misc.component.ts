import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DataService } from 'src/app/services/data.service';
import { ChartType, ChartOptions } from 'chart.js';
import { Label } from 'ng2-charts';
//import * as pluginDataLabels from 'chartjs-plugin-datalabels';

@Component({
  selector: 'app-misc',
  templateUrl: './misc.component.html',
  styleUrls: ['./misc.component.css']
})
export class MiscComponent implements OnInit {

  chargeType: any;
  values: any;
  seslist = null
  type1 = 25;
  type2 = 25;
  type3 = 50;

  constructor(private dataService: DataService, private route: ActivatedRoute) {
    this.route.params.subscribe((data: any) =>{
      this.chargeType = data;
      console.log(data);
      this.type1 = 25;
      this.type2 = 26;
      this.type3 = 54;

    })
   }

  ngOnInit(): void {
    this.dataService.sendGetRequest("SessionsPerStation/").subscribe((data: any) =>{
      this.values = data;
      console.log(data);
      this.seslist = data;
      // this.type1 = this.seslist[0];
      // this.type2 = this.seslist[1];
      // this.type3 = this.seslist[2];
  
    })
  }

  fillpie(): void {
    this.pieChartData = [50, 23, 27];
  }


  public pieChartOptions: ChartOptions = {
    responsive: true,
    legend: {
      position: 'top',
    },
    plugins: {
      datalabels: {
        formatter: (value, ctx) => {
          const label = ctx.chart.data.labels[ctx.dataIndex];
          return label;
        },
      },
    }
  };


  public pieChartLabels: Label[] = [['slow'], ['medium'], 'fast'];
  public pieChartData: number[] = [this.type1, this.type2, this.type3];
  public pieChartType: ChartType = 'pie';
  public pieChartLegend = true;
  ///public pieChartPlugins = [pluginDataLabels];
  public pieChartColors = [
    {
      backgroundColor: ['rgba(255,0,0,0.3)', 'rgba(0,255,0,0.3)', 'rgba(0,0,255,0.3)'],
    },
  ];


}
