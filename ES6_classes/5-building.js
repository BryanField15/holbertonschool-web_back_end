export default class Building {
  constructor(sqft) {
    this._sqft = sqft;

    if (this.evacuationWarningMessage !== Building.prototype.evacuationWarningMessage) {
      this.evacuationWarningMessage();
    }
  }

  get sqft() {
    return this._sqft;
  }

  // eslint-disable-next-line class-methods-use-this
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
