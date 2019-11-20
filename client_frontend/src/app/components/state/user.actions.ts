export class UserAction1 {
  static readonly type = '[User] Login';
  constructor(public email: string, public password: string) { }
}
