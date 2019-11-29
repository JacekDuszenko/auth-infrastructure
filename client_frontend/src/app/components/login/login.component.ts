import {Component} from '@angular/core';
import {Store, Select} from '@ngxs/store';
import {FormGroup} from '@angular/forms';
import {FormlyFieldConfig} from '@ngx-formly/core';
import {Observable} from 'rxjs';
import {UserAction} from '../state/user.state';

@Component({
    selector: 'app-login',
    templateUrl: './login.component.html',
    styleUrls: ['./login.component.css']
})
export class LoginComponent {

    @Select(state => state.user.errorLogin)
    errorLogin$: Observable<boolean>;

    loginForm = new FormGroup({});

    loginFields: FormlyFieldConfig[] = [
        {
            key: 'email',
            type: 'input',
            templateOptions: {
                label: 'Nazwa użytkownika',
                placeholder: 'Wpisz nazwe użytkownika',
                required: true,
                minLength: 5
            }
        },
        {
            key: 'password',
            type: 'input',
            templateOptions: {
                type: 'password',
                label: 'Hasło',
                placeholder: 'Wpisz hasło',
                required: true
            }
        }
    ];


    constructor(public store: Store) {
    }


    login() {
        this.store.dispatch(new UserAction(this.loginForm.value.email, this.loginForm.value.password));

    }

}


