import { Injectable } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/do'

import { PJ_API } from '../../app.api'
import { User } from './user.model';
import { Router } from '@angular/router'

@Injectable()
export class LoginService {

    user: User

    constructor(private http: HttpClient, private router: Router) { }

    isLoggedIn(): boolean {
        return this.user !== undefined
    }


    login(email: String, password: string): Observable<User> {
        return this.http.post<User>(PJ_API + '/api/1.0/login_user/', { username: email, password: password })
            .do(user => this.user = user)
    }

    handleLogin(path?: string) {
        this.router.navigate(['/login'])

    }



}