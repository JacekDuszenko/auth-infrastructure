import { State, Action, StateContext } from '@ngxs/store';
import { UserAction } from './user.actions';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { tap, catchError } from 'rxjs/operators';
import { of } from 'rxjs';

export class UserStateModel {
  public errorLogin: boolean
}

@State<UserStateModel>({
  name: 'user',
  defaults: {
    errorLogin: null
  }
})
export class UserState {

  constructor(public httpClient: HttpClient) { }

  @Action(UserAction)
  add(ctx: StateContext<UserStateModel>, { email, password }: UserAction) {
    return this.httpClient.post<{ email, password }>('http://localhost:1313/login', { email: email, password: password }).pipe(
      tap(value => {
        console.log('login')
        console.log(value)
        ctx.patchState({
          errorLogin: false
        })
      }),
      catchError((err: HttpErrorResponse) => {
        ctx.patchState({
          errorLogin: true
        })
        return of();
      })
    )
  }
}
