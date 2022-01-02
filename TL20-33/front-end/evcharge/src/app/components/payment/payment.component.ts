import { Component, OnInit } from '@angular/core';
import { DataService } from './../../services/data.service';
import { MatDialog } from '@angular/material/dialog';
import { NewpayComponent } from './../newpay/newpay.component';
import { HttpParams } from '@angular/common/http';

@Component({
  selector: 'app-payment',
  templateUrl: './payment.component.html',
  styleUrls: ['./payment.component.css']
})
export class PaymentComponent implements OnInit {

  newPayment = null;
  amount = null;
  method = null;
  bank = null;
  url = null;
  superurl = null;

  constructor(private dataService: DataService, public dialog: MatDialog) { }

  ngOnInit(): void {
  }

  openDialog(): void {
    const dialogRef = this.dialog.open(NewpayComponent, {
      width: '250px',
      height : 'auto',
      data: null
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('Dialog Closed');
      if (result !== undefined) {
        this.newPayment = result.value;
        this.submitForm();
      }
    });
  }

  submitForm(): void {
    this.amount = this.newPayment.amount;
    this.method = this.newPayment.method;
    console.log(this.amount);
    this.bank = this.newPayment.bank;

    this.url = this.amount + "/" + this.method + "/" + this.bank;
    console.log(this.url);
    console.log("correct url is");

    this.superurl = "http://localhost:8765/evcharge/api/admin/addpayment/" + this.url;

    console.log(this.superurl);
    
    //this.dataService.sendEasyPost(this.amount + "/" + this.method + "/" + this.bank);
    this.dataService.payment(this.superurl);
    //this.dataService.sendGetRequest(this.url);
  }

  submitForm2(): void {
    let httpParams = new HttpParams()
                      .set('AddressCity',this.newPayment.AddressCity)
                      .set('AddressStreet',this.newPayment.AddressStreet)
                      .set('AddressNumber',this.newPayment.AddressNumber)
    this.dataService.sendPostRequest("stores/insert",httpParams).subscribe( // EDW TO URL
      (response) => {console.log(response);this.ngOnInit();},
      (error) => console.log(error)
    );
  }

}
