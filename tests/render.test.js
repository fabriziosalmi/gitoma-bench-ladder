import test from "node:test";
import assert from "node:assert/strict";

import { renderGreeting } from "../src/render.js";

test("normal name renders inside a div", () => {
  const html = renderGreeting("Alice");
  assert.equal(html, '<div class="greeting">Hello, Alice!</div>');
});

test("ampersand in name is escaped to entity", () => {
  // Pre-fix: the literal & passes through as-is, breaking
  // entity-decode roundtrip.
  const html = renderGreeting("Tom & Jerry");
  assert.match(
    html,
    /&amp;/,
    "raw & must be escaped to &amp; in HTML output",
  );
});

test("script tag in name is rendered as text, NOT as a script element", () => {
  // The XSS payload — pre-fix, this test FAILS because the raw
  // <script> tag is interpolated into the HTML and the browser
  // would execute it. Post-fix, the <, >, /, etc. are entity-escaped
  // and the output is harmless text.
  const payload = "<script>alert(1)</script>";
  const html = renderGreeting(payload);
  assert.doesNotMatch(
    html,
    /<script[^>]*>/i,
    `XSS leak: rendered output contains a real <script> tag for input ${JSON.stringify(payload)}`,
  );
  // And the literal payload appears as escaped text.
  assert.match(html, /&lt;script&gt;/, "payload must be entity-escaped");
});

test("attribute-context payload is also neutralised", () => {
  // Even if a future caller embeds the result in an attribute, the
  // escape function should kill quote-breakouts. Pre-fix: raw " breaks
  // out. Post-fix: " becomes &quot;.
  const html = renderGreeting('"><img src=x onerror=alert(1)>');
  assert.doesNotMatch(
    html,
    /<img\s+src=/i,
    "attribute-context XSS leak: <img> tag was injected verbatim",
  );
});
