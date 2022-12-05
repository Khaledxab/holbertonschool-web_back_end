'use strict';
const request = require('request');
const chai = require('chai');

describe('basic integration testing', () => {
    it('Main page content', (done) => {
        request('http://localhost:7865', (err, res, body) => {
            chai.expect(body).to.equal('Welcome to the payment system');
            done();
        });
    });
    it('Main page status', (done) => {
        request('http://localhost:7865', (err, res, body) => {
            chai.expect(res.statusCode).to.equal(200);
            done();
        });
    });
}
);
