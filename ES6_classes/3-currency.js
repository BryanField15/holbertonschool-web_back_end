export default class Currency {
  constructor(code, name) {
    this.setCode(code);
    this.setName(name);
  }

  get code() {
    return this._code;
  }

  setCode(code) {
    if (typeof code !== 'string') {
      throw TypeError('code must be a string');
    }
    this._code = code;
  }

  set code(newCode) {
    this.setCode(newCode);
  }

  get name() {
    return this._name;
  }

  setName(name) {
    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    }
    this._name = name;
  }

  set name(newName) {
    this.setName(newName);
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
