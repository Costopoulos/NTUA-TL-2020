import {Component, OnInit, Inject} from '@angular/core';
import {FormGroup, FormControl, Validators} from '@angular/forms';
import {MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';

@Component({
  selector: 'app-newpay',
  templateUrl: './newpay.component.html',
  styleUrls: ['./newpay.component.css']
})
export class NewpayComponent implements OnInit {

  constructor(public dialogRef: MatDialogRef<NewpayComponent>,
    @Inject(MAT_DIALOG_DATA) public data: FormGroup) {

    this.data = new FormGroup({
      amount: new FormControl('', [Validators.required]),
      method: new FormControl('', [Validators.required]),
      bank: new FormControl('', [Validators.required]),
    })
  }

  ngOnInit(): void {

  }

  onNoClick(): void {
    this.dialogRef.close();
  }

}