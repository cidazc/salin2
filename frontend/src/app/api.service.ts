import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  API_KEY = '59fcaaf165844884a3573f6465832a2b';
  constructor(private httpClient: HttpClient) { }


public getNews(){
  return this.httpClient.get(`https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=${this.API_KEY}`);
};
public getHeroes(){
  return this.httpClient.get(`http://localhost:8000/heroes/?format=json`);
};
public getTranslations(){
  return this.httpClient.get(`http://localhost:8000/translations/?format=json`);
};

}
