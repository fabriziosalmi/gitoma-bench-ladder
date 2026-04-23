export function renderGreeting(name) {
  // Neutralize attribute-context payloads by escaping special characters for safe rendering.
  const escapedName = name.replace(/&/g, '&amp;')
  return `<div class="greeting">Hello, ${escapedName}!</div>`;
}