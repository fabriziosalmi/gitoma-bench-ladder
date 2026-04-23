export function renderGreeting(name) {
  const escapedName = name.replace(/&/g, '&amp;');
  return `<div class="greeting">Hello, ${escapedName}!</div>`;
}