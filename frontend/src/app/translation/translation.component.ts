import { Component, OnInit } from '@angular/core';
import {ApiService} from '../api.service';

@Component({
  selector: 'app-translation',
  templateUrl: './translation.component.html',
  styleUrls: ['./translation.component.css']
})
export class TranslationComponent implements OnInit {
translations;
  constructor(private apiService: ApiService) { }

  ngOnInit(){
    this.apiService.getTranslations().subscribe((data)=>{
      console.log(data);
      this.translations = data;
    });
  }

}
