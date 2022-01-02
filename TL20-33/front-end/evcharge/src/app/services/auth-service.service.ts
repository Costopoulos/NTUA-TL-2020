import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthServiceService {

  constructor(private http:HttpClient) { }
  
  login(data): Observable<any> {
    console.log("sucessfull login");
    return this.http.post("http://localhost:8765/evcharge/api/login", data);
  }

  logout(): Observable<any> {
    console.log("sucessfull logout");
    return this.http.post("http://localhost:8765/evcharge/api/logout",null);
  }

 }
