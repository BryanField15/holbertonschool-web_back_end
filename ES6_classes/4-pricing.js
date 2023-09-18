import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this.setAmount(amount);
    this.setCurrency(currency);
  }

  get amount() {
    return this._amount;
  }

  setAmount(amount) {
    if (typeof amount !== 'number') {
      throw TypeError('amount must be a number');
    }
    this._amount = amount;
  }

  set amount(newAmount) {
    this.setamount(newAmount);
  }

  get currency() {
    return this._currency;
  }

  setCurrency(currency) {
    if (!(currency instanceof Currency)) {
      throw TypeError;
    }
    this._currency = currency;
  }

  set currency(newCurrency) {
    this.setCurrency(newCurrency);
  }

  displayFullPrice() {
    return `${this.amount} ${this._currency.name} (${this._currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
