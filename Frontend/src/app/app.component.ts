import {Component, OnInit} from "@angular/core"

@Component({
  selector: 'pj-app',
  templateUrl: 'app.component.html'
})
export class AppComponent implements OnInit {

  content = 'PJ App!'

  constructor() { }

  ngOnInit() {
  }

}
