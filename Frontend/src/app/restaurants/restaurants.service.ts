import { Injectable } from '@angular/core'
import { HttpClient, HttpParams } from '@angular/common/http'

import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map'
import 'rxjs/add/operator/catch'
import { ErrorHandler } from 'app/app.error-handler';


import { Restaurant } from "./restaurant/restaurant.model";
import { MenuItem } from '../restaurant-detail/menu-item/menu-item.model'

import { PJ_API } from '../app.api'

@Injectable()
export class RestaurantsService {


    constructor(private http: HttpClient) { }

    restaurants(): Observable<Restaurant[]> {
        return this.http.get(PJ_API + /restaurants/)
            .catch(ErrorHandler.handleError)

    }

    restaurantById(id: string): Observable<Restaurant> {
        return this.http.get(PJ_API + /restaurants/ + id)
            .catch(ErrorHandler.handleError)
    }

    reviewsOfRestaurant(id: string): Observable<any> {
        return this.http.get(PJ_API + /reviews/ + '?restaurantId=' + id)            
            .catch(ErrorHandler.handleError)
    }

    menuOfRestaurant(id: string): Observable<MenuItem[]> {
        return this.http.get<MenuItem[]>(PJ_API + /menu/ + '?restaurantId=' + id)           
            .catch(ErrorHandler.handleError)
    }


}
