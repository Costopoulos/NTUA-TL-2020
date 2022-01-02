import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { AuthServiceService } from 'src/app/services/auth-service.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  formGroup: FormGroup;

  constructor(private authService: AuthServiceService) { }

  ngOnInit() {
    this.initForm();
  }

  initForm(){
    this.formGroup = new FormGroup({
      username: new FormControl(''),
      password: new FormControl('')
    })
  }

  loginProcess(){
    this.authService.login(this.formGroup.value).subscribe(result =>{
      if (result.success){
        //console.log(result);
        //alert(result.message);
      } else {
        if(result.message != undefined)
          alert(result.message);
        else 
          alert("Logged in successfully");
      }
    });
  }

}
