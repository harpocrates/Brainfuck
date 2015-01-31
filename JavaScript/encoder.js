// Generated by CoffeeScript 1.8.0
'use strict';
var exports, generate, generate_table, get_sequence;

String.prototype.repeat = function(n) {
  return Array(n + 1).join(this);
};

get_sequence = function(to, frm) {
  var dif;
  if (frm == null) {
    frm = 0;
  }
  dif = (to - frm) & 255;
  if (dif > 128) {
    return '-'.repeat(256 - dif);
  } else {
    return '+'.repeat(dif);
  }
};

generate_table = function() {
  var T, a, b, c, changes, competitor, from, to, z, _, _i, _j, _k, _l, _len, _len1, _m, _n, _o, _p, _q, _ref, _ref1, _ref2, _ref3;
  T = {};
  for (to = _i = 0; _i < 256; to = ++_i) {
    for (from = _j = 0; _j < 256; from = ++_j) {
      T[from + ' ' + to] = get_sequence(to, from);
    }
  }
  console.log("done first part");
  for (from = _k = 0; _k < 256; from = ++_k) {
    _ref = [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1].concat([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]);
    for (_l = 0, _len = _ref.length; _l < _len; _l++) {
      b = _ref[_l];
      _ref1 = [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1].concat([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]);
      for (_m = 0, _len1 = _ref1.length; _m < _len1; _m++) {
        c = _ref1[_m];
        _ref2 = [from, 0], a = _ref2[0], to = _ref2[1];
        for (_ = _n = 0; _n < 256; _ = ++_n) {
          if (a === 0) {
            competitor = "[" + (get_sequence(b)) + ">" + (get_sequence(c)) + "<]>";
            if (competitor.length < T[from + ' ' + to].length) {
              T[from + ' ' + to] = competitor;
            }
            break;
          }
          _ref3 = [(a + b) & 255, (to + c) & 255], a = _ref3[0], to = _ref3[1];
        }
      }
    }
  }
  console.log("done second part");
  changes = true;
  while (true) {
    changes = false;
    console.log("looping...");
    for (from = _o = 0; _o < 256; from = ++_o) {
      for (to = _p = 0; _p < 256; to = ++_p) {
        for (z = _q = 0; _q < 256; z = ++_q) {
          if (T[from + ' ' + z].length + T[z + ' ' + to].length < T[from + ' ' + to].length) {
            T[from + ' ' + to] = T[from + ' ' + z] + T[z + ' ' + to];
            changes = true;
          }
        }
      }
    }
    if (changes) {
      break;
    }
  }
  console.log("done third part");
  return T;
};

generate = function(string, T) {
  var i, n, prev, to_parse, to_return, _i, _len, _ref;
  _ref = [
    (function() {
      var _i, _ref, _results;
      _results = [];
      for (i = _i = 0, _ref = string.length; 0 <= _ref ? _i < _ref : _i > _ref; i = 0 <= _ref ? ++_i : --_i) {
        _results.push(string.charCodeAt(i));
      }
      return _results;
    })(), ""
  ], to_parse = _ref[0], to_return = _ref[1];
  prev = null;
  for (_i = 0, _len = to_parse.length; _i < _len; _i++) {
    n = to_parse[_i];
    if (prev === null) {
      to_return += T[0 + ' ' + n] + '.';
    } else if (T[prev + ' ' + n].length < T[0 + ' ' + n].length + 1) {
      to_return += T[prev + ' ' + n] + '.';
    } else if (prev !== null) {
      to_return += '>' + T[0 + ' ' + n] + '.';
    } else {
      to_return += T[0 + ' ' + n] + '.';
    }
    prev = n;
  }
  return to_return;
};

if (typeof exports === "undefined" || exports === null) {
  exports = {};
}

exports.generate = generate;

exports.generate_table = generate_table;