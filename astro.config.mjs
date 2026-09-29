import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://reimandlab.org',
  // Old Jekyll URLs -> new locations (news posts keep their original URLs)
  redirects: {
    '/team': '/#people',
    '/papers': '/publications/',
    '/posts': '/news/',
    '/research': '/#research',
    '/software': '/#software',
    '/jobs': '/#join',
    '/contact': '/#contact',
  },
});
