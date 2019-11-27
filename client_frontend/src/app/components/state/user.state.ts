import {State, Action, StateContext} from '@ngxs/store';

import {HttpClient} from '@angular/common/http';

export class UserAction {
    static readonly type = '[User] Login';

    constructor(public email: string, public password: string) {
    }
}

export class UserStateModel {
    public errorLogin: boolean;
}

@State<UserStateModel>({
    name: 'user',
    defaults: {
        errorLogin: null
    }
})
export class UserState {

    constructor(public httpClient: HttpClient) {
    }
    @Action(UserAction)
    add(ctx: StateContext<UserStateModel>, {email, password}: UserAction) {
        console.log(email, password);
        this.httpClient.post('login', {email: email, password: password})
            .subscribe((response) => {
                try {
                    const resp = response as any;
                    console.log(resp);
                    if (resp.authorisation === true) { 
                        this.authorizeUser(ctx);
                    } else {
                        this.invalidateUser(ctx);
                    }
                } catch (error) {
                    this.invalidateUser(ctx);
                }
            });
    }
    private authorizeUser(ctx: StateContext<UserStateModel>) {
        ctx.patchState({
            errorLogin: false
        });
    }
    private invalidateUser(ctx: StateContext<UserStateModel>) {
        ctx.patchState({
            errorLogin: true
        });
    }
}
