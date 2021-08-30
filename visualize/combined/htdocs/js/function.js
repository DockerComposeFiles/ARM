/*own jQuery selector
  $ as selector over all
  $f as selector to select first element
 */
var $ = function (object) {
    return document.querySelectorAll(object);
};
var $f = function (object) {
    return document.querySelector(object);
};
console.log("function.min.js success");
//# sourceMappingURL=function.js.map