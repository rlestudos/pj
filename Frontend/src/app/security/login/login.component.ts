import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms'
import {ActivatedRoute, Router} from '@angular/router'
import { LoginService } from './login.service';

import { NotificationService } from '../../shared/messages/notification.service'


@Component({
  selector: 'pj-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  loginForm: FormGroup
  navigateTo: string

  constructor(private fb: FormBuilder,
    private loginService: LoginService,
    private notificationService: NotificationService,
    private activatedRoute: ActivatedRoute,
    private router: Router) { }

  ngOnInit() {
    this.loginForm = this.fb.group({
      email: this.fb.control('', [Validators.required]),
      password: this.fb.control('', [Validators.required])
    })
    this.navigateTo = this.activatedRoute.snapshot.params['to'] || '/'
  }

  login() {
    this.loginService.login(this.loginForm.value.email, this.loginForm.value.password)
      .subscribe(user => this.notificationService.notify('Login efetuado'),
        response => this.notificationService.notify('Dados Invalidos!'),
        ()=>{this.router.navigate([this.navigateTo])}
        )

  }


}
