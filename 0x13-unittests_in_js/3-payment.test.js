'use strict';
const chai = require('chai');
const sinon = require('sinon');

const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./3-payment.js');

describe('sendPaymentRequestToApi function', () => {
    it('validate the usage of the Utils function', () => {
        const spy = sinon.spy(Utils, 'calculateNumber');
        sendPaymentRequestToApi(100, 20);
        chai.expect(spy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
        spy.restore();
        stubUtils.restore()
        spyConsole.restore();
    });
});