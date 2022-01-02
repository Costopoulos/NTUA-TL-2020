import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})

export class DataService {

  private REST_API_SERVER = 'http://localhost:8765/evcharge/api/';

  constructor(private httpClient: HttpClient) { }

  public sendGetRequest(url: String) {
    this.REST_API_SERVER = 'http://localhost:8765/evcharge/api/' + url;
    return this.httpClient.get(this.REST_API_SERVER);
  }

  public sendPostRequest(url: String, httpParams: HttpParams) {
    this.REST_API_SERVER = 'https://localhost:8765/evcharge/api/' + url;
    console.log(httpParams.toString());
    return this.httpClient.post(this.REST_API_SERVER,
                                httpParams.toString(),
                                {
                                  headers: new HttpHeaders()
                                    .set('Content-Type', 'application/x-www-form-urlencoded')
                                });
  }

  public sendEasyPost(url: string) {
    this.REST_API_SERVER = 'http://localhost:8765/evcharge/api/admin/addpayment/' + url;
    return this.httpClient.get(this.REST_API_SERVER);
  }

  public payment(url: string) {
    this.REST_API_SERVER = url;
    return this.httpClient.get(this.REST_API_SERVER);
  }





  // public sendGetRequest() {
  //   //this.REST_API_SERVER += url;
  //   return this.httpClient.get("http://localhost:8765/SessionsPerStation/4");
  // }


}
