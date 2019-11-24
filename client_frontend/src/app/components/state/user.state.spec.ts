import {TestBed, async} from '@angular/core/testing';
import {NgxsModule, Store} from '@ngxs/store';
import {UserAction, UserState} from './user.state';

import {HttpClient, HttpClientModule} from '@angular/common/http';
import {of} from 'rxjs';


describe('Test actions', () => {
    let store: Store;
    let httpClient: HttpClient;

    beforeEach(async(() => {
        TestBed.configureTestingModule({
            imports: [NgxsModule.forRoot([UserState]), HttpClientModule]
        }).compileComponents();
        store = TestBed.get(Store);
        httpClient = TestBed.get(HttpClient);
    }));

    it('should create an action and login failed', () => {
        spyOn(httpClient, 'post').and.returnValue(of({authorisation: false}));
        store.dispatch(new UserAction('item-1', 'item-2'));
        store.selectOnce(state => state.user.errorLogin).subscribe((errorLogin: boolean) => {
            expect(errorLogin).toEqual(true);
        });
    });

    it('should create an action and login succeeded', () => {
        spyOn(httpClient, 'post').and.returnValue(of({authorisation: true}));
        store.dispatch(new UserAction('item-3', 'item-4'));
        store.selectOnce(state => state.user.errorLogin).subscribe((errorLogin: boolean) => {
            expect(errorLogin).toEqual(false);

        });
    });
});
