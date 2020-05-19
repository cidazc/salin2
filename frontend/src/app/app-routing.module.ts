import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {NewsComponent} from './news/news.component';
import {TranslationComponent} from './translation/translation.component'
const routes: Routes = [
  {path:'news', component: NewsComponent},
  {path:'translation', component: TranslationComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
