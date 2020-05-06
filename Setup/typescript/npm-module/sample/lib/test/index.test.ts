import * as assert from 'assert';
import * as chai from "chai";
import * as Mocha from 'mocha';
import * as sample from "..";

const suite = Mocha.describe;
const test = Mocha.it;

const expect = chai.expect;

export const BaseTest = () => {
    suite('Base', () => {
        test('init', async () => {
            expect(sample.init("Hello World")).eq("Hello World");
        });
    });
};

BaseTest();
