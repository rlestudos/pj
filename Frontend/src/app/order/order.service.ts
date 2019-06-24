import { Injectable } from '@angular/core'

import { Headers, RequestOptions, Http } from '@angular/http'
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs/Observable'
import 'rxjs/add/operator/map'

import { ShoppingCartService } from '../restaurant-detail/shopping-cart/shopping-cart.service'
import { CartItem } from '../restaurant-detail/shopping-cart/cart-item.model'
import { Order } from './order.model'
import { PJ_API } from 'app/app.api';
import { LoginService } from '../security/login/login.service'


@Injectable()
export class OrderService {

  constructor(private cartService: ShoppingCartService,
    private http: Http,
    private loginService: LoginService) { }

  itemsValue(): number {
    return this.cartService.total()
  }

  cartItems(): CartItem[] {
    return this.cartService.items
  }

  increaseQty(item: CartItem) {
    this.cartService.increaseQty(item)
  }

  decreaseQty(item: CartItem) {
    this.cartService.decreaseQty(item)
  }

  remove(item: CartItem) {
    this.cartService.removeItem(item)
  }

  clear() {
    this.cartService.clear()
  }

  
  checkOrder(order: Order): Observable<string> {
    const headers = new Headers()
    headers.append('Content-Type', 'application/json')
    return this.http.post(PJ_API + '/orders/',
      JSON.stringify(order),
      new RequestOptions({ headers: headers }))
      .map(response => response.json())
      .map(order => order.id)
  }
  
/*
  checkOrder(order: Order): Observable<string> {
    let headers = new HttpHeaders()
    if(this.loginService.isLoggedIn())
    {
      headers = headers.set('Autorization', 'Token ${this.loginService.user.token}')  
    }
    return this.http.post<Order>(PJ_API + '/orders/',
      order,{ headers: headers })
      .map(order => order.id)
  }
  */

}
