import { expect } from "chai";
import { myFunction } from "../src/myFunction.js";

describe("Test missing cases", () => {
  it("should handle error case", () => {
    expect(myFunction()).to.throw(Error);
  });
});