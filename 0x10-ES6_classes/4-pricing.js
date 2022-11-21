import Currency from "./3-currency";

class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
    }

    get amount() {
        return this._amount;
        }
    
    set amount(newAmount) {
        if (typeof amount === 'number') this._amount = newAmount;
    }

    get currency() {
        return this._currency;
        }
    
    set currency(newCurrency) {
        if (currency instanceof Currency) this._currency = newCurrency;
    }

    displayFullPrice() {
        return `${this._amount} ${this._currency.displayFullCurrency()}`;
    }

    static convertPrice(amount, conversionRate) {
        return amount * conversionRate;
    }

}

export default Pricing;
