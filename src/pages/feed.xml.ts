import type { APIRoute } from 'astro';
import { getNews, site } from '../lib/data';

const esc = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

export const GET: APIRoute = async ({ site: base }) => {
  const items = (await getNews()).slice(0, 30).map((n) => {
    const link = n.href ? new URL(n.href, base).href : new URL('/news/', base).href;
    return `<item><title>${esc(n.text)}</title><link>${esc(link)}</link><guid isPermaLink="false">${esc(n.date.toISOString() + n.text)}</guid><pubDate>${n.date.toUTCString()}</pubDate><category>${n.type}</category></item>`;
  });
  const xml = `<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>${esc(site.name)}</title><link>${base}</link><description>${esc(site.tagline)}</description>${items.join('')}</channel></rss>`;
  return new Response(xml, { headers: { 'Content-Type': 'application/rss+xml; charset=utf-8' } });
};
