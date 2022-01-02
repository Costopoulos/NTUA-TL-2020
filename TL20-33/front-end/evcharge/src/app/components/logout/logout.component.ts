import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { AuthServiceService } from 'src/app/services/auth-service.service';

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.css']
})
export class LogoutComponent implements OnInit {

  formGroup: FormGroup;

  constructor(private authService: AuthServiceService) { }

  ngOnInit() {
  }

  

  logoutProcess(){
    this.authService.logout().subscribe(result =>{
      if (result.success){
        console.log(result);
        alert(result.message);
      } else {
        alert(result.message);
      }
    });
  }

}