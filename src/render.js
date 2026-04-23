// Tiny HTML renderer — the buggy side of rung-4.
//
// The `renderGreeting` function below interpolates the `name` argument
// directly into an HTML template literal. Any `name` that contains
// HTML metacharacters (`<`, `>`, `&`, `"`, `'`) breaks out of its
// intended text context. The classic XSS payload is `<script>alert(1)
// </script>` — the rendered output contains a real <script> tag the
// browser will execute.
//
// Fix: HTML-escape the input before interpolation. Any equivalent
// (DOMPurify, manual replace, server-side templating engine with
// auto-escape) is fine as long as the special characters never reach
// the output as raw HTML.
//
// The companion tests in `tests/render.test.js` pin both the happy
// path and the XSS payload — pre-fix the second test fails.

export function renderGreeting(name) {
  return `<div class="greeting">Hello, ${name}!</div>`;
}
